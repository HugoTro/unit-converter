from ui_2t_ui import Ui_LengthConverter

class Temperature(Ui_LengthConverter):
    def temps_convert(self):
            temps_dd1val=str(self.ui.temps_dd_in_unit.currentText())
            temps_dd2val=str(self.ui.temps_dd_out_unit.currentText())
            d=self.ui.temps_in_line.text()
            if temps_dd1val==self.temps[1] and temps_dd2val==self.temps[2]:
                try:
                    fahrenheit=float(d)*(9/5)+32
                    fahrenheit=round(fahrenheit,self.set_rounding())
                    self.ui.temps_out_line.setText(str(fahrenheit))
                    self.temps_success()
                except:
                    self.temps_err_1()
            elif temps_dd1val==self.temps[2] and temps_dd2val==self.temps[1]:
                try:
                    celsius=(float(d)-32)*(5/9)
                    celsius=round(celsius,self.set_rounding())
                    self.ui.temps_out_line.setText(str(celsius))
                    self.temps_success()
                except:
                    self.temps_err_1()
            elif temps_dd1val==self.temps[1] and temps_dd2val==self.temps[3]:
                try:
                    kelvin=float(d)+273.15
                    kelvin=round(kelvin,self.set_rounding())
                    self.ui.temps_out_line.setText(str(kelvin))
                    self.temps_success()
                except:
                    self.temps_err_1()
            elif temps_dd1val==self.temps[3] and temps_dd2val==self.temps[1]:
                try:
                    celsius=float(d)-273.15
                    celsius=round(celsius,self.set_rounding())
                    self.ui.temps_out_line.setText(str(celsius))
                    self.temps_success()
                except:
                    self.temps_err_1()
            elif temps_dd1val==self.temps[2] and temps_dd2val==self.temps[3]:
                try:
                    kelvin=(float(d)-32)*(5/9)+273.15
                    kelvin=round(kelvin,self.set_rounding())
                    self.ui.temps_out_line.setText(str(kelvin))
                    self.temps_success()
                except:
                    self.temps_err_1()
            elif temps_dd1val==self.temps[3] and temps_dd2val==self.temps[2]:
                try:
                    fahrenheit=(float(d)-273.15)*(9/5)+32
                    fahrenheit=round(fahrenheit,self.set_rounding())
                    self.ui.temps_out_line.setText(str(fahrenheit))
                    self.temps_success()
                except:
                    self.temps_err_1()
            else:
                self.ui.temps_err_line.setText('The conversion you wish for is not yet supported. Sorry :/')
                self.temps_setvis()