from PySide6 import QtWidgets, QtGui
from ui_2t_ui import Ui_LengthConverter
import math
import qdarktheme
from threading import Timer

class conv(QtWidgets.QWidget, Ui_LengthConverter):
    lengths=['Choose a length unit','Feet & inches (ft,in)', 'Centimeters (cm)']
    spds=['Choose a speed unit', 'Kilometers per hour (km/h)', 'Knots (kts)', 'Meters per second (m/s)', 'Feet per minute (fpm)', 'Mach (M)', 'Miles per hour (mph)']
    temps=['Choose a temperature unit', 'Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)']
    def __init__(self):
        super(conv, self).__init__()
        self.ui = Ui_LengthConverter()
        self.ui.setupUi(self)
        self.setupUi()
        self.err_line_reset()
        self.spds_err_line_reset()
        self.setupConnections()
        self.setupShortcuts()
        self.setStyleSheet(qdarktheme.load_stylesheet('dark'))
        self.show()
    def setupUi(self):
        self.ui.dd_in_unit.addItems(self.lengths)
        self.ui.dd_out_unit.addItems(self.lengths)
        self.ui.spds_dd_in_unit.addItems(self.spds)
        self.ui.spds_dd_out_unit.addItems(self.spds)
        self.ui.temps_dd_in_unit.addItems(self.temps)
        self.ui.temps_dd_out_unit.addItems(self.temps)
    def setupConnections(self):
        self.ui.btn_val.clicked.connect(self.convert)
        self.ui.btn_spds_val.clicked.connect(self.spds_convert)
        self.ui.check_dark_mode.stateChanged.connect(self.lgt_drk_mode)
    def setupShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence('Return'), self, self.s_conv)
    def s_conv(self):
        self.convert()
        self.spds_convert()
    def lgt_drk_mode(self):
        if self.ui.check_dark_mode.isChecked():
            self.setStyleSheet(qdarktheme.load_stylesheet('dark'))
        else:
            self.setStyleSheet(qdarktheme.load_stylesheet('light'))
    def set_rounding(self):
        if self.ui.check_rnding.isChecked():
            u=int(self.ui.nbr_rnding.value())
            return u
        else:
            return 999
    def success(self):
        self.ui.error_line.setText(f'Success! Values are rounded to {self.set_rounding()} digits after the decimal.')
        self.setvis()
    def error1(self):
        self.ui.error_line.setText('Something went wrong, please retry.')
        self.setvis()
    def error2(self):
        self.ui.error_line.setText('One of your inputs does not contain numbers.')
        self.setvis()
    def error3(self):
        self.ui.error_line.setText("You didn't input a number.")
        self.setvis()
    def setvis(self):
        n_timer=Timer(5,self.err_line_reset)
        n_timer.start()
    def err_line_reset(self):
        self.ui.error_line.setText('This line will display status messages.')
    def convert(self):
        dd1val=str(self.ui.dd_in_unit.currentText())
        dd2val=str(self.ui.dd_out_unit.currentText())
        a=self.ui.in_line.text()
        b=self.ui.in_line2.text()
        if dd1val==self.lengths[1] and dd2val==self.lengths[2]:
            try:
                cm1=float(a)*30.48
                cm2=float(b)*2.54
                cms=cm1+cm2
                cms=round(cms,self.set_rounding())
                self.ui.out_line.setText(str(cms))
                self.success()
            except:
                self.error2()
        elif dd1val==self.lengths[2] and dd2val==self.lengths[1]:
            try:
                inc=float(a)/2.54
                feet=math.floor(inc/12)
                inches=inc-12*feet
                inches=round(inches,self.set_rounding())
                self.ui.out_line.setText(str(feet))
                self.ui.out_line2.setText(str(inches))
                self.success()
            except:
                self.error3()
        elif dd1val==self.lengths[1] and dd2val==self.lengths[1]:
            try:
                cm1=float(a)*30.48
                cm2=float(b)*2.54
                cms=cm1+cm2
                cms=round(cms,4)
                inc=cms/2.54
                feet=math.floor(inc/12)
                inches=inc-12*feet
                inches=round(inches,self.set_rounding())
                self.ui.out_line.setText(str(feet))
                self.ui.out_line2.setText(str(inches))
                self.success()
            except:
                self.error2()
        elif dd1val==self.lengths[2] and dd2val==self.lengths[2]:
            try:
                self.ui.out_line.setText(a)
                self.success()
            except:
                self.error3()
        else:
            self.error1()
    def spds_convert(self):
        spds_dd1val=str(self.ui.spds_dd_in_unit.currentText())
        spds_dd2val=str(self.ui.spds_dd_out_unit.currentText())
        c=self.ui.spds_in_line.text()
        if spds_dd1val==spds_dd2val:
            self.ui.spds_err_line.setText("I don't think converting units into the same unit is useful :)")
            self.spds_setvis()
        elif spds_dd1val==self.spds[1] and spds_dd2val==self.spds[2]:
            try:
                kts=float(c)/1.852
                kts=round(kts,self.set_rounding())
                self.ui.spds_out_line.setText(str(kts))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[2] and spds_dd2val==self.spds[1]:
            try:
                kmph=float(c)*1.852
                kmph=round(kmph,self.set_rounding())
                self.ui.spds_out_line.setText(str(kmph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[2] and spds_dd2val==self.spds[3]:
            try:
                kmph=float(c)*1.852
                ms=kmph/3.6
                ms=round(ms,self.set_rounding())
                self.ui.spds_out_line.setText(str(ms))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[3] and spds_dd2val==self.spds[2]:
            try:
                kmph=float(c)*3.6
                kts=kmph/1.852
                kts=round(kts,self.set_rounding())
                self.ui.spds_out_line.setText(str(kts))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[2] and spds_dd2val==self.spds[4]:
            try:
                fpm=float(c)*6076.1155/60
                fpm=round(fpm,self.set_rounding())
                self.ui.spds_out_line.setText(str(fpm))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[4] and spds_dd2val==self.spds[2]:
            try:
                kts=float(c)*60/6076.1155
                kts=round(kts,self.set_rounding())
                self.ui.spds_out_line.setText(str(kts))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[2] and spds_dd2val==self.spds[5]:
            try:
                mach=float(c)*1.852/3.6/343
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[5] and spds_dd2val==self.spds[2]:
            try:
                mach=float(c)*343*3.6/1.852
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[3] and spds_dd2val==self.spds[5]:
            try:
                mach=float(c)/343
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[5] and spds_dd2val==self.spds[3]:
            try:
                ms=float(c)*343
                ms=round(ms,self.set_rounding())
                self.ui.spds_out_line.setText(str(ms))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[1] and spds_dd2val==self.spds[3]:
            try:
                ms=float(c)/3.6
                ms=round(ms,self.set_rounding())
                self.ui.spds_out_line.setText(str(ms))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[3] and spds_dd2val==self.spds[1]:
            try:
                kmph=float(c)*3.6
                kmph=round(kmph,self.set_rounding())
                self.ui.spds_out_line.setText(str(kmph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[1] and spds_dd2val==self.spds[5]:
            try:
                mach=float(c)/3.6/343
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[5] and spds_dd2val==self.spds[1]:
            try:
                mach=float(c)*343*3.6
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[3] and spds_dd2val==self.spds[4]:
            try:
                fpm=float(c)*3.28084*60
                fpm=round(fpm,self.set_rounding())
                self.ui.spds_out_line.setText(str(fpm))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[4] and spds_dd2val==self.spds[3]:
            try:
                ms=float(c)/60/3.28084
                ms=round(ms,self.set_rounding())
                self.ui.spds_out_line.setText(str(ms))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[1] and spds_dd2val==self.spds[4]:
            try:
                fpm=float(c)*3280.84/60
                fpm=round(fpm,self.set_rounding())
                self.ui.spds_out_line.setText(str(fpm))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[4] and spds_dd2val==self.spds[1]:
            try:
                kmph=float(c)*60/3280.84
                kmph=round(kmph,self.set_rounding())
                self.ui.spds_out_line.setText(str(kmph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[4] and spds_dd2val==self.spds[5]:
            try:
                mach=float(c)/60/3.28084/343
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[5] and spds_dd2val==self.spds[4]:
            try:
                fpm=float(c)*343*3.28084*60
                fpm=round(fpm,self.set_rounding())
                self.ui.spds_out_line.setText(str(fpm))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[1] and spds_dd2val==self.spds[6]:
            try:
                mph=float(c)*0.6213711922
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[6] and spds_dd2val==self.spds[1]:
            try:
                kmph=float(c)*1.609344
                kmph=round(kmph,self.set_rounding())
                self.ui.spds_out_line.setText(str(kmph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[6] and spds_dd2val==self.spds[5]:
            try:
                mach=float(c)*0.001303
                mach=round(mach,self.set_rounding())
                self.ui.spds_out_line.setText(str(mach))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[5] and spds_dd2val==self.spds[6]:
            try:
                mph=float(c)*767.269148
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[3] and spds_dd2val==self.spds[6]:
            try:
                mph=float(c)*0.00062137119225*3600
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[6] and spds_dd2val==self.spds[3]:
            try:
                ms=float(c)/3600/0.00062137119225
                ms=round(ms,self.set_rounding())
                self.ui.spds_out_line.setText(str(ms))
                self.spds_success()
            except:
                self.spds_err_1()
        
        elif spds_dd1val==self.spds[2] and spds_dd2val==self.spds[6]:
            try:
                mph=float(c)*1.1507794480236
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[6] and spds_dd2val==self.spds[2]:
            try:
                kts=float(c)*0.8689762419007
                kts=round(kts,self.set_rounding())
                self.ui.spds_out_line.setText(str(kts))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[4] and spds_dd2val==self.spds[6]:
            try:
                mph=float(c)/5280*60
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        elif spds_dd1val==self.spds[6] and spds_dd2val==self.spds[4]:
            try:
                mph=float(c)*5280/60
                mph=round(mph,self.set_rounding())
                self.ui.spds_out_line.setText(str(mph))
                self.spds_success()
            except:
                self.spds_err_1()
        else:
            self.ui.spds_err_line.setText('The conversion you wish for is not yet supported. Sorry :/')
            self.spds_setvis()
    def spds_success(self):
        self.ui.spds_err_line.setText(f'Success! Values are rounded to {self.set_rounding()} digits after the decimal.')
        self.spds_setvis()
    def spds_err_1(self):
        self.ui.spds_err_line.setText('Please input a number and retry')
        self.spds_setvis()
    def spds_setvis(self):
        t=Timer(5,self.spds_err_line_reset)
        t.start()
    def spds_err_line_reset(self):
        self.ui.spds_err_line.setText('This line will display status messages.')
    def temps_convert(self):
        temps_dd1val=str(self.ui.temps_dd_in_unit.currentText())
        temps_dd2val=str(self.ui.temps_dd_out_unit.currentText())
        d=self.ui.spds_in_line.text()

app=QtWidgets.QApplication()
window1=conv()
app.exec()

