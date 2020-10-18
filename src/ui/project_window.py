# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 160)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.location_line = QLineEdit(self.centralwidget)
        self.location_line.setObjectName(u"location_line")

        self.gridLayout.addWidget(self.location_line, 2, 1, 1, 2)

        self.file_browser_btn = QPushButton(self.centralwidget)
        self.file_browser_btn.setObjectName(u"file_browser_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_browser_btn.sizePolicy().hasHeightForWidth())
        self.file_browser_btn.setSizePolicy(sizePolicy)
        self.file_browser_btn.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.file_browser_btn, 2, 3, 1, 1)

        self.project_name_line = QLineEdit(self.centralwidget)
        self.project_name_line.setObjectName(u"project_name_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.project_name_line.sizePolicy().hasHeightForWidth())
        self.project_name_line.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.project_name_line, 0, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.create_project_btn = QPushButton(self.centralwidget)
        self.create_project_btn.setObjectName(u"create_project_btn")
        self.create_project_btn.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.create_project_btn, 3, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.project_name_line, self.location_line)
        QWidget.setTabOrder(self.location_line, self.file_browser_btn)
        QWidget.setTabOrder(self.file_browser_btn, self.create_project_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Project Name: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Location: ", None))
        self.file_browser_btn.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.create_project_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

