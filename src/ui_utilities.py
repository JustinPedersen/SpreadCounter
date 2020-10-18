import os
import sys
import json
import subprocess

from PySide2 import QtGui
from PySide2 import QtWidgets


def get_resource_path(relative_path):
    """
    Get the absolute path to a given resource.
    :param str relative_path: Relative path to be converted
    :return: The absolute path, either to the temp folder or project folder.
    :rtype str
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def read_project_json(folder):
    """
    Helper function to read in the current project's settings json.
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


def get_valid_images(image_path, full_path=True):
    """
    Given a path collect and return all the valid image types for processing.
    :param str image_path: Path to the images to collect.
    :param bool full_path: If True will return the full paths.
    :return: List of all the connected images.
    :rtype: list[str]
    """
    collected_images = []
    for file in os.listdir(image_path):
        if file.endswith('.png') or file.endswith('.jpg'):
            # Append the collected image with a full path or not depending on settings.
            collected_images.append(os.path.join(image_path, file)) if full_path else collected_images.append(file)

    return collected_images


def create_project(project_name, location_path):
    """
    Create the folders required for a new project. If the location is valid and no project with that
    name exists a new one will be made. Once that is complete the internal folders will be created.
    If they are already present they are skipped.

    :param str project_name: Name of the new project,
    :param str location_path: Path to where the new project will sit.
    :return: Dict of all the newly created folders.
    :rtype: dict
    """
    project_dir = os.path.join(location_path, project_name)
    dirs = [os.path.join(project_dir, x) for x in ['source_images', 'processed_images', 'debug_images', 'output']]

    # Only create the project if location is valid and project doesn't already exist.
    if os.path.isdir(location_path) and not os.path.exists(project_dir):
        os.mkdir(project_dir)

    for directory in dirs:
        if not os.path.exists(directory):
            os.mkdir(directory)

    result_dict = {os.path.basename(directory): directory for directory in dirs}
    result_dict.update({'root': project_dir,
                        'counts': {}})
    return result_dict


def pop_up_window(message):
    """
    Display a window with a warning for the user.
    :param str message: The message to display.
    :return: the generated message box.
    :rtype: object
    """
    message_box = QtWidgets.QMessageBox()
    message_box.setText(message)
    message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    message_box.show()

    return message_box


def question_box(parent, message, title, flags=None):
    """
    Open up a yes or no dialog and return the result.
    :param parent: The Parent UI.
    :param str message: The message to display.
    :param str title: The window title.
    :param list flags: Custom button flags to use.
    """
    if not flags:
        flags = QtWidgets.QMessageBox.Yes
        flags |= QtWidgets.QMessageBox.No
        flags |= QtWidgets.QMessageBox.Cancel

    # Capture the response
    response = QtWidgets.QMessageBox.question(parent,
                                              title,
                                              message,
                                              flags)

    if response == QtWidgets.QMessageBox.Yes:
        return 0
    elif response == QtWidgets.QMessageBox.No:
        return 1
    else:
        return 2


def set_style(app):
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))

    dark_theme = QtGui.QPalette()
    dark_theme.setColor(QtGui.QPalette.Window, QtGui.QColor(45, 45, 45))
    dark_theme.setColor(QtGui.QPalette.WindowText, QtGui.QColor(222, 222, 222))
    dark_theme.setColor(QtGui.QPalette.Button, QtGui.QColor(60, 60, 60))
    dark_theme.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(222, 222, 222))
    dark_theme.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(222, 222, 222))
    dark_theme.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(222, 222, 222))
    dark_theme.setColor(QtGui.QPalette.Highlight, QtGui.QColor(134, 156, 158))
    dark_theme.setColor(QtGui.QPalette.Base, QtGui.QColor(200, 200, 200))
    # Define the pallet color
    # Then set the pallet color
    app.setPalette(dark_theme)


def compile_ui_files():
    """
    Helper function to compile the .ui files quickly and easily.
    :return:
    """
    bat_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'compile', 'compile_ui_files.bat')
    subprocess.call([bat_path])
