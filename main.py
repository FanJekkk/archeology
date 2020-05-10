# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sat Mar  7 15:27:35 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from menu import *
from PyQt5.QtWidgets import*

class Ui_MainWindow(object):
    def openWindow(self):
        if  self.lineEdit.text() == "admin":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MenuWindow()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()
        else:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Пароль неверный")
            self.lineEdit.setStyleSheet("color: red;\n")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(557, 369)
        MainWindow.setMinimumSize(QtCore.QSize(0, 350))
        MainWindow.setMaximumSize(QtCore.QSize(558, 402))
        MainWindow.setStyleSheet("QWidget#centralwidget {background-image: url(:/images/image/tt3.jpg);} \n"
                                 "QLabel#label_3 {\n"
                                 "image: url(:/images/image/avatar.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(14)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton.setStyleSheet(" QPushButton#pushButton {\n"
                                      "     background-color: #EEDDFF;\n"
                                      "  border: 1px solid #7922CC;\n"
                                      "  border-radius: 25px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:pressed {\n"
                                      "     background-color: rgb(224, 0, 0);     \n"
                                      " }\n"
                                      " QPushButton#pushButton:hover {\n"
                                      "     background-color:#FFE8DB;\n"
                                      " }\n"
                                      "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("opacity: 1;\n"
                                 "color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
                                   "opacity: 1;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 190, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите пароль")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 171, 121))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Археология", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Войти", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Авторизация", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Пароль", None, -1))


import icont

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
