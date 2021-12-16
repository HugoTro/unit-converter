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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_LengthConverter(object):
    def setupUi(self, LengthConverter):
        if not LengthConverter.objectName():
            LengthConverter.setObjectName(u"LengthConverter")
        LengthConverter.resize(297, 224)
        LengthConverter.setMinimumSize(QSize(297, 0))
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

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 2)


        self.retranslateUi(LengthConverter)

        self.tabs.setCurrentIndex(1)


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
        self.spds_err_line.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.speeds_tab), QCoreApplication.translate("LengthConverter", u"Speeds", None))
    # retranslateUi

