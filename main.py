import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from OptionPricing import Option_Pricing


# Change to the file we work on
qtCreatorFile = "optionpricingGUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# Main code
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
        # more initialization
    
    def calculate(self):
        S = float(self.Stock_Price.text())
        K = float(self.Strike_Price.text())
        r = float(self.R.text())
        q = float(self.Q.text())
        T = self.date_begin.date().daysTo(self.date_end.date())/365
        M = int(self.Price_Step.text())
        N = int(self.Time_Step.text())
        sigma = float(self.Volatility.text())

        EuropeanOption = Option_Pricing(S, K, r, q, T, sigma)
        price = EuropeanOption.explicit(M, N)

        # Final price
        self.Call_Option.setText(str(round(price['call'],4)))
        self.Put_Option.setText(str(round(price['put'],4)))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



