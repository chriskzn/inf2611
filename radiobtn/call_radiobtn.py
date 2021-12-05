import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_radiobtn import *

class MyForm(QDialog):
     def __init__(self, parent = None):
          super().__init__()
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)

          self.ui.pushButton_Compute.clicked.connect(self.Compute)
          # Set the default radiobutton to Multiply
          self.ui.radioButton_Multiply.setChecked(1)

     def Compute(self):
          if len(self.ui.lineEdit_First.text()) !=0:
               a = int(self.ui.lineEdit_First.text())
          else:
               a = 0

          if len(self.ui.lineEdit_Second.text()) !=0:
               b = int(self.ui.lineEdit_Second.text())
          else:
               b = 0

          if self.ui.radioButton_Add.isChecked() == True:
               result = a + b
          if self.ui.radioButton_Subtract.isChecked() == True:
               result = a - b
          if self.ui.radioButton_Multiply.isChecked() == True:
               result = a * b
          if self.ui.radioButton_Divide.isChecked() == True:
               result = a / b

          self.ui.lblResult.setText("Result: " + str(result))
          
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
