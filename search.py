# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui',
# licensing of 'search.ui' applies.
#
# Created: Sat Mar 14 17:53:14 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import menu
import searchname
import searchcolor
import searchsome

class Ui_MainWindow(object):
    def closeWindow(self, MenuWindow):
        MenuWindow.hide()
    def searchcolor(self):
        self.window = QtWidgets.QDialog()
        self.ui = searchcolor.Ui_Dialogcolor()
        self.ui.setupUi(self.window)
        self.window.show()
    def searchname(self):
        self.window = QtWidgets.QDialog()
        self.ui = searchname.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def searchsome(self):
        self.window = QtWidgets.QDialog()
        self.ui = searchsome.Ui_Dialogsome()
        self.ui.setupUi(self.window)
        self.window.show()
    def openmenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 620)
        MainWindow.setStyleSheet(" \n"
                                  "  font-size: 18px;\n")
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        MainWindow.setMinimumSize(QtCore.QSize(1000, 620))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 250))
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
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.searchname)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 250))
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
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.searchcolor)
        self.pushButton_3.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 250))
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
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchsome)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
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
        self.pushButton_4.clicked.connect(self.openmenu)
        self.pushButton_4.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Поиск в базе", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Поиск по ID артефакта", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Поиск по цвету", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Поиск по нескольким\n"
" признакам", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Назад", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

