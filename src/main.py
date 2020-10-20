import re
import os
import sys
from pprint import pprint
import subprocess

from functools import partial

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

import src.core as core
import src.ui_utilities as ui_utilities
import src.ui.create_project_window as create_project_window

from src.ui import main_window
from src import project

__version__ = '1.2.0'


class PhotoViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.pixel_map = None
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(44, 44, 44)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setVerticalStretch(1)
        self.setSizePolicy(size_policy)

    def hasPhoto(self):
        """
        If the current photo viewer has a photo.
        """
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())

        if not rect.isNull():
            self.setSceneRect(rect)

            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixel_map=None):
        self._zoom = 0
        if pixel_map and not pixel_map.isNull():
            self._empty = False
            self.pixel_map = pixel_map
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixel_map)
        else:
            self._empty = True
            self.pixel_map = None
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.delta() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        """
        Toggle the ability to drag on the image.
        """
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def setMinMaxFromImage(self, desired_width=500):
        """
        Helper function to set the min and max height of a widget using its own image.
        :param int desired_width: The end width for the object.
        """
        if self.pixel_map:
            scale_factor = self.pixel_map.height() / desired_width

            if scale_factor != 0:
                # This ensures the image's scale in the UI is always the same.
                # self.setMaximumHeight((self.pixel_map.height() / scale_factor) + 30000)
                # self.setMaximumWidth((self.pixel_map.width() / scale_factor) + 30000)
                self.setMaximumHeight(self.parent().height())
                self.setMaximumWidth(self.parent().width())

                # self.setMinimumHeight(self.pixel_map.height() / scale_factor)
                self.setMinimumHeight(self.parent().height() * 0.85)
                self.setMinimumWidth(self.pixel_map.width() / scale_factor)

                self.fitInView()


# noinspection PyAttributeOutsideInit
class SpreadCountUI(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(SpreadCountUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'Spread Counter -- v{__version__}')

        # Create a project instance and set it
        self.project = project.Project()
        self.current_image_index = 0

        self.no_image_path = ui_utilities.get_resource_path(os.path.join(os.path.dirname(__file__),
                                                                         'icons',
                                                                         'no_image.png'))

        # The popup windows are stored so that Python's cleaner doesn't immediately kill them.
        self.popup = None

        # Creating the custom photo viewer widgets
        self.count_viewer = PhotoViewer(self)
        self.debug_viewer = PhotoViewer(self)
        self.count_viewer.setVisible(False)
        self.debug_viewer.setVisible(False)

        # Adding the custom widgets to the ui.
        self.picture_view_hb.addWidget(self.count_viewer)
        self.picture_view_hb.addWidget(self.debug_viewer)

        # UI Setup
        self.update_ui_settings()
        self.create_shortcuts()
        self.create_connections()
        self.style()
        self.display_current()
        self.processing_progress_bar.setVisible(False)
        self.show()

        # TEMP TESTING
        test_folder = r'C:\Users\Justi\OneDrive\Documents\Projects\Python\SpreadCounter\tests\_test_projects\mobile'
        self.open_project(folder=test_folder)

    def closeEvent(self, event):
        """
        Check That the user has saved the project, if not ask to save it.
        :param event: Close event
        """
        if self.project.root:
            project_saved = self.project.check_project_saved()

            if project_saved:
                # The project is already saved, closed the window.
                event.accept()
            else:
                # The project is not saved, ask the user what they want to do.
                result = ui_utilities.question_box(self,
                                                   'Would you like to save before quitting?',
                                                   'Close Spread Counter')

                if result == 0:
                    # Save project and exit
                    self.save_project()
                    event.accept()

                if result == 1:
                    # Close without saving
                    event.accept()

                if result == 2:
                    # Cancel and don't close
                    event.ignore()

        else:
            # The project hasn't been created, just close the UI.
            event.accept()

    def resizeEvent(self, event):
        self.count_viewer.setMinMaxFromImage()
        self.debug_viewer.setMinMaxFromImage()
        super().resizeEvent(event)

    def create_shortcuts(self):
        """
        Create all the shortcuts needed for the application.
        """
        self.up_arrow_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("up"), self)
        self.down_arrow_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("down"), self)
        self.frame_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("f"), self)

    def create_connections(self):
        """
        Create connections between all the widgets and methods.
        """
        # Actions
        self.action_how_it_works.triggered.connect(self.help)
        self.action_save_project.triggered.connect(self.save_project)
        self.action_open_project.triggered.connect(self.open_project)
        self.action_create_project.triggered.connect(self.create_project_window)
        self.action_export_to_exl.triggered.connect(self.export_to_exl)
        self.action_debug_mode.changed.connect(self.display_current)
        self.action_open_project_folder.triggered.connect(self.open_current_project_folder)

        # Buttons
        self.process_images_btn.clicked.connect(partial(self.process_images))
        self.next_btn.clicked.connect(partial(self.update_current_image, 1))
        self.prev_btn.clicked.connect(partial(self.update_current_image, -1))
        self.count_offset_sb.valueChanged.connect(self.update_actual_count)

        # Combo Boxes
        self.thresholding_cb.currentIndexChanged.connect(partial(self.disable_thresholds, self.thresholding_cb))

        # shortcuts
        self.up_arrow_shortcut.activated.connect(partial(self.update_count_spin_box, 1))
        self.down_arrow_shortcut.activated.connect(partial(self.update_count_spin_box, -1))
        self.frame_shortcut.activated.connect(partial(self.count_viewer.fitInView))
        self.frame_shortcut.activated.connect(partial(self.debug_viewer.fitInView))

        # Ui updates
        for check_box in self.findChildren(QtWidgets.QCheckBox):
            check_box.stateChanged.connect(self.update_ui_settings)

        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            spin_box.valueChanged.connect(self.update_ui_settings)

        for double_spin_box in self.findChildren(QtWidgets.QDoubleSpinBox):
            double_spin_box.valueChanged.connect(self.update_ui_settings)

        for combo_box in self.findChildren(QtWidgets.QComboBox):
            combo_box.currentIndexChanged.connect(self.update_ui_settings)

        for group_box in self.findChildren(QtWidgets.QGroupBox):
            if group_box.isCheckable():
                group_box.toggled.connect(self.update_ui_settings)

    def disable_thresholds(self, combo_box, *args):
        """
        If the user sets the thresholding mode to None, disable the
        thresholding boxes for a better UX.
        """
        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            if 'thresh' in spin_box.objectName():
                if combo_box.currentIndex() == 2:
                    spin_box.setEnabled(False)
                else:
                    spin_box.setEnabled(True)

    def update_ui_settings(self):
        """
        Update the internal ui dict settings with those present in the UI.
        """
        ui_settings = {}

        for check_box in self.findChildren(QtWidgets.QCheckBox):
            ui_settings.update({check_box.objectName(): check_box.isChecked()})

        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            ui_settings.update({spin_box.objectName(): spin_box.value()})

        for double_spin_box in self.findChildren(QtWidgets.QDoubleSpinBox):
            ui_settings.update({double_spin_box.objectName(): double_spin_box.value()})

        for combo_box in self.findChildren(QtWidgets.QComboBox):
            ui_settings.update({combo_box.objectName(): combo_box.currentIndex()})

        for group_box in self.findChildren(QtWidgets.QGroupBox):
            if group_box.isCheckable():
                ui_settings.update({group_box.objectName(): group_box.isChecked()})

        self.project.ui_settings = ui_settings

    def set_ui_settings(self):
        """
        Set the current state of the UI settings from the self.project.
        """
        for check_box in self.findChildren(QtWidgets.QCheckBox):
            if check_box.objectName() in self.project.ui_settings:
                check_box.setChecked(self.project.ui_settings[check_box.objectName()])

        for double_spin_box in self.findChildren(QtWidgets.QDoubleSpinBox):
            if double_spin_box.objectName() in self.project.ui_settings:
                double_spin_box.setValue(self.project.ui_settings[double_spin_box.objectName()])

        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            if spin_box.objectName() in self.project.ui_settings:
                spin_box.setValue(self.project.ui_settings[spin_box.objectName()])

        for combo_box in self.findChildren(QtWidgets.QComboBox):
            if combo_box.objectName() in self.project.ui_settings:
                combo_box.setCurrentIndex(self.project.ui_settings[combo_box.objectName()])

        for group_box in self.findChildren(QtWidgets.QGroupBox):
            if group_box.objectName() in self.project.ui_settings:
                group_box.setChecked(self.project.ui_settings[group_box.objectName()])

    def update_project_label(self):
        """
        Update the project label to reflect the current project.
        """
        self.project_label.setText(f'Project : {self.project.name}')

    def update_image_label(self):
        """
        Update the image label to let the user know what image they are currently looking at
        """
        if self.project.counts:
            image = self.project.get_count_image_name(self.current_image_index)
            self.image_label.setText(f'Image: {image}')
        else:
            self.image_label.setText('Image: ')

    def update_preview_title(self):
        """
        Update the preview number, so the user can see what number image they are on.
        """
        if self.project.counts:
            self.preview_gb.setTitle(re.sub(r'\((\d+)\/(\d+)\)\:$',
                                            r'({}/{}):'.format(self.current_image_index + 1,
                                                               len(self.project.counts)),
                                            self.preview_gb.title()))
        else:
            self.preview_gb.setTitle('Preview (0/0):')

    def update_count_text(self):
        if self.current_image_index in self.project.counts:
            actual_count = self.project.get_total_count(self.current_image_index)

            self.count_label.setText(re.sub(r': (\d+)$',
                                            r': {}'.format(actual_count),
                                            self.count_label.text()))
        else:
            self.count_label.setText('Count: 0')

    def update_actual_count(self):
        """
        When the user updates the actual count, update the current image's count offset.
        """
        if self.current_image_index in self.project.counts:
            self.project.counts[self.current_image_index]['count_offset'] = self.count_offset_sb.value()
            self.update_count_text()

    def update_count_spin_box(self, value=None):
        """
        When a new image is loaded, set its count offset in the ui.

        :param int value: The value to add or subtract from the current count offset.
        """
        if self.project.counts:
            if value:
                # If a value is given, set the delta + update the project dict
                self.count_offset_sb.setValue(self.count_offset_sb.value() + value)

            else:
                # IF not, use the self.project value
                self.count_offset_sb.setValue(self.project.counts[self.current_image_index]['count_offset'])

        else:
            self.count_offset_sb.setValue(0)

    def update_ui_state(self):
        """
        Helper function to call all the necessary UI updates at once.
        """
        self.display_current()
        self.update_project_label()
        self.update_preview_title()
        self.update_count_text()
        self.update_count_spin_box()
        self.update_image_label()

        # Update the image viewers
        self.count_viewer.fitInView()
        self.debug_viewer.fitInView()

    def process_images(self):
        """
        Take in all the settings from the UI. Iterate over all the source images and count them.
        Then present the counted images to the user for checking.
        """
        ui_settings = self.project.ui_settings

        if self.project.source_images:
            images_to_process = self.project.get_valid_images()

            if images_to_process:
                # Un-hide the progress bar
                self.processing_progress_bar.setVisible(True)

                for i, image in enumerate(images_to_process):
                    image_path = self.project.get_relative_image_path(image, 0)
                    process_path = self.project.get_relative_image_path(image, 1)

                    debug_path = None
                    if self.action_debug_mode.isChecked():
                        debug_path = self.project.get_relative_image_path(image, 2)

                    result = core.find_circles_in_dish(image_path=image_path,
                                                       write_path=process_path,
                                                       debug_path=debug_path,
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

                    image_dict = {'count': result['count'],
                                  'count_offset': 0,
                                  'input_image': image}

                    self.project.counts[i] = image_dict
                    pprint(self.project.counts[i])

                    self.processing_progress_bar.setValue((i + 1) / len(images_to_process) * 100)

                # Update the UI State
                self.update_ui_state()

                # Hide the progress bar
                self.processing_progress_bar.setVisible(False)

                # Save the scene so no data is lost
                self.save_project()

            else:
                self.no_source_images_window()
        else:
            self.no_project_created_window()

    def show_image(self, image_path, debug_path=None):
        """
        Given an image path, display it on the Preview Image Label.
        :param str image_path: Path to the image to be displayed.
        :param str debug_path: If present will show the debug image.
        """
        image = QtGui.QImage(image_path)
        self.count_viewer.setPhoto(QtGui.QPixmap.fromImage(image))
        self.count_viewer.setMinMaxFromImage()
        self.count_viewer.setVisible(True)

        if debug_path:
            debug_image = QtGui.QImage(debug_path)
            self.debug_viewer.setPhoto(QtGui.QPixmap.fromImage(debug_image))
            self.debug_viewer.setMinMaxFromImage()
            self.debug_viewer.setVisible(True)
        else:
            self.debug_viewer.setVisible(False)

    def display_current(self):
        debug_path = None

        if self.project.counts:
            # Hide the missing image label
            self.missing_image_label.setVisible(False)

            # If we are in debug mode, add the debug path.
            if self.action_debug_mode.isChecked():
                debug_path = self.project.get_count_debug_path(self.current_image_index)

            image_path = self.project.get_count_process_path(self.current_image_index)

            self.show_image(image_path=image_path,
                            debug_path=debug_path)

        else:
            # Display the No image png
            self.missing_image_label.setVisible(True)
            self.missing_image_label.setPixmap(self.no_image_path)

            # Hide the image viewers since there are no counts for this project
            self.count_viewer.setVisible(False)
            self.debug_viewer.setVisible(False)

    def update_current_image(self, value):
        if self.project.processed_images:
            if self.current_image_index + value >= len(self.project.counts):
                self.current_image_index = 0

            elif self.current_image_index + value == -1:
                self.current_image_index = len(self.project.counts) - 1
            else:
                self.current_image_index += value

            self.update_ui_state()

    def save_project(self):
        """
        Save out the current self.project to a json.
        """
        self.project.save_project()

    def open_project(self, folder=None):
        """
        Open up a previously saved project and read in its settings.
        :param str folder: Folder can be passed in for quicker debugging.
        """

        if not folder:
            folder = QtWidgets.QFileDialog.getExistingDirectory()

        if folder:
            self.project.open_project(folder)
            self.set_ui_settings()
            self.update_ui_settings()
            self.update_ui_state()

            self.project.print_data()

        else:
            # No json with settings or source images folder found. This is not a project.
            self.popup = ui_utilities.pop_up_window('The selected folder is not a valid project.')

    def create_project_window(self):
        """
        Open the create project window.
        """
        project_saved = self.project.check_project_saved()

        if not project_saved:
            message = 'Your current project is not saved.\n' \
                      'Would you like to save before creating\n' \
                      'a new project? '

            flags = QtWidgets.QMessageBox.Yes
            flags |= QtWidgets.QMessageBox.No

            save_project = ui_utilities.question_box(parent=self,
                                                     message=message,
                                                     title='Spread Counter',
                                                     flags=flags) == 0
            if save_project:
                self.save_project()

        self.create_project_window = create_project_window.CreateProjectUI(self)

    def export_to_exl(self):
        """
        Export the current session data to exel
        """
        if self.project.counts:
            workbook, sheet = core.generate_spreadsheet()

            for i, count in enumerate(self.project.counts):
                sheet.write(i + 1, 0, os.path.basename(self.project.counts[count]['input_path']))
                sheet.write(i + 1, 1, self.project.counts[count]['count'])
                sheet.write(i + 1, 2, self.project.counts[count]['count_offset'])

            workbook.save(self.project.excel_output)

            self.popup = ui_utilities.pop_up_window('Successfully Saved out counts.\n'
                                                    'Please check project output folder.')

    def open_current_project_folder(self):
        """
        Open the current project folder.
        """
        if self.project.root:
            subprocess.Popen(r'explorer "{}"'.format(self.project.root.replace('/', os.sep)))

    def no_source_images_window(self):
        """
        When there are no source images present, instruct the user of the issue and
        offer an option to open the source images folder.
        """
        message = 'You need to copy the images to be processed into \n' \
                  'this project\'s source_images folder.\n\n' \
                  'Would you like to open that folder now?'

        flags = QtWidgets.QMessageBox.Yes
        flags |= QtWidgets.QMessageBox.No

        response = ui_utilities.question_box(parent=self, message=message, title='Spread Counter', flags=flags)

        if response == 0:
            if self.project.root:
                subprocess.Popen(r'explorer "{}"'.format(self.project.source_images.replace('/', os.sep)))

    def no_project_created_window(self):
        """
        IF there is currently no project created, inform the user of this and
        offer an option to open the create folder dialog.

        """
        message = 'You need to open a project or create a new project and then copy \n' \
                  'the images to be processed into that project\'s "source_images" folder.\n\n' \
                  'Would you like to create a project now?'

        flags = QtWidgets.QMessageBox.Yes
        flags |= QtWidgets.QMessageBox.No

        response = ui_utilities.question_box(parent=self, message=message, title='Spread Counter', flags=flags)

        if response == 0:
            self.create_project_window()

    def help(self):
        """
        Open up a popup window with some text about how the program works.
        """
        # TODO: Add a link to the git repo here.

        help_message = "This application uses OpenCV, a Python based computer vision\n" \
                       "framework to detect a Petri dish within an image, then search for\n" \
                       "dots within it. Those dots are then counted and presented back.\n" \
                       "This method is by no means perfect and there will always be miss\n" \
                       "counts that occur.\n\n" \
                       "It is always important to remember that good images will produce better\n" \
                       "results than poor ones."
        self.popup = ui_utilities.pop_up_window(help_message)


def run_application():
    """
    Run the app.
    """
    app = QtWidgets.QApplication(sys.argv)
    ui_utilities.set_style(app)
    mainWin = SpreadCountUI()
    ret = app.exec_()
    sys.exit()


if __name__ == '__main__':
    # Compile the UI files for easier dev.
    if not hasattr(sys, '_MEIPASS'):
        ui_utilities.compile_ui_files()

    run_application()
