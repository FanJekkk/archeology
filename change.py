# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui',
# licensing of 'change.ui' applies.
#
# Created: Sat Mar 14 17:21:08 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import charch
import dbarch
from PyQt5.QtWidgets import *
import sqlite3
conn = sqlite3.connect('./database.db')

class Ui_Dialog(object):
    def opendb(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dbarch.Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def closeWindow(self, Dialog):
        Dialog.hide()
    def openWindow(self, Dialog):
        searchrol = str(self.lineEdit.text())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE id_artefact=?", (searchrol,))
        data = cur.fetchone()
        if data:
            self.window = QtWidgets.QDialog()
            self.ui1 = charch.Ui_Dialog1()
            self.ui1.setupUi(self.window)
            self.window.show()
            image = data[1]
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image, 'jpg')
            pixmap = pixmap.scaledToWidth(300)
            self.ui1.imagelabel.setPixmap(pixmap)
            self.ui1.imagelabel.setGeometry(0,0,120,120)
            self.ui1.lineEdit.setText(searchrol)
            self.ui1.lineEdit_2.setText(data[3])
            name = data[3]
            self.ui1.comboBox_4.addItem(str(data[4]))
            cur.execute("SELECT * FROM colors")
            for row in cur:
                self.ui1.comboBox_4.addItem(str(row[1]))
            Dialog.hide()
        elif searchrol == '':
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Введите ID  артефакта")
            self.lineEdit.setStyleSheet("color: red;\n")
        else:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Артефаката с таким ID не найдено")
            self.lineEdit.setStyleSheet("color: black;\n")
        cur.close()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 341)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
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
        self.pushButton.clicked.connect(lambda: self.openWindow(Dialog))
        self.verticalLayout_2.addWidget(self.pushButton)
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
        self.pushButton_2.clicked.connect(self.opendb)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(Dialog))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Поиск артефакта для изменения", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Введите ID артефакта,\n"
"который хотите изменить", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "OK", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "Отмена", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    line = QLineEdit()
    sys.exit(app.exec_())

