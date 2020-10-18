# SpreadCounter
A faster way to count petri dish spreads! 

# What is this? 
This project originally started as a cool excuse to mess around with OpenCV computer vision in an attempt to aid in
counting spots on a petri dish for my better half's lab work. 

Counting colonies on a dish can, in the best of times be a tedious task when you have a few hundred to get through.
However, counting circular objects in an image can be a trivial task for computers. This application aims to speed up
the process of counting spots as well as provide that data back in an easily manipulated and presentable format such
as excel spreadsheets and marked images.

# How does it work?
![Main UI](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/main_ui_000.png)

Spread counter takes an input set of images and performs some image processing on them, and then to the 
best of its ability will count all the circles it can find in the image. Almost all operations
performed on the images can be customised and fine-tuned by the user on a per-project basis.

First the image is read in, then it is scaled down by a factor so that it is easier to process.
Then the image is converted to greyscale so that it is even easier to work with. From there
if the user so chooses the Dish itself will be located within the image, and a mask will be created
so that all the pixels around the dish are black. This will alienate any false positives from being
counted outside of the dish. 

The image then has its contrast enhanced, so the particles are easier to pick out from the media.
If the user so chooses the image can then be processed further or just used as is. For some images
further processing is necessary. A threshold can be applied to the image so that all the values
are clamped. 

Finally, Image recognition is run on the image, circular spots are then detected and counted.

In this image on the right-hand side is the input image with the counted spots circled and on the 
left-hand side the grey, masked out image that the image recognition was run on. 

![Counted spots](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/main_ui_001.png)

# UI Overview
![Annotated UI](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/main_ui_002.png)
1. Process images: Once clicked will begin processing all the images in the current project's input_images folder.
2. Image: The name of the current image being displayed.
3. Project: The name of the current project.
4. Preview: The Index of the current image being previewed.
5. The Counted image displaying all the circles that were counted. These images are stored in the output_images folder.
6. The debug image, this is what the computer sees and actually counts.
7. Prev: See the previous image. 
8. Next: See the next image.
9. Count Offset: Often the machine count will be incorrect. This will offset the number of counted circles.
You can scroll over this field to update it or use the arrow keys.
10. Count: The final count, both machine and offset count.
11. Image Scale Factor: How much to scale the debug image by. Smaller will be faster. **NOTE**: Altering this setting will
change the other parameters under circle detection settings, so it is best to find a good value for this early on. 
A value between 0.2 and 0.5 is recommended. 
12. Contrast Multiplier: How much contrast to apply to the image. More contrast makes for more accurate detection.
13. Thresholding: Optional setting for any image thresholding.

    None: Leave the image as is.
    
    Single: Threshold the image once.
    
    Multi: Threshold the image in multiple passes cleaning up small specs as it goes.

14. Upper Threshold: The lightest value to clamp by.
15. Lower Threshold: The darkest value to clamp by.
16. Dish Detection: If enabled, the dish will be located in the image and masked out.
17. Max dish offset radius: The max radius of the dish relative to the size of the image.
18. Min dish offset radius: The min radius of the dish relative to the size of the image.

    Default values for these are fine as long as the dish is framed the same as the example images.

19. Dish offset %: Once the dish is located, scale its radius in by this percentage. This is here
to prevent the edges of the dish being counted and creating false positives. A value of 1.0 will result 
in the dish scale not being offset at all. This can be seen in the image: (5) with the smaller white circle. 

20. Colony Min Dist: The minimum distance allowed between circle centers. If you see many overlapping false positives
consider slowly upping this value. 
21. Colony min Radius: The minimum allowed radius for a circle to be counted. If too many tiny specs in the image
are counted, consider slowly upping this value.
22. Colony max Radius: The maximum allowed radius for a circle to be counted. If blobs bigger than the actual colonies
are being counted, slowly lower this value. Vise versa, if the bigger circles aren't being counted, slowly up this value.

    **NOTE:** As mentioned above, changing the image Scale factor (11) will alter these values and they will need to be 
    adjusted accordingly.
23: Draw centers: Draw the centers of located circles.
24: Draw circles: Draw a circle around the counted colonies.
25: Draw Dish Circle: Draw a circle around the dish itself.
26: Draw count: Draw the machine counted number on the image itself.    

# Project creation
To create a new project simply go to file > New Project.

![create project](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/create_project_000.png)

Input the project's name and give it a location to be stored, then hit create project. A project folder will then be
created with a few folders. 

```
< Project Name >
└─ source_images
└─ processed_images
└─ debug_images
└─ output
└─ settings.json
```

Source images: Your images to be processed.
Processed images: Counted and marked images.
Debug images: The computer vision images.
output: Where the Excel sheet will be output to.
settings.json: All the UI settings for this project as well as data about the counted images.

# Input image Do's and Dont's
Providing good images to be processed is essentially the most important part of the entire process.
It is essential that the input images are as clear, clean and consistent for the best results. 


The dish is off at an angle, its always best to take the image from directly above, and frame the dish like this.
Try keep the lighting even and consistent without any bright spots.

![do_dont](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/do_dont_000.png)


# Workflow
1. Take a test picture of a dish
2. Create a new project and place the test image into the source images
3. Tweak the settings until desired result.
4. Re-take the test picture and refine if needed.
5. Once you are happy with the results, take all the pictures needed and load them into the source images.
6. Process the images, this might take a while. 
7. Go through the images once processed and correct any miss counts.
8. Export data to Excel.


# Shortcuts
| Shortcut            | Key              |
|---------------------|------------------|
| Save Project        | Ctrl + S         |
| Open Project        | Ctrl + O         |
| New Project         | Ctrl + N         |
| Export to Excel     | Ctrl + E         |
| Open Project Folder | Ctrl + P         |
| Help                | Ctrl + H         |
| Process images      | Ctrl + Shift + P |
| Prev                | Left Arrow       |
| Next                | Right Arrow      |
| Count Increase      | Up Arrow         |
| Count Decrease      | Down Arrow       |
