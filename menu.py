# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui',
# licensing of 'menu.ui' applies.
#
# Created: Sat Mar 14 16:23:15 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import dbarch
import search
import analyz
import sqlite3

conn = sqlite3.connect("database.db")

class Ui_MenuWindow(object):
    def closeWindow(self, MenuWindow):
        MenuWindow.hide()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dbarch.Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def opensearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = search.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def analyze(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = analyz.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(1000, 620)
        MenuWindow.setMinimumSize(QtCore.QSize(1000, 620))
        MenuWindow.setMaximumSize(QtCore.QSize(1000, 620))
        MenuWindow.setStyleSheet(" \n"
                                        "  font-size: 18px;\n")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setToolTipDuration(2)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(" QPushButton#pushButton_2 {\n"
                                        "     background-color: #EEDDFF;\n"
                                        "  border: 1px solid #7922CC;\n"
                                        "  border-radius: 25px;\n"
                                        "background-image: url(:/images/image/unn.png);\n"
                                        "background-position: center; /* Положение фона */\n"
                                        "background-repeat: no-repeat; \n"      
                                        "text-align: bottom;"
                                        "}\n"
                                        "QPushButton#pushButton_2:pressed {\n"
                                        "     background-color: rgb(224, 0, 0);     \n"
                                        " }\n"
                                        " QPushButton#pushButton_2:hover {\n"
                                        "     background-color:#FFE8DB;\n"
                                        " }\n"
                                        "")

        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setIconSize(QtCore.QSize(130, 160))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(MenuWindow))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(250, 250))
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(" QPushButton#pushButton_3 {\n"
                                        "     background-color: #EEDDFF;\n"
                                        "  border: 1px solid #7922CC;\n"
                                        "  border-radius: 25px;\n"
                                        "background-image: url(:/images/image/search.png);\n"
                                        "background-position: center; /* Положение фона */\n"
                                        "background-repeat: no-repeat; \n"
                                        "text-align: bottom;"
                                        "}\n"
                                        "QPushButton#pushButton_3:pressed {\n"
                                        "     background-color: rgb(224, 0, 0);     \n"
                                        " }\n"
                                        " QPushButton#pushButton_3:hover {\n"
                                        "     background-color:#FFE8DB;\n"
                                        " }\n"
                                        "")
        self.pushButton_3.setIconSize(QtCore.QSize(160, 200))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.opensearch)
        self.pushButton_3.clicked.connect(lambda: self.closeWindow(MenuWindow))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 250))
        self.pushButton.setStyleSheet(" QPushButton#pushButton {\n"
                                        "     background-color: #EEDDFF;\n"
                                        "  border: 1px solid #7922CC;\n"
                                        "  border-radius: 25px;\n"
                                        "background-image: url(:/images/image/analytics.png);\n"
                                        "background-position: center; /* Положение фона */\n"
                                        "background-repeat: no-repeat; \n"
                                        "text-align: bottom;"
                                        "}\n"
                                        "QPushButton#pushButton:pressed {\n"
                                        "     background-color: rgb(224, 0, 0);     \n"
                                        " }\n"
                                        " QPushButton#pushButton:hover {\n"
                                        "     background-color:#FFE8DB;\n"
                                        " }\n"
                                        "")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(200, 240))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.analyze)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MenuWindow))
        self.horizontalLayout.addWidget(self.pushButton)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QtWidgets.QApplication.translate("MenuWindow", "Главное меню", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MenuWindow", "Пополнение/\nредактирование "
                                                                                 "базы", None, -1))
        self.pushButton_2.setToolTip(
            QtWidgets.QApplication.translate("MenuWindow", "Пополнение/редактирование базы",
                                             None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MenuWindow", "Поиск по базе", None, -1))
        self.pushButton_3.setToolTip(
            QtWidgets.QApplication.translate("MenuWindow", "<html><head/><body><p>Поиск по базе</p></body></html>",
                                             None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MenuWindow", "Анализ данных", None, -1))
        self.pushButton.setToolTip(
            QtWidgets.QApplication.translate("MenuWindow", "<html><head/><body><p>Анализ данных</p></body></html>",
                                             None, -1))


import icont

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())

