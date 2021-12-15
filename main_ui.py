# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_LengthConverter(object):
    def setupUi(self, LengthConverter):
        if not LengthConverter.objectName():
            LengthConverter.setObjectName(u"LengthConverter")
        LengthConverter.resize(290, 180)
        self.gridLayout = QGridLayout(LengthConverter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.out_line2 = QLineEdit(LengthConverter)
        self.out_line2.setObjectName(u"out_line2")

        self.gridLayout.addWidget(self.out_line2, 4, 1, 1, 1)

        self.out_line = QLineEdit(LengthConverter)
        self.out_line.setObjectName(u"out_line")

        self.gridLayout.addWidget(self.out_line, 4, 0, 1, 1)

        self.dd_out_unit = QComboBox(LengthConverter)
        self.dd_out_unit.setObjectName(u"dd_out_unit")
        self.dd_out_unit.setDuplicatesEnabled(False)

        self.gridLayout.addWidget(self.dd_out_unit, 3, 0, 1, 2)

        self.dd_in_unit = QComboBox(LengthConverter)
        self.dd_in_unit.setObjectName(u"dd_in_unit")

        self.gridLayout.addWidget(self.dd_in_unit, 1, 0, 1, 2)

        self.in_line2 = QLineEdit(LengthConverter)
        self.in_line2.setObjectName(u"in_line2")

        self.gridLayout.addWidget(self.in_line2, 0, 1, 1, 1)

        self.btn_val = QPushButton(LengthConverter)
        self.btn_val.setObjectName(u"btn_val")

        self.gridLayout.addWidget(self.btn_val, 2, 0, 1, 2)

        self.in_line = QLineEdit(LengthConverter)
        self.in_line.setObjectName(u"in_line")
        self.in_line.setMaxLength(32767)

        self.gridLayout.addWidget(self.in_line, 0, 0, 1, 1)

        self.error_line = QLabel(LengthConverter)
        self.error_line.setObjectName(u"error_line")
        self.error_line.setEnabled(True)

        self.gridLayout.addWidget(self.error_line, 5, 0, 1, 2)


        self.retranslateUi(LengthConverter)

        QMetaObject.connectSlotsByName(LengthConverter)
    # setupUi

    def retranslateUi(self, LengthConverter):
        LengthConverter.setWindowTitle(QCoreApplication.translate("LengthConverter", u"Unit converter", None))
        self.dd_out_unit.setPlaceholderText("")
        self.in_line2.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Second line for inches", None))
        self.btn_val.setText(QCoreApplication.translate("LengthConverter", u"Convert to", None))
        self.in_line.setInputMask("")
        self.in_line.setText("")
        self.in_line.setPlaceholderText(QCoreApplication.translate("LengthConverter", u"Write your length here", None))
        self.error_line.setText("")
    # retranslateUi

