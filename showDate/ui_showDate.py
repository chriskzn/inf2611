# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showDate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(364, 329)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(90, 230, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.label.setObjectName("label")
        self.pushButton_ShowDate = QtWidgets.QPushButton(Dialog)
        self.pushButton_ShowDate.setGeometry(QtCore.QRect(200, 270, 75, 23))
        self.pushButton_ShowDate.setObjectName("pushButton_ShowDate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Selected Date: "))
        self.pushButton_ShowDate.setText(_translate("Dialog", "Show Date"))