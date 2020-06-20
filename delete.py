# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui',
# licensing of 'delete.ui' applies.
#
# Created: Sat Mar 14 17:39:33 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import dbarch
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog
import sqlite3
from PyQt5.QtCore import QObject
import sys
conn = sqlite3.connect('./database.db')

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Ui_Dialog, self).__init__(*args, **kwargs)
    def closeWindow(self, Dialog):
        Dialog.hide()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dbarch.Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def deleting(self):
        Dialog = QDialog()
        line = str(self.lineEdit.text())
        cur = conn.cursor()
        result = cur.execute("SELECT * from artefacts WHERE id_artefact=?", (line,))

        if (len(result.fetchall()) > 0):
            Dialog.hide()
            cur = conn.cursor()
            cur.execute("DELETE from artefacts WHERE id_artefact = ?", (line,) )
            conn.commit()
            QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')
            cur.close()
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Артефакта с таким ID не найдено.")
        cur.close()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet(" \n"
                             "  font-size: 18px;\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.deleting)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
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
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setStyleSheet(" QPushButton#pushButton_2 {\n"
                                      "     background-color: #EEDDFF;\n"
                                      "  border: 1px solid #7922CC;\n"
                                      "  border-radius: 25px;\n"
                                      "}\n"
                                      "QPushButton#pushButton_2:pressed {\n"
                                      "     background-color: rgb(224, 0, 0);     \n"
                                      " }\n"
                                      " QPushButton#pushButton_2:hover {\n"
                                      "     background-color:#FFE8DB;\n"
                                      " }\n"
                                      "")
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(Dialog))
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Удаление артефакта", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Введите ID артефакта для удаления", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "OK", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "Назад", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

