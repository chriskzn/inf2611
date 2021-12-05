import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_showDate import *

class MyForm(QDialog):
     def __init__(self, parent = None):
          super().__init__()
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)

          # Add signal and slot to pushButton
          self.ui.pushButton_ShowDate.clicked.connect(self.showDate)

     def showDate(self):
          self.ui.dateEdit.setDisplayFormat('MMM d yyyy')
          self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
     
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
