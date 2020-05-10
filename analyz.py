# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyz.ui',
# licensing of 'analyz.ui' applies.
#
# Created: Mon Mar 16 16:35:58 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import menu
import classif
import claster

class Ui_MainWindow(object):
    def closeWindow(self, MainWindow):
        MainWindow.hide()
    def openmenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openclassif(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = classif.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openclaster(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = claster.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 701, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openclassif)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openclaster)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.pushButton_3.clicked.connect(self.openmenu)
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Анализ данных по артефактам", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Классификация артефактов", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Кластеризация артефактов", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "База знаний", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Решающие правила", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Назад", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

