# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_2t.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_LengthConverter(object):
    def setupUi(self, LengthConverter):
        if not LengthConverter.objectName():
            LengthConverter.setObjectName(u"LengthConverter")
        LengthConverter.resize(501, 278)
        LengthConverter.setMinimumSize(QSize(365, 0))
        self.gridLayout = QGridLayout(LengthConverter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabs = QTabWidget(LengthConverter)
        self.tabs.setObjectName(u"tabs")
        self.lengths_tab = QWidget()
        self.lengths_tab.setObjectName(u"lengths_tab")
        self.gridLayout_2 = QGridLayout(self.lengths_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dd_in_unit = QComboBox(self.lengths_tab)
        self.dd_in_unit.setObjectName(u"dd_in_unit")

        self.gridLayout_2.addWidget(self.dd_in_unit, 2, 0, 1, 2)

        self.dd_out_unit = QComboBox(self.lengths_tab)
        self.dd_out_unit.setObjectName(u"dd_out_unit")
        self.dd_out_unit.setDuplicatesEnabled(False)

        self.gridLayout_2.addWidget(self.dd_out_unit, 4, 0, 1, 2)

        self.btn_val = QPushButton(self.lengths_tab)
        self.btn_val.setObjectName(u"btn_val")

        self.gridLayout_2.addWidget(self.btn_val, 3, 0, 1, 2)

        self.in_line2 = QLineEdit(self.lengths_tab)
        self.in_line2.setObjectName(u"in_line2")

        self.gridLayout_2.addWidget(self.in_line2, 0, 1, 1, 1)

        self.out_line2 = QLineEdit(self.lengths_tab)
        self.out_line2.setObjectName(u"out_line2")

        self.gridLayout_2.addWidget(self.out_line2, 5, 1, 1, 1)

        self.in_line = QLineEdit(self.lengths_tab)
        self.in_line.setObjectName(u"in_line")
        self.in_line.setMaxLength(32767)

        self.gridLayout_2.addWidget(self.in_line, 0, 0, 1, 1)

        self.out_line = QLineEdit(self.lengths_tab)
        self.out_line.setObjectName(u"out_line")

        self.gridLayout_2.addWidget(self.out_line, 5, 0, 1, 1)

        self.error_line = QLabel(self.lengths_tab)
        self.error_line.setObjectName(u"error_line")
        self.error_line.setEnabled(True)
        self.error_line.setMaximumSize(QSize(16777215, 17))

        self.gridLayout_2.addWidget(self.error_line, 6, 0, 1, 2)

        self.tabs.addTab(self.lengths_tab, "")
        self.speeds_tab = QWidget()
        self.speeds_tab.setObjectName(u"speeds_tab")
        self.gridLayout_3 = QGridLayout(self.speeds_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_spds_val = QPushButton(self.speeds_tab)
        self.btn_spds_val.setObjectName(u"btn_spds_val")

        self.gridLayout_3.addWidget(self.btn_spds_val, 2, 0, 1, 1)

        self.spds_dd_in_unit = QComboBox(self.speeds_tab)
        self.spds_dd_in_unit.setObjectName(u"spds_dd_in_unit")

        self.gridLayout_3.addWidget(self.spds_dd_in_unit, 1, 0, 1, 1)

        self.spds_in_line = QLineEdit(self.speeds_tab)
        self.spds_in_line.setObjectName(u"spds_in_line")

        self.gridLayout_3.addWidget(self.spds_in_line, 0, 0, 1, 1)

        self.spds_out_line = QLineEdit(self.speeds_tab)
        self.spds_out_line.setObjectName(u"spds_out_line")

        self.gridLayout_3.addWidget(self.spds_out_line, 4, 0, 1, 1)

        self.spds_dd_out_unit = QComboBox(self.speeds_tab)
        self.spds_dd_out_unit.setObjectName(u"spds_dd_out_unit")

        self.gridLayout_3.addWidget(self.spds_dd_out_unit, 3, 0, 1, 1)

        self.spds_err_line = QLabel(self.speeds_tab)
        self.spds_err_line.setObjectName(u"spds_err_line")
        self.spds_err_line.setMaximumSize(QSize(16777215, 17))

        self.gridLayout_3.addWidget(self.spds_err_line, 5, 0, 1, 1)

        self.tabs.addTab(self.speeds_tab, "")
        self.weights_tab = QWidget()
        self.weights_tab.setObjectName(u"weights_tab")
        self.verticalLayout = QVBoxLayout(self.weights_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.weights_tab)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tabs.addTab(self.weights_tab, "")
        self.forces_tab = QWidget()
        self.forces_tab.setObjectName(u"forces_tab")
        self.gridLayout_5 = QGridLayout(self.forces_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.forces_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.tabs.addTab(self.forces_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.temps_in_line = QLineEdit(self.tab)
        self.temps_in_line.setObjectName(u"temps_in_line")

        self.verticalLayout_2.addWidget(self.temps_in_line)

        self.temps_dd_in_unit = QComboBox(self.tab)
        self.temps_dd_in_unit.setObjectName(u"temps_dd_in_unit")

        self.verticalLayout_2.addWidget(self.temps_dd_in_unit)

        self.btn_temps_val = QPushButton(self.tab)
        self.btn_temps_val.setObjectName(u"btn_temps_val")

        self.verticalLayout_2.addWidget(self.btn_temps_val)

        self.temps_dd_out_unit = QComboBox(self.tab)
        self.temps_dd_out_unit.setObjectName(u"temps_dd_out_unit")

        self.verticalLayout_2.addWidget(self.temps_dd_out_unit)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.temps_err_line = QLabel(self.tab)
        self.temps_err_line.setObjectName(u"temps_err_line")
        self.temps_err_line.setMaximumSize(QSize(16777215, 17))

        self.verticalLayout_2.addWidget(self.temps_err_line)

        self.tabs.addTab(self.tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.gridLayout_4 = QGridLayout(self.settings_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.settings_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 22))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.check_rnding = QCheckBox(self.settings_tab)
        self.check_rnding.setObjectName(u"check_rnding")
        self.check_rnding.setCheckable(True)
        self.check_rnding.setChecked(True)

        self.gridLayout_4.addWidget(self.check_rnding, 1, 0, 1, 1)

        self.label_3 = QLabel(self.settings_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)

        self.check_dark_mode = QCheckBox(self.settings_tab)
        self.check_dark_mode.setObjectName(u"check_dark_mode")
        self.check_dark_mode.setChecked(True)

        self.gridLayout_4.addWidget(self.check_dark_mode, 0, 0, 1, 1)

        self.nbr_rnding = QSpinBox(self.settings_tab)
        self.nbr_rnding.setObjectName(u"nbr_rnding")
        self.nbr_rnding.setMaximum(12)
        self.nbr_rnding.setValue(9)

        self.gridLayout_4.addWidget(self.nbr_rnding, 2, 0, 1, 1)

        self.tabs.addTab(self.settings_tab, "")

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 2)


        self.retranslateUi(LengthConverter)

        self.tabs.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(LengthConverter)
    # setupUi

    def retranslateUi(self, LengthConverter):
        LengthConverter.setWindowTitle(QCoreApplication.translate("LengthConverter", u"Unit converter", None))
        self.dd_out_unit.setPlaceholderText("")
        self.btn_val.setText(QCoreApplication.translate("LengthConverter", u"Convert to", None))
        self.in_line2.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Second line for inches", None))
        self.in_line.setInputMask("")
        self.in_line.setText("")
        self.in_line.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Write your length here", None))
        self.error_line.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.lengths_tab), QCoreApplication.translate("LengthConverter", u"Lengths", None))
        self.btn_spds_val.setText(QCoreApplication.translate("LengthConverter", u"Convert to", None))
        self.spds_in_line.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Input a speed here", None))
        self.spds_err_line.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.speeds_tab), QCoreApplication.translate("LengthConverter", u"Speeds", None))
        self.label.setText(QCoreApplication.translate("LengthConverter", u"INOP", None))
        self.tabs.setTabText(self.tabs.indexOf(self.weights_tab), QCoreApplication.translate("LengthConverter", u"Weights", None))
        self.label_6.setText(QCoreApplication.translate("LengthConverter", u"INOP", None))
        self.tabs.setTabText(self.tabs.indexOf(self.forces_tab), QCoreApplication.translate("LengthConverter", u"Forces", None))
        self.temps_in_line.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Input a temperature here", None))
        self.btn_temps_val.setText(QCoreApplication.translate("LengthConverter", u"Convert to", None))
        self.temps_err_line.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("LengthConverter", u"Temperatures", None))
        self.label_4.setText(QCoreApplication.translate("LengthConverter", u"Convert: Enter", None))
        self.check_rnding.setText(QCoreApplication.translate("LengthConverter", u"Round numbers (numbers after the decimal)", None))
        self.label_3.setText("")
        self.check_dark_mode.setText(QCoreApplication.translate("LengthConverter", u"Dark Mode (Recommended)", None))
        self.tabs.setTabText(self.tabs.indexOf(self.settings_tab), QCoreApplication.translate("LengthConverter", u"Settings", None))
    # retranslateUi

