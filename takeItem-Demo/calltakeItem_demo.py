import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_takeItem_demo import *

class MyForm(QDialog):
     def __init__(self, parent = None):
          super().__init__()
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)

          # Code for button Add
          self.ui.btnAdd.clicked.connect(self.addCountry)

          # Code for takeItem(2)
          self.ui.btnTake2.clicked.connect(self.take2)

     def addCountry(self):
          self.ui.listWidget.addItem(self.ui.lineEdit_Country.text())
          self.ui.lineEdit_Country.setText('')                  

     def take2(self):
          self.ui.listWidget.takeItem(2)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
     
