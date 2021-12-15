from PySide6 import QtWidgets, QtGui
from main_ui import Ui_LengthConverter
import math

class conv(QtWidgets.QWidget, Ui_LengthConverter):
    convu=['Choose a length','Feet & inches', 'Centimeters']
    def __init__(self):
        super(conv, self).__init__()
        self.ui = Ui_LengthConverter()
        self.ui.setupUi(self)
        self.setupUi()
        self.ui.error_line.setVisible(False)
        self.setupConnections()
        self.setupShortcuts()
        self.show()
    def setupUi(self):
        self.ui.dd_in_unit.addItems(self.convu)
        self.ui.dd_out_unit.addItems(self.convu)
    def setupConnections(self):
        self.ui.btn_val.clicked.connect(self.convert)
    def setupShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence('Return'), self, self.convert)
    def success(self):
        self.ui.error_line.setText('Success! Some values might be rounded.')
        self.ui.error_line.setVisible(True)
    def error1(self):
        self.ui.error_line.setText('Something went wrong, please retry.')
        self.ui.error_line.setVisible(True)
    def error2(self):
        self.ui.error_line.setText('One of your inputs does not contain numbers.')
        self.ui.error_line.setVisible(True)
    def error3(self):
        self.ui.error_line.setText("You didn't input a number")
        self.ui.error_line.setVisible(True)
    def convert(self):
        dd1val=str(self.ui.dd_in_unit.currentText())
        dd2val=str(self.ui.dd_out_unit.currentText())
        a=self.ui.in_line.text()
        b=self.ui.in_line2.text()
        if dd1val==self.convu[1] and dd2val==self.convu[2]:
            try:
                cm1=float(a)*30.48
                cm2=float(b)*2.54
                cms=cm1+cm2
                cms=round(cms,2)
                self.ui.out_line.setText(str(cms))
                self.success()
            except:
                self.error2()
        elif dd1val==self.convu[2] and dd2val==self.convu[1]:
            try:
                inc=float(a)/2.54
                feet=math.floor(inc/12)
                inches=inc-12*feet
                inches=round(inches,2)
                self.ui.out_line.setText(str(feet))
                self.ui.out_line2.setText(str(inches))
                self.success()
            except:
                self.error3()
        elif dd1val==self.convu[1] and dd2val==self.convu[1]:
            try:
                cm1=float(a)*30.48
                cm2=float(b)*2.54
                cms=cm1+cm2
                cms=round(cms,4)
                inc=cms/2.54
                feet=math.floor(inc/12)
                inches=inc-12*feet
                inches=round(inches,2)
                self.ui.out_line.setText(str(feet))
                self.ui.out_line2.setText(str(inches))
                self.success()
            except:
                self.error2()
        elif dd1val==self.convu[2] and dd2val==self.convu[2]:
            try:
                self.ui.out_line.setText(a)
                self.success()
            except:
                self.error3()
        else:
            self.error1()

app=QtWidgets.QApplication()
window1=conv()
app.exec()

