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
            self.imagelabel.show()
    def check_local(self):
        local = self.lineEdit_4.text()
        if local == '':
            self.lineEdit_4.setText("нет данных")
        else:
            self.lineEdit_4.setText(local)
        return local
    def convertImage(self):
        fname = self.lineEdit_3.text()
        if fname == '':
            self.lineEdit_3.setText("C:/Users/dns/PycharmProjects/qtarch/1234.jpg")
            with open('1234.jpg', 'rb') as file:
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

    def choose_admixture(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM admixture")
        for row in cur:
            self.comboBox_3.addItem(str(row[1]))
    def choose_thickness(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM thickness")
        for row in cur:
            self.comboBox_2.addItem(str(row[1]))
    def choose_water_absorption(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM water_absorption")
        for row in cur:
            self.comboBox_5.addItem(str(row[1]))
    def choose_defect(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM defect")
        for row in cur:
            self.comboBox_6.addItem(str(row[1]))
    def choose_texture(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM texture")
        for row in cur:
            self.comboBox_7.addItem(str(row[1]))
    def adding(self, fname):
        id_artefact = str(self.lineEdit.text())
        name = self.lineEdit_2.text()
        local = self.lineEdit_4.text()
        if local == '':
            self.lineEdit_4.setText("нет данных")
        else:
            self.lineEdit_4.setText(local)
        color_id = self.comboBox.itemText(self.comboBox.currentIndex())
        type_id = self.comboBox_4.itemText(self.comboBox_4.currentIndex())
        admixture_id = self.comboBox_3.itemText(self.comboBox_3.currentIndex())
        thickness_id = self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        water_absorption_id = self.comboBox_5.itemText(self.comboBox_5.currentIndex())
        defect_id = self.comboBox_6.itemText(self.comboBox_6.currentIndex())
        texture_id = self.comboBox_7.itemText(self.comboBox_7.currentIndex())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE id_artefact=?", (id_artefact,))
        data = cur.fetchall()
        if data:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Такой ID уже существует, введите другой")
        elif id_artefact == '':
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Введите ID  артефакта")
            self.lineEdit.setStyleSheet("color: red;\n")
            self.lineEdit_4.setText("")
        else:
            picture = self.convertImage()
            local = self.check_local()
            path_picture = str(self.lineEdit_3.text())
            QMessageBox.information(QMessageBox(), 'Successful', 'Артефакт добавлен')
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("ID артефакта")
            self.lineEdit.setStyleSheet("color: black;\n")
            self.lineEdit_2.setText("")
            self.imagelabel.setText("")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO artefacts (picture,id_artefact, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id, defect_id, texture_id, path_picture, local) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (picture, id_artefact, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                 defect_id, texture_id, path_picture, local))
            conn.commit()
            cur.close()
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            index = self.comboBox_4.findText("нет данных по типу", QtCore.Qt.MatchFixedString)
            self.comboBox_4.setCurrentIndex(index)
            index = self.comboBox_3.findText("нет данных по примесям", QtCore.Qt.MatchFixedString)
            self.comboBox_3.setCurrentIndex(index)
            index = self.comboBox_2.findText("нет данных по толщине стенки", QtCore.Qt.MatchFixedString)
            self.comboBox_2.setCurrentIndex(index)
            index = self.comboBox.findText("нет данных по цвету", QtCore.Qt.MatchFixedString)
            self.comboBox.setCurrentIndex(index)
            index = self.comboBox_5.findText("нет данных по водопоглощению", QtCore.Qt.MatchFixedString)
            self.comboBox_5.setCurrentIndex(index)
            index = self.comboBox_6.findText("нет данных по дефектам", QtCore.Qt.MatchFixedString)
            self.comboBox_6.setCurrentIndex(index)
            index = self.comboBox_7.findText("нет данных по текстуре массы", QtCore.Qt.MatchFixedString)
            self.comboBox_7.setCurrentIndex(index)
            self.imagelabel.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        MainWindow.setMinimumSize(QtCore.QSize(800, 620))
        MainWindow.setMaximumSize(QtCore.QSize(800, 620))
        MainWindow.setStyleSheet(" \n"
                                 "  font-size: 18px;\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setEditable(False)
        self.comboBox_4.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setMaxVisibleItems(10)
        self.comboBox_5.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.imagelabel = QtWidgets.QLabel(MainWindow)
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.imagelabel.setText("")
        self.horizontalLayout.addWidget(self.imagelabel)
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setMaxVisibleItems(10)
        self.comboBox_6.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_6.setObjectName("comboBox_6")
        self.verticalLayout.addWidget(self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setMaxVisibleItems(10)
        self.comboBox_7.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_7.setObjectName("comboBox_7")
        self.verticalLayout.addWidget(self.comboBox_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setAcceptDrops(True)
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
        self.choose_admixture()
        self.choose_thickness()
        self.choose_water_absorption()
        self.choose_defect()
        self.choose_texture()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Добавление артефакта", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "ID артефакта", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Часть сосуда", None, -1))
        self.comboBox_4.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Тип артефакта", None, -1))
        self.comboBox_3.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Примеси", None, -1))
        self.comboBox.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "", None, -1))
        self.comboBox_2.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.comboBox_5.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Толщина", None, -1))
        self.comboBox_6.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Брак", None, -1))
        self.lineEdit_4.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Место нахождения", None, -1))
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

