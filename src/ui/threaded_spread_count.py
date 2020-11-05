"""
Multi threading widgets for the spread counter
"""

import os
from PySide2 import QtCore
from src import core


class ResultObj(QtCore.QObject):
    def __init__(self, val):
        super().__init__()
        self.val = val


class ThreadedSpreadCount(QtCore.QThread):
    finished = QtCore.Signal(object)

    def __init__(self, queue, callback, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.queue = queue
        self.finished.connect(callback)

    def run(self):
        while True:
            arg = self.queue.get()
            if arg is None:
                # Shut down the thread.
                return

            self.process_image(arg)

    def process_image(self, args):
        """
        Process the image given its paths in the args.

        :param list args: Ordered arguments with the settings to process the images:
                          [0] str - image path
                          [1] str - write path
                          [2] str - debug path
                          [3] dict - ui settings
        :return:
        """
        ui_settings = args[3]
        count_result = core.find_circles_in_dish(image_path=args[0],
                                                 write_path=args[1],
                                                 debug_path=args[2],
                                                 dish_detection=ui_settings['dish_detection_gb'],
                                                 thresholding_type=ui_settings['thresholding_cb'],
                                                 max_threshold=ui_settings['upper_thresh_sb'],
                                                 min_threshold=ui_settings['lower_thresh_sb'],
                                                 contrast_multiplier=ui_settings['contrast_multiplier_sb'],
                                                 scale_factor=ui_settings['image_scale_factor_sb'],
                                                 mask_offset=ui_settings['dish_offset_sb'],
                                                 max_dish_radius_offset=ui_settings['dish_offset_sb'],
                                                 min_dish_radius_offset=ui_settings['min_dish_offset_radius_sb'],
                                                 circle_min_dist=ui_settings['circle_min_dist_sb'],
                                                 circle_min_rad=ui_settings['circle_min_rad_sb'],
                                                 circle_max_rad=ui_settings['circle_max_rad_sb'],
                                                 draw_dish_circle=ui_settings['draw_dish_circles_cb'],
                                                 draw_circle=ui_settings['draw_circles_cb'],
                                                 draw_center=ui_settings['draw_centers_cb'],
                                                 draw_count=ui_settings['draw_count_cb'])

        # Compile the results into a neat dict that will fit into the self.project.counts
        result = {args[4]: {'count': count_result['count'],
                            'count_offset': 0,
                            'input_image': os.path.basename(args[0])}}

        self.finished.emit(ResultObj(result))
