import os
import json
from pprint import pprint


class Project:
    def __init__(self):
        self.settings_json = 'settings.json'
        self._project = {'root': None,
                         'counts': {},
                         'ui_settings': {}}

    @classmethod
    def read_project_json(cls, folder):
        """
        Helper function to read in the settings json.
        :return: Dict of the data from settings.json
        :rtype: dict
        """
        project_settings_json = os.path.join(folder, 'settings.json')

        if not os.path.isfile(project_settings_json):
            return {}

        with open(project_settings_json) as f:
            data = json.load(f)

        # The int keys need to be changed back as json brings them in as strings
        res = False
        while not res:
            for key in data['counts']:
                if type(key) == str:
                    data['counts'][int(key)] = data['counts'][key]
                    del data['counts'][key]
            res = all(isinstance(sub, int) for sub in data['counts'])

        return data

    def is_project_folder(self, folder):
        """
        :param str folder: Location to the folder
        :return: If a given folder is a valid project.
        :rtype: bool
        """
        expected_list = [self.settings_json, 'source_images', 'debug_images', 'processed_images']

        sub_folders = os.listdir(folder)
        for x in sub_folders:
            if x in expected_list:
                return True

        return False

    def open_project(self, folder):
        """
        Open up a previously saved project and read in its settings.
        :param str folder: Folder where the setting.json is located.
        """
        sub_folders = os.listdir(folder)

        if self.is_project_folder(folder):
            if self.settings_json in sub_folders:

                # If the settings file is found, load it in.
                self._project.update(self.read_project_json(folder))

            else:
                # If it's a project but there isn't a setting file, make due with what is there.
                self._project = {'root': None,
                                 'counts': {},
                                 'ui_settings': {}}

                self.create_project(project_name=os.path.basename(folder),
                                    location_path=os.path.dirname(folder))

    def save_project(self):
        """
        Save out the current self._project to a json.
        """
        if self.root:
            settings_file_path = os.path.join(self.root, 'settings.json')
            with open(settings_file_path, 'w') as outfile:
                json.dump(self._project, outfile)

            print(f'Project Saved to {settings_file_path}')

    def create_project(self, project_name, location_path):
        """
        Create the folders required for a new project. If the location is valid and no project with that
        name exists a new one will be made. Once that is complete the internal folders will be created.
        If they are already present they are skipped.

        :param str project_name: Name of the new project,
        :param str location_path: Path to where the new project will sit.
        :return: Dict of all the newly created folders.
        :rtype: dict
        """
        project_dir = os.path.normpath(os.path.join(location_path, project_name))
        dirs = [os.path.join(project_dir, x) for x in ['source_images', 'processed_images', 'debug_images', 'output']]

        # Only create the project if location is valid and project doesn't already exist.
        if os.path.isdir(location_path) and not os.path.exists(project_dir):
            os.mkdir(project_dir)

        for directory in dirs:
            if not os.path.exists(directory):
                os.mkdir(directory)

        self.root = project_dir

    def check_project_saved(self):
        """
        Make sure the current session is saved by comparing the self.project with the settings.json.
        """
        return self.read_project_json(self.root) == self._project if self.root else False

    @property
    def root(self):
        """
        :return: The root directory of the project.
        :rtype: str
        """
        return os.path.normpath(self._project['root']) if self._project['root'] else None

    @root.setter
    def root(self, folder):
        """
        :param str folder: The base folder for the project
        """
        self._project['root'] = folder

    @property
    def source_images(self):
        """
        :return: The source images folder for the current project.
        :rtype: str
        """
        return os.path.join(self.root, 'source_images') if self._project['root'] else None

    @property
    def processed_images(self):
        """
        :return: The processed image folder for the current project.
        :rtype: str
        """
        return os.path.join(self.root, 'processed_images') if self._project['root'] else None

    @property
    def debug_images(self):
        """
        :return: The debug image folder for the current project.
        :rtype: str
        """
        return os.path.join(self.root, 'debug_images') if self._project['root'] else None

    @property
    def output(self):
        """
        :return: The output image folder for the current project.
        :rtype: str
        """
        return os.path.join(self.root, 'output') if self._project['root'] else None

    @property
    def excel_output(self):
        """
        :return: The path where excel sheets are to be output.
        :rtype: str
        """
        return os.path.join(self.output, '_results.xls') if self._project['root'] else None

    @property
    def ui_settings(self):
        """
        :return: UI settings for the current project
        :rtype: dict
        """
        return self._project['ui_settings']

    @ui_settings.setter
    def ui_settings(self, settings):
        """
        :param dict settings: The new UI settings to use.
        """
        self._project['ui_settings'].update(settings)

    @property
    def counts(self):
        """
        :return: UI settings for the current project
        :rtype: dict
        """
        return self._project['counts']

    @counts.setter
    def counts(self, data):
        """
        :param dict data: The new UI settings to use.
        """
        pprint(data)
        self._project['counts'].update(data)

    @property
    def name(self):
        """
        :return: Name of the current project
        :rtype: str
        """
        return os.path.basename(self.root)

    def get_count_debug_path(self, index):
        """
        :return: The debug path for a given index in the count dict
        :rtype: str
        """
        return self.counts[index]['debug_path'] if index in self.counts else ''

    def get_count_process_path(self, index):
        """
        :return: The process path for a given index in the count dict
        :rtype: str
        """
        return self.counts[index]['processed_path'] if index in self.counts else ''

    def print_data(self):
        """
        pint Internal _project for debugging only.
        """
        pprint(self._project)
