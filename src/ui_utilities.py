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
