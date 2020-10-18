import os

from PySide2 import QtWidgets

from src.ui import project_window
import src.ui_utilities as ui_utilities


class CreateProjectUI(QtWidgets.QMainWindow, project_window.Ui_MainWindow):
    def __init__(self, parent):
        self.parent = parent
        super(CreateProjectUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Create Project')
        # The popup windows are stored so that Python's cleaner doesn't immediately kill them.
        self.popup = None
        self.create_connections()
        self.show()

    def create_connections(self):
        self.file_browser_btn.clicked.connect(self.create_project_location)
        self.create_project_btn.clicked.connect(self.create_project)

    def create_project(self):
        """
        Create a new project at the location given.
        Then update the parent UI's model and project Label.
        """
        project_name = self.project_name_line.text()
        location = self.location_line.text()

        if project_name and location and os.path.isdir(location):
            result = ui_utilities.create_project(project_name=project_name,
                                                 location_path=location)
            self.parent.project.update(result)
            self.parent.update_ui_state()
            self.close()

    def create_project_location(self):
        """
        Get the location of a new project
        """
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        if folder:
            sub_folders = os.listdir(folder)
            if 'settings.json' in sub_folders or 'source_images' in sub_folders:
                self.popup = ui_utilities.pop_up_window('That is not a valid project location.\n'
                                                        'There might be another project there already.')
            else:
                self.location_line.setText(folder)
