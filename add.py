# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui',
# licensing of 'add.ui' applies.
#
# Created: Sat Mar 14 17:43:00 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QMainWindow, QFileDialog
import dbarch
import sys
import sqlite3
from PyQt5.QtWidgets import *
conn = sqlite3.connect('./database.db')

class Ui_MainWindow(QMainWindow):

    def chooseImage(self):
        fname,_ = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image file (*.jpg)')
        if fname:
            self.lineEdit_3.setText(fname)
            pixmap = QtGui.QPixmap(fname)
            pixmap = pixmap.scaledToWidth(300)
            self.imagelabel.setPixmap(pixmap)
    def convertImage(self):
        fname = self.lineEdit_3.text()
        if fname == '':
            with open('C:/Users/dns/PycharmProjects/qtarch/1234.jpg', 'rb') as file:
                picture = file.read()
        else:
            with open(fname, 'rb') as file:
                picture = file.read()
        return picture

    def closeWindow(self, MainWindow):
        MainWindow.hide()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dbarch.Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def choose_color(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM colors")
        for row in cur:
            self.comboBox.addItem(str(row[1]))

    def choose_type(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM types")
        for row in cur:
            self.comboBox_4.addItem(str(row[1]))
    def adding(self, fname):
        id_artefact = str(self.lineEdit.text())
        name = self.lineEdit_2.text()
        color_id = self.comboBox.itemText(self.comboBox.currentIndex())
        type_id = self.comboBox_4.itemText(self.comboBox_4.currentIndex())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE id_artefact=?", (id_artefact,))
        data = cur.fetchall()
        picture = self.convertImage()
        if data:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Такой ID уже существует, введите другой")
        elif id_artefact == '':
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Введите ID  артефакта")
            self.lineEdit.setStyleSheet("color: red;\n")
        else:
            QMessageBox.information(QMessageBox(), 'Successful', 'Артефакт добавлен')
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("ID артефакта")
            self.lineEdit.setStyleSheet("color: black;\n")
            cur = conn.cursor()
            cur.execute("INSERT INTO artefacts (picture,id_artefact, name, color_id, type_id) VALUES (?,?,?,?,?)", (picture, id_artefact, name, color_id, type_id))
            conn.commit()
            cur.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox.setEditable(False)
        self.comboBox_4.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.imagelabel = QtWidgets.QLabel(MainWindow)
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.imagelabel.setText("")
        self.horizontalLayout.addWidget(self.imagelabel)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setAcceptDrops(True)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.clicked.connect(self.chooseImage)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.adding)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
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
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.choose_color()
        self.choose_type()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Добавление артефакта", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "ID артефакта", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Часть сосуда", None, -1))
        self.comboBox_4.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Тип артефакта", None, -1))
        self.comboBox_3.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Удлиненная", None, -1))
        self.comboBox_3.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Удлиненная", None, -1))
        self.comboBox_3.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Закргуленная", None, -1))
        self.comboBox.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "", None, -1))
        self.comboBox_2.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.comboBox_2.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.comboBox_2.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "1,5", None, -1))
        self.comboBox_2.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.comboBox_2.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.lineEdit_3.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Фото не выбрано", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Выбор фото", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "ОК", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Назад", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

