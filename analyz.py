# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyz.ui',
# licensing of 'analyz.ui' applies.
#
# Created: Mon Jun  1 11:15:56 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import menu
import classif
import pandas as pd
import add_data
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

class Ui_MainWindow(object):
    def closeWindow(self, MainWindow):
        MainWindow.hide()
    def loadData(self):
        while self.tableWidget.rowCount() >0:
            self.tableWidget.removeRow(0)
        query1 = "SELECT classes, color_id, type_id, admixture_id, thickness_id, water_absorption_id, texture_id, defect_id " \
                 " FROM train_artefacts"
        res = cur.execute(query1)
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        return
    def add_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = add_data.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def del_data(self):
        query = "SELECT * " \
            " FROM train_artefacts"
        res = cur.execute(query)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                print(data)
                cl_id = data[0]
                classes = data[1]
                color_id = data[2]
                type_id = data[3]
                admixture_id = data[4]
                thickness_id = data[5]
                water_absorption_id = data[6]
                texture_id = data[7]
                defect_id = data[8]
                cur.execute("DELETE FROM train_artefacts WHERE id = ? ", (cl_id,))
                conn.commit()
                self.loadData()
    def classif(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = classif.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 620)
        MainWindow.setStyleSheet(" \n"
                                 "  font-size: 18px;\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_data)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_5.setStyleSheet(" QPushButton#pushButton_5 {\n"
"     background-color: #EEDDFF;\n"
"  border: 1px solid #7922CC;\n"
"  border-radius: 25px;\n"
"}\n"
"QPushButton#pushButton_5:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#pushButton_5:hover {\n"
"     background-color:#FFE8DB;\n"
" }\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.del_data)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 150)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" QPushButton#pushButton {\n"
"     background-color: #EEDDFA;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.classif)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setStyleSheet(" QPushButton#pushButton_3 {\n"
"     background-color: #EEDDFF;\n"
"  border: 1px solid #7922CC;\n"
"  border-radius: 25px;\n"
"}\n"
"QPushButton#pushButton_3:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#pushButton_3:hover {\n"
"     background-color:#FFE8DB;\n"
" }\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.menu)
        self.pushButton_3.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadData()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Анализ данных по артефактам", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Удалить", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Обучающие данные", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Класс", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Цвет артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Тип артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Примеси", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Толщина стенки", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Показатель водопоглощения", None, -1))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "Текстура", None, -1))
        self.tableWidget.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("MainWindow", "Брак", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Начать классификацию", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Назад", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

