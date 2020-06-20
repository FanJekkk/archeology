# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbarch.ui',
# licensing of 'dbarch.ui' applies.
#
# Created: Sun Apr 26 13:52:19 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import add
import change
import delete
import menu
import sqlite3
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import pandas
from keras.models import Sequential
from keras.layers import Dense
conn = sqlite3.connect('database.db')

class Ui_OtherWindow(object):
    def loadData(self):
        query = "SELECT picture, id_artefact, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id, defect_id, texture_id, local " \
                " FROM artefacts"
        res = conn.cursor().execute(query)
        cur = conn.cursor()
        query1 = "SELECT id_artefact, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id, defect_id, texture_id, local " \
                " FROM artefacts"
        ras = cur.execute(query1)
        rows = cur.fetchall()
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = str(data)
                if (column_number == 0):
                    item = self.getImageLabel(data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                self.tableWidget.verticalHeader().setDefaultSectionSize(180)
    def getImageLabel(self, image):
        imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel

    def closeWindow(self, OtherWindow):
        OtherWindow.hide()

    def add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = add.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def change(self):
        self.window = QtWidgets.QDialog()
        self.ui = change.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def delete(self):
        self.window = QtWidgets.QDialog()
        self.ui = delete.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setWindowModality(QtCore.Qt.NonModal)
        OtherWindow.resize(1000, 620)
        OtherWindow.setStyleSheet(" \n"
                                        "  font-size: 18px;\n")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)
        self.pushButton.clicked.connect(lambda: self.closeWindow(OtherWindow))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(2000, 16777215))
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
        self.pushButton_2.clicked.connect(self.change)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(OtherWindow))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
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
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(lambda: self.closeWindow(OtherWindow))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_4.setStyleSheet(" QPushButton#pushButton_4 {\n"
"     background-color: #EEDDFF;\n"
"  border: 1px solid #7922CC;\n"
"  border-radius: 25px;\n"
"}\n"
"QPushButton#pushButton_4:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#pushButton_4:hover {\n"
"     background-color:#FFE8DB;\n"
" }\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.menu)
        self.pushButton_4.clicked.connect(lambda: self.closeWindow(OtherWindow))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet(" QTableWidget {\n"
                                        "     font-size: 24px;\n"
                                        "}\n")
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
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(8, 200)
        self.tableWidget.setColumnWidth(9, 200)
        self.tableWidget.setColumnWidth(10, 200)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(OtherWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(OtherWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
        self.loadData()

    def retranslateUi(self, OtherWindow):
        OtherWindow.setWindowTitle(QtWidgets.QApplication.translate("OtherWindow", "База данных по артефактам", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("OtherWindow", "Добавить", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("OtherWindow", "Изменить", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("OtherWindow", "Удалить", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("OtherWindow", "Назад", None, -1))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("OtherWindow", "Фото", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("OtherWindow", "ID артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("OtherWindow", "Часть сосуда", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("OtherWindow", "Цвет", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("OtherWindow", "Тип артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("OtherWindow", "Примеси", None, -1))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("OtherWindow", "Толщина", None, -1))
        self.tableWidget.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("OtherWindow", "Водопоглощение", None, -1))
        self.tableWidget.horizontalHeaderItem(8).setText(QtWidgets.QApplication.translate("OtherWindow", "Брак", None, -1))
        self.tableWidget.horizontalHeaderItem(9).setText(QtWidgets.QApplication.translate("OtherWindow", "Текстура массы", None, -1))
        self.tableWidget.horizontalHeaderItem(10).setText(QtWidgets.QApplication.translate("OtherWindow", "Место нахождения", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("OtherWindow", "Меню", None, -1))
        self.action.setText(QtWidgets.QApplication.translate("OtherWindow", "Поиск по базе", None, -1))
        self.action_2.setText(QtWidgets.QApplication.translate("OtherWindow", "Анализ артефактов", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

