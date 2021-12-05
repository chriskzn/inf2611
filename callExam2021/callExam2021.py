# This is the default import statement for PyQt
import sys
# This is the main import for PyQt to let Python know
# we have QtWidgets appliction and we need the form imported
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
# This is the name of the ui file we converted
from ui_exammcq2021 import *
# Define our Form Class, this is our top-level object, it i a Dialog application
class MyForm(QDialog):
    # Create an initializer constructor for our class - form
    def __init__(self):
        super().__init__()
        # Initialize the actual Dialog class itself
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Add items to ListWidget
        self.ui.listWidget.addItem('The text to add')
        self.ui.listWidget.addItem('The Text To Add')
        self.ui.listWidget.addItem('the text to add')

        # Add a Signal and Slot to the OK Button
        self.ui.btnOK.clicked.connect(self.Test)

        # Add a Signal and Slot to the "Capital Add to List" button
        self.ui.btnCapitalToList.clicked.connect(self.CapitalAddToList)

    def Test(self):
        # Variable to store LineEdit
        x=self.ui.edtInput.text()
        # Capitalize the variable x and store in variable y
        y=x.capitalize()
        # Convert whole string to UpperCase
        t=y.upper()
        # Display results of y
        self.ui.lblTestx.setText(y)
        # Display result on spare Text Label
        self.ui.lblOutput.setText(t)

    def CapitalAddToList(self):
        # Variable to store LineEdit
        x=self.ui.edtInput.text()
        # Capitalize the variable x and store in variable y
        y=x.capitalize()
        # Display the text to the lable
        self.ui.lblOutput.setText(y)
        # Add the text to the listWidget
        self.ui.listWidget.addItem(y)
        
        
if __name__=="__main__":
    # Creates an application object with the name app through QApplication
    # Every PyQt5 application must create sys.argv
    # The sys.argv parameter helps in passing and controlling the startup
    # attributes of a script.
    app = QApplication(sys.argv)
    # An instance of the MyForm class is created with the name w.
    w = MyForm()
    # The show() method will display the widget on the screen
    w.show()
    # The sys.exit() method ensures a clean exit, releasing memory resources
    # The exec_() method has an underscore because exec is a Python keyword.
    sys.exit(app.exec_())
