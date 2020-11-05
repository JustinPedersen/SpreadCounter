# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(755, 683)
        self.action_open_github_page = QAction(MainWindow)
        self.action_open_github_page.setObjectName(u"action_open_github_page")
        self.action_create_project = QAction(MainWindow)
        self.action_create_project.setObjectName(u"action_create_project")
        self.action_open_project = QAction(MainWindow)
        self.action_open_project.setObjectName(u"action_open_project")
        self.action_export_to_exl = QAction(MainWindow)
        self.action_export_to_exl.setObjectName(u"action_export_to_exl")
        self.action_save_project = QAction(MainWindow)
        self.action_save_project.setObjectName(u"action_save_project")
        self.action_debug_mode = QAction(MainWindow)
        self.action_debug_mode.setObjectName(u"action_debug_mode")
        self.action_debug_mode.setCheckable(True)
        self.action_debug_mode.setChecked(True)
        self.action_open_project_folder = QAction(MainWindow)
        self.action_open_project_folder.setObjectName(u"action_open_project_folder")
        self.action_connect_views = QAction(MainWindow)
        self.action_connect_views.setObjectName(u"action_connect_views")
        self.action_connect_views.setCheckable(True)
        self.action_connect_views.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.process_images_btn = QPushButton(self.centralwidget)
        self.process_images_btn.setObjectName(u"process_images_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_images_btn.sizePolicy().hasHeightForWidth())
        self.process_images_btn.setSizePolicy(sizePolicy)
        self.process_images_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.process_images_btn)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")

        self.horizontalLayout_10.addWidget(self.image_label)

        self.project_label = QLabel(self.centralwidget)
        self.project_label.setObjectName(u"project_label")
        self.project_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.project_label)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.preview_gb = QGroupBox(self.centralwidget)
        self.preview_gb.setObjectName(u"preview_gb")
        self.verticalLayout_4 = QVBoxLayout(self.preview_gb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.top_vertical_spacer)

        self.picture_view_hb = QHBoxLayout()
        self.picture_view_hb.setObjectName(u"picture_view_hb")
        self.missing_image_label = QLabel(self.preview_gb)
        self.missing_image_label.setObjectName(u"missing_image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.missing_image_label.sizePolicy().hasHeightForWidth())
        self.missing_image_label.setSizePolicy(sizePolicy1)
        self.missing_image_label.setMinimumSize(QSize(0, 0))
        self.missing_image_label.setMaximumSize(QSize(300, 300))
        self.missing_image_label.setScaledContents(False)
        self.missing_image_label.setAlignment(Qt.AlignCenter)

        self.picture_view_hb.addWidget(self.missing_image_label)


        self.verticalLayout_4.addLayout(self.picture_view_hb)

        self.bot_vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.bot_vertical_spacer)


        self.verticalLayout.addWidget(self.preview_gb)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prev_btn = QPushButton(self.centralwidget)
        self.prev_btn.setObjectName(u"prev_btn")

        self.horizontalLayout_5.addWidget(self.prev_btn)

        self.next_btn = QPushButton(self.centralwidget)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout_5.addWidget(self.next_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.count_offset_label = QLabel(self.centralwidget)
        self.count_offset_label.setObjectName(u"count_offset_label")

        self.horizontalLayout_6.addWidget(self.count_offset_label)

        self.count_offset_sb = QSpinBox(self.centralwidget)
        self.count_offset_sb.setObjectName(u"count_offset_sb")
        self.count_offset_sb.setMinimum(-100)
        self.count_offset_sb.setMaximum(100)

        self.horizontalLayout_6.addWidget(self.count_offset_sb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.count_label = QLabel(self.centralwidget)
        self.count_label.setObjectName(u"count_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.count_label)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image_process_settings_gb = QGroupBox(self.centralwidget)
        self.image_process_settings_gb.setObjectName(u"image_process_settings_gb")
        self.verticalLayout_6 = QVBoxLayout(self.image_process_settings_gb)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.image_process_settings_gb)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.image_scale_factor_sb = QDoubleSpinBox(self.image_process_settings_gb)
        self.image_scale_factor_sb.setObjectName(u"image_scale_factor_sb")
        self.image_scale_factor_sb.setFrame(False)
        self.image_scale_factor_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.image_scale_factor_sb.setSingleStep(0.050000000000000)
        self.image_scale_factor_sb.setValue(0.200000000000000)

        self.horizontalLayout_12.addWidget(self.image_scale_factor_sb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.image_process_settings_gb)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_16.addWidget(self.label_11)

        self.contrast_multiplier_sb = QDoubleSpinBox(self.image_process_settings_gb)
        self.contrast_multiplier_sb.setObjectName(u"contrast_multiplier_sb")
        self.contrast_multiplier_sb.setFrame(False)
        self.contrast_multiplier_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.contrast_multiplier_sb.setMaximum(100.000000000000000)
        self.contrast_multiplier_sb.setSingleStep(0.050000000000000)
        self.contrast_multiplier_sb.setValue(1.200000000000000)

        self.horizontalLayout_16.addWidget(self.contrast_multiplier_sb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.image_process_settings_gb)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.thresholding_cb = QComboBox(self.image_process_settings_gb)
        self.thresholding_cb.addItem("")
        self.thresholding_cb.addItem("")
        self.thresholding_cb.addItem("")
        self.thresholding_cb.setObjectName(u"thresholding_cb")

        self.horizontalLayout_2.addWidget(self.thresholding_cb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.image_process_settings_gb)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.upper_thresh_sb = QSpinBox(self.image_process_settings_gb)
        self.upper_thresh_sb.setObjectName(u"upper_thresh_sb")
        self.upper_thresh_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.upper_thresh_sb.setMinimum(0)
        self.upper_thresh_sb.setMaximum(255)
        self.upper_thresh_sb.setValue(255)

        self.horizontalLayout_14.addWidget(self.upper_thresh_sb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.image_process_settings_gb)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.lower_thresh_sb = QSpinBox(self.image_process_settings_gb)
        self.lower_thresh_sb.setObjectName(u"lower_thresh_sb")
        self.lower_thresh_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lower_thresh_sb.setMinimum(0)
        self.lower_thresh_sb.setMaximum(255)
        self.lower_thresh_sb.setValue(200)

        self.horizontalLayout_15.addWidget(self.lower_thresh_sb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)


        self.verticalLayout_2.addWidget(self.image_process_settings_gb)

        self.dish_detection_gb = QGroupBox(self.centralwidget)
        self.dish_detection_gb.setObjectName(u"dish_detection_gb")
        self.dish_detection_gb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dish_detection_gb.setCheckable(True)
        self.verticalLayout_8 = QVBoxLayout(self.dish_detection_gb)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.dish_detection_gb)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.max_dish_offset_radius_sb = QDoubleSpinBox(self.dish_detection_gb)
        self.max_dish_offset_radius_sb.setObjectName(u"max_dish_offset_radius_sb")
        self.max_dish_offset_radius_sb.setFrame(False)
        self.max_dish_offset_radius_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.max_dish_offset_radius_sb.setSingleStep(0.050000000000000)
        self.max_dish_offset_radius_sb.setValue(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.max_dish_offset_radius_sb)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.dish_detection_gb)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.min_dish_offset_radius_sb = QDoubleSpinBox(self.dish_detection_gb)
        self.min_dish_offset_radius_sb.setObjectName(u"min_dish_offset_radius_sb")
        self.min_dish_offset_radius_sb.setFrame(False)
        self.min_dish_offset_radius_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.min_dish_offset_radius_sb.setSingleStep(0.050000000000000)
        self.min_dish_offset_radius_sb.setValue(0.200000000000000)

        self.horizontalLayout_4.addWidget(self.min_dish_offset_radius_sb)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.dish_detection_gb)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dish_offset_sb = QDoubleSpinBox(self.dish_detection_gb)
        self.dish_offset_sb.setObjectName(u"dish_offset_sb")
        self.dish_offset_sb.setFrame(False)
        self.dish_offset_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dish_offset_sb.setSingleStep(0.050000000000000)
        self.dish_offset_sb.setValue(0.850000000000000)

        self.horizontalLayout.addWidget(self.dish_offset_sb)


        self.verticalLayout_8.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.dish_detection_gb)

        self.circle_detection_gb = QGroupBox(self.centralwidget)
        self.circle_detection_gb.setObjectName(u"circle_detection_gb")
        self.verticalLayout_3 = QVBoxLayout(self.circle_detection_gb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.circle_detection_gb)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.circle_min_dist_sb = QSpinBox(self.circle_detection_gb)
        self.circle_min_dist_sb.setObjectName(u"circle_min_dist_sb")
        self.circle_min_dist_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.circle_min_dist_sb.setMinimum(1)
        self.circle_min_dist_sb.setMaximum(500)
        self.circle_min_dist_sb.setValue(5)

        self.horizontalLayout_7.addWidget(self.circle_min_dist_sb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.circle_detection_gb)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.circle_min_rad_sb = QSpinBox(self.circle_detection_gb)
        self.circle_min_rad_sb.setObjectName(u"circle_min_rad_sb")
        self.circle_min_rad_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.circle_min_rad_sb.setMinimum(1)
        self.circle_min_rad_sb.setMaximum(500)
        self.circle_min_rad_sb.setValue(1)

        self.horizontalLayout_8.addWidget(self.circle_min_rad_sb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.circle_detection_gb)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.circle_max_rad_sb = QSpinBox(self.circle_detection_gb)
        self.circle_max_rad_sb.setObjectName(u"circle_max_rad_sb")
        self.circle_max_rad_sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.circle_max_rad_sb.setMinimum(1)
        self.circle_max_rad_sb.setMaximum(500)
        self.circle_max_rad_sb.setValue(10)

        self.horizontalLayout_9.addWidget(self.circle_max_rad_sb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addWidget(self.circle_detection_gb)

        self.output_draw_settings_gb = QGroupBox(self.centralwidget)
        self.output_draw_settings_gb.setObjectName(u"output_draw_settings_gb")
        self.verticalLayout_5 = QVBoxLayout(self.output_draw_settings_gb)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.draw_centers_cb = QCheckBox(self.output_draw_settings_gb)
        self.draw_centers_cb.setObjectName(u"draw_centers_cb")
        self.draw_centers_cb.setChecked(True)

        self.verticalLayout_5.addWidget(self.draw_centers_cb)

        self.draw_circles_cb = QCheckBox(self.output_draw_settings_gb)
        self.draw_circles_cb.setObjectName(u"draw_circles_cb")
        self.draw_circles_cb.setChecked(True)

        self.verticalLayout_5.addWidget(self.draw_circles_cb)

        self.draw_dish_circles_cb = QCheckBox(self.output_draw_settings_gb)
        self.draw_dish_circles_cb.setObjectName(u"draw_dish_circles_cb")
        self.draw_dish_circles_cb.setChecked(True)

        self.verticalLayout_5.addWidget(self.draw_dish_circles_cb)

        self.draw_count_cb = QCheckBox(self.output_draw_settings_gb)
        self.draw_count_cb.setObjectName(u"draw_count_cb")
        self.draw_count_cb.setEnabled(True)
        self.draw_count_cb.setChecked(False)

        self.verticalLayout_5.addWidget(self.draw_count_cb)


        self.verticalLayout_2.addWidget(self.output_draw_settings_gb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addLayout(self.verticalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.processing_progress_bar = QProgressBar(self.centralwidget)
        self.processing_progress_bar.setObjectName(u"processing_progress_bar")
        self.processing_progress_bar.setEnabled(True)
        self.processing_progress_bar.setValue(24)
        self.processing_progress_bar.setTextVisible(True)

        self.verticalLayout_7.addWidget(self.processing_progress_bar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 755, 21))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_open_github_page)
        self.menuFile.addAction(self.action_save_project)
        self.menuFile.addAction(self.action_open_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_create_project)
        self.menuTools.addAction(self.action_export_to_exl)
        self.menuTools.addAction(self.action_open_project_folder)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_debug_mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open_github_page.setText(QCoreApplication.translate("MainWindow", u"Open Github Page", None))
#if QT_CONFIG(shortcut)
        self.action_open_github_page.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.action_create_project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
#if QT_CONFIG(shortcut)
        self.action_create_project.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open_project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
#if QT_CONFIG(shortcut)
        self.action_open_project.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_export_to_exl.setText(QCoreApplication.translate("MainWindow", u"Export Session to Exl", None))
#if QT_CONFIG(shortcut)
        self.action_export_to_exl.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
#if QT_CONFIG(shortcut)
        self.action_save_project.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_debug_mode.setText(QCoreApplication.translate("MainWindow", u"debug_mode", None))
        self.action_open_project_folder.setText(QCoreApplication.translate("MainWindow", u"Open Project folder", None))
#if QT_CONFIG(shortcut)
        self.action_open_project_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_connect_views.setText(QCoreApplication.translate("MainWindow", u"connect views", None))
        self.process_images_btn.setText(QCoreApplication.translate("MainWindow", u"Process images", None))
#if QT_CONFIG(shortcut)
        self.process_images_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+P", None))
#endif // QT_CONFIG(shortcut)
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"Image: ", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.preview_gb.setTitle(QCoreApplication.translate("MainWindow", u"Preview (0/0):", None))
        self.missing_image_label.setText("")
        self.prev_btn.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
#if QT_CONFIG(shortcut)
        self.prev_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.next_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.count_offset_label.setText(QCoreApplication.translate("MainWindow", u"Count offset", None))
#if QT_CONFIG(tooltip)
        self.count_offset_sb.setToolTip(QCoreApplication.translate("MainWindow", u"If the count on the image is incorrect, offset it here.", None))
#endif // QT_CONFIG(tooltip)
        self.count_label.setText(QCoreApplication.translate("MainWindow", u"Count: 0", None))
        self.image_process_settings_gb.setTitle(QCoreApplication.translate("MainWindow", u"Image processing settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Image Scale Factor", None))
#if QT_CONFIG(tooltip)
        self.image_scale_factor_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The amount to scale the image by. Smaller number will \n"
"result in faster performance. \n"
"If the image is too big the application might freeze up.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Contrast Multiplier", None))
#if QT_CONFIG(tooltip)
        self.contrast_multiplier_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The Amount to shrink the dish search area by. \n"
"This will avoid detecting parts of the rim as \n"
"false positives as well as any dots on the edge of the dish.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.thresholding_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Single", None))
        self.thresholding_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi", None))
        self.thresholding_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Upper Threshold", None))
#if QT_CONFIG(tooltip)
        self.upper_thresh_sb.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lower Threshold", None))
#if QT_CONFIG(tooltip)
        self.lower_thresh_sb.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dish_detection_gb.setToolTip(QCoreApplication.translate("MainWindow", u"If enabled, the dish itself will be detected in the image and masked out. This prevents false positive dots on the surrounding area being counted.", None))
#endif // QT_CONFIG(tooltip)
        self.dish_detection_gb.setTitle(QCoreApplication.translate("MainWindow", u"Dish detection settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max dish offset radius", None))
#if QT_CONFIG(tooltip)
        self.max_dish_offset_radius_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The Max size of the dish relative to the image width and height.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Min dish offset radius", None))
#if QT_CONFIG(tooltip)
        self.min_dish_offset_radius_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The Min size of the dish relative to the image width and height.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dish offset % : ", None))
#if QT_CONFIG(tooltip)
        self.dish_offset_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The Amount to shrink the dish search area by. \n"
"This will avoid detecting parts of the rim as \n"
"false positives as well as any dots on the edge of the dish.", None))
#endif // QT_CONFIG(tooltip)
        self.circle_detection_gb.setTitle(QCoreApplication.translate("MainWindow", u"Circle detection settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Colony Min Dist", None))
#if QT_CONFIG(tooltip)
        self.circle_min_dist_sb.setToolTip(QCoreApplication.translate("MainWindow", u"If there are too many false positives in a \n"
"small area, consider upping this value.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Colony Min Radius", None))
#if QT_CONFIG(tooltip)
        self.circle_min_rad_sb.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The minimum allowed radius of a colony.</p><p>If any small blips are creating false positives,</p><p>you might want to up this value. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Colony Max Radius", None))
#if QT_CONFIG(tooltip)
        self.circle_max_rad_sb.setToolTip(QCoreApplication.translate("MainWindow", u"The maximum allowed radius of a colony", None))
#endif // QT_CONFIG(tooltip)
        self.output_draw_settings_gb.setTitle(QCoreApplication.translate("MainWindow", u"Output draw settings", None))
#if QT_CONFIG(tooltip)
        self.draw_centers_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Draw the center mark of detected colonies", None))
#endif // QT_CONFIG(tooltip)
        self.draw_centers_cb.setText(QCoreApplication.translate("MainWindow", u"Draw centers", None))
#if QT_CONFIG(tooltip)
        self.draw_circles_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Draw a circle around detected colonies", None))
#endif // QT_CONFIG(tooltip)
        self.draw_circles_cb.setText(QCoreApplication.translate("MainWindow", u"Draw circles", None))
#if QT_CONFIG(tooltip)
        self.draw_dish_circles_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Draw a circle around the detected dish. This is usfull for debugging.", None))
#endif // QT_CONFIG(tooltip)
        self.draw_dish_circles_cb.setText(QCoreApplication.translate("MainWindow", u"Draw dish circle", None))
#if QT_CONFIG(tooltip)
        self.draw_count_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Draw the number of counted colonies on the top left of the image", None))
#endif // QT_CONFIG(tooltip)
        self.draw_count_cb.setText(QCoreApplication.translate("MainWindow", u"Draw count", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"tools", None))
    # retranslateUi

