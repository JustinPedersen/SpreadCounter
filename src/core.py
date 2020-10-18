import numpy as np
import imutils
import xlwt
from xlwt import Workbook
import cv2
import os


"""
IDEAS:

if a group of pixel's area is greater than a cutoff value, remove them.
This will cut out huge blobs in the mask. 
"""


def generate_spreadsheet():
    """
    Create a base spreadsheet and Sheet 1 on it.
    :return:
    """
    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create a sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    sheet1.write(0, 0, 'Image')
    sheet1.write(0, 1, 'Count')
    sheet1.write(0, 2, 'Adjusted Count')

    return wb, sheet1


def single_threshold_mask(input_image, upper_limit=255, lower_limit=200):
    """
    :param input_image: The image to process.
    :param upper_limit: The upper limit to clamp by
    :param lower_limit: The lower limit to clamp by
    :return: A mask of the clamped image.
    """
    working_image = input_image.copy()

    upper = np.array([upper_limit], dtype="uint8")
    lower = np.array([lower_limit], dtype="uint8")
    mask = cv2.inRange(working_image, lower, upper)
    return cv2.dilate(mask, None, iterations=1)


def multi_threshold_mask(input_image, threshold_range=(180, 200)):
    """
    Threshold an image in multiple passes for cleaner results.

    :param input_image: The image to process.
    :param threshold_range: The begin and end lower ranges to use during the thresholding process.
    :return: The generated mask.
    """
    working_image = input_image.copy()

    # create a blank mask
    mask = np.zeros_like(working_image)

    # Upper clamp limit
    upper = np.array([255], dtype="uint8")

    # Create a kernel to help filter out noise.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    for lower_threshold in range(threshold_range[0], threshold_range[1]):
        prev_mask = mask.copy()
        lower = np.array([lower_threshold], dtype="uint8")
        mask = cv2.inRange(working_image, lower, upper)
        mask = cv2.bitwise_or(mask, prev_mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask


def find_circles_in_dish(image_path, write_path=None, debug_path=None, thresholding_type=0,
                         max_threshold=255, min_threshold=200, contrast_multiplier=1.0,
                         scale_factor=1.0, mask_offset=0.85, max_dish_radius_offset=0.5, min_dish_radius_offset=0.2,
                         circle_min_dist=5, circle_min_rad=1, circle_max_rad=10,
                         draw_dish_circle=True, draw_circle=True, draw_center=True, draw_count=True):
    """
    Find circles within a big circle in the image. First we detect the dish itself, shrink the radius a bit
    and then mask out the rest of the image. After we process the image to make detection easier and count
    spots from there.

    :param str image_path: Path to the image to process.
    :param str write_path: If present, will write the processed image to this location.
    :param str debug_path: If present, will write the debug image to this location.
    :param int thresholding_type: The type of thresholding to use.
                                  0 - single
                                  1 - Multi
    :param int max_threshold: The upper thresholding limit for the image mask.
    :param int min_threshold: The Lower thresholding limit for the image mask.
    :param float contrast_multiplier: Offset the image's contrast by a factor.
    :param float scale_factor: The factor to scale the image by
    :param float mask_offset: The Amount to shrink the dish search area by. This will avoid detecting
                              parts of the rim as false positives as well as any dots on the edge of the dish.
    :param float max_dish_radius_offset: The Max size of the dish relative to the image width and height.
    :param float min_dish_radius_offset: The Min size of the dish relative to the image width and height.
    :param int circle_min_dist: The min dist between circles to be detected in the dish.
    :param int circle_min_rad: The min radius of circles in the dish.
    :param int circle_max_rad: The max radius of circles in the dish.
    :param bool draw_dish_circle: If True will draw the circle of the dish and its offset. Useful for debugging.
    :param bool draw_circle: If True will draw a circle around any found dots.
    :param bool draw_center: If True will draw the circle center for any found dots.
    :param bool draw_count: If True will draw the circle count in the top right corner.
    :return:
    """
    # Read in the original search image and make a copy of it.
    search_image = cv2.imread(image_path).copy()
    orig_width, orig_height = search_image.shape[:2]

    # Resize the search image by a given factor, so it computes faster.
    resize_image = cv2.resize(search_image, (0, 0), fx=scale_factor, fy=scale_factor)
    width, height = resize_image.shape[:2]

    # Calculating the image resize factor.
    resize_factor = (orig_width / width)

    # Create a grey image copy of the resize image for even faster computation.
    grey_image = cv2.cvtColor(resize_image.copy(), cv2.COLOR_BGR2GRAY)

    # Calculate the min + max dish distance relative to the size of the image.
    min_dist = (width + height) / 2
    max_dish_radius = int(min_dist * max_dish_radius_offset)
    min_dish_radius = int(min_dist * min_dish_radius_offset)

    # Detecting the dish itself to use as a mask and estimated size of the dish.
    dish_circles = cv2.HoughCircles(image=grey_image,
                                    method=cv2.HOUGH_GRADIENT,
                                    dp=1,
                                    minDist=min_dist,
                                    param1=118,
                                    param2=8,
                                    minRadius=min_dish_radius,
                                    maxRadius=max_dish_radius)
    dish_circles = np.uint16(np.around(dish_circles))

    # amplify the contrast of the image
    grey_image = cv2.convertScaleAbs(grey_image, alpha=contrast_multiplier, beta=1)

    # Create a mask + draw on it.
    mask = np.zeros((width, height), np.uint8)

    # Draw a mask for the image with the located dish. this will ensure no false positives outside of the dish.
    for i in dish_circles.copy()[0, :]:
        i[2] = i[2] * mask_offset
        cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), thickness=-1)

    # Copy that image using that mask
    masked_data = cv2.bitwise_and(grey_image, grey_image, mask=mask)

    if thresholding_type == 0:
        mask = single_threshold_mask(masked_data,
                                     upper_limit=max_threshold,
                                     lower_limit=min_threshold)
    elif thresholding_type == 1:
        mask = multi_threshold_mask(masked_data,
                                    threshold_range=(min_threshold, max_threshold))

    if thresholding_type > 1:
        mask = masked_data

    # Write the mask out to disc for debugging purposes.
    if debug_path:
        cv2.imwrite(debug_path, mask)

    # Detect smaller circles in the image
    circles = cv2.HoughCircles(image=mask,
                               method=cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=circle_min_dist,
                               param1=118,
                               param2=8,
                               minRadius=circle_min_rad,
                               maxRadius=circle_max_rad)

    # If the user wants the dish circle drawn, do it here but on the original image.
    if draw_dish_circle:
        for i in dish_circles[0, :]:
            # resizing for the scale factor.
            i[0] = int(i[0]*resize_factor)
            i[1] = int(i[1]*resize_factor)
            i[2] = int(i[2]*resize_factor)
            thickness = int(2 * resize_factor)
            cv2.circle(search_image, (i[0], i[1]), i[2], (255, 255, 255), thickness)

            i[2] = i[2] * mask_offset
            cv2.circle(search_image, (i[0], i[1]), i[2], (210, 210, 210), thickness)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        if circles.any():
            # Draw the centers and circles for found dots.
            for i in circles[0, :]:
                i[0] = int(i[0] * resize_factor)
                i[1] = int(i[1] * resize_factor)
                i[2] = int(i[2] * resize_factor)
                thickness = int(2 * resize_factor)

                if draw_circle:
                    cv2.circle(search_image, (i[0], i[1]), i[2], (0, 255, 0), thickness)

                if draw_center:
                    cv2.circle(search_image, (i[0], i[1]), 2, (0, 0, 255), thickness)

            # n_centers = cv2.connectedComponents(mask)[0] - 1
            # print(f'detected {n_centers} circles')

            if draw_count:
                text = str(circles.shape[1])
                cv2.putText(search_image, text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if write_path:
            cv2.imwrite(write_path, search_image)

        return {'count': circles.shape[1]}

    else:
        if write_path:
            cv2.imwrite(write_path, search_image)

        return {'count': 0}
