# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exammcq2021_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(522, 199)
        self.lblYourInput = QtWidgets.QLabel(Dialog)
        self.lblYourInput.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.lblYourInput.setObjectName("lblYourInput")
        self.edtInput = QtWidgets.QLineEdit(Dialog)
        self.edtInput.setGeometry(QtCore.QRect(100, 20, 161, 20))
        self.edtInput.setObjectName("edtInput")
        self.lblOutput = QtWidgets.QLabel(Dialog)
        self.lblOutput.setGeometry(QtCore.QRect(100, 50, 161, 16))
        self.lblOutput.setObjectName("lblOutput")
        self.btnCapitalToList = QtWidgets.QPushButton(Dialog)
        self.btnCapitalToList.setGeometry(QtCore.QRect(290, 70, 111, 23))
        self.btnCapitalToList.setObjectName("btnCapitalToList")
        self.btnTitleToList = QtWidgets.QPushButton(Dialog)
        self.btnTitleToList.setGeometry(QtCore.QRect(290, 100, 111, 23))
        self.btnTitleToList.setObjectName("btnTitleToList")
        self.btnAddToList = QtWidgets.QPushButton(Dialog)
        self.btnAddToList.setGeometry(QtCore.QRect(290, 130, 111, 23))
        self.btnAddToList.setObjectName("btnAddToList")
        self.btnClearList = QtWidgets.QPushButton(Dialog)
        self.btnClearList.setGeometry(QtCore.QRect(290, 160, 111, 23))
        self.btnClearList.setObjectName("btnClearList")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(410, 130, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(410, 160, 75, 23))
        self.btnCancel.setObjectName("btnCancel")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 256, 111))
        self.listWidget.setObjectName("listWidget")
        self.lblTestx = QtWidgets.QLabel(Dialog)
        self.lblTestx.setGeometry(QtCore.QRect(330, 50, 151, 16))
        self.lblTestx.setObjectName("lblTestx")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "2021 Exam MCQ"))
        self.lblYourInput.setText(_translate("Dialog", "Your Input:"))
        self.lblOutput.setText(_translate("Dialog", "TextLabel"))
        self.btnCapitalToList.setText(_translate("Dialog", "Capital Add to List"))
        self.btnTitleToList.setText(_translate("Dialog", "Title Add to List"))
        self.btnAddToList.setText(_translate("Dialog", "Add To List"))
        self.btnClearList.setText(_translate("Dialog", "Clear List"))
        self.btnOK.setText(_translate("Dialog", "OK"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
        self.lblTestx.setText(_translate("Dialog", "Test x"))
