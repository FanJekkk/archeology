# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchsome.ui',
# licensing of 'searchsome.ui' applies.
#
# Created: Sat Mar 14 21:24:26 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import search
import os
import webbrowser
from fpdf import FPDF
import sqlite3
conn = sqlite3.connect('database.db')

class Ui_Dialogsome(object):
    def openWindowtxt(self, Dialog):
        type = str(self.comboBox_3.currentText())
        water = str(self.comboBox_2.currentText())
        thickness = str(self.comboBox.currentText())
        cur = conn.cursor()
        res1 = cur.execute(
            "SELECT * from artefacts WHERE (type_id = ? and water_absorption_id = ? and thickness_id = ?) "
            "or (type_id = ? and water_absorption_id != ? and thickness_id = ?)"
            "or (type_id = ? and water_absorption_id = ? and thickness_id != ?)"
            "or (type_id = ? and water_absorption_id != ? and thickness_id != ?) ",
            (type, water, thickness, type, water, thickness, type, water, thickness,type, water, thickness,))
        dat = res1.fetchall()
        if dat:
            f = open('artefact.txt', 'w')
            for data in dat:
                f.write("Отчет по артефакту(ам) типа " + data[5]+"\n")
                f.write("\nID артефакта: " + data[2])
                f.write("\nТип артефакта: " + data[5])
                f.write("\nЦвет артефакта: " + data[4])
                f.write("\nПримеси: " + data[6])
                f.write("\nТолщина стенки: " + data[7])
                f.write("\nПоказатель водопоглощения: " + data[8])
                f.write("\nСледы брака: " + data[9])
                f.write("\nТекстура массы: " + data[10])
                f.write("\nМесто обнаружения: " + data[12]+"\n\n\n")
            f.close()
            os.startfile(r'artefact.txt')
        else:
            QMessageBox.information(QMessageBox(), 'Артефакт не найден.', 'Артефактов с таким цветом не найдено')
        cur.close()
    def openWindow(self, Dialog):
        type = str(self.comboBox_3.currentText())
        water = str(self.comboBox_2.currentText())
        thickness = str(self.comboBox.currentText())
        cur = conn.cursor()
        res1 = cur.execute("SELECT * from artefacts WHERE (type_id = ? and water_absorption_id = ? and thickness_id = ?) "
                           "union select * from artefact where  (type_id = ? and water_absorption_id != ? and thickness_id = ?)"
                           "union select * from artefact where (type_id = ? and water_absorption_id = ? and thickness_id != ?)"
                           "union select * from artefact where (type_id = ? and water_absorption_id != ? and thickness_id != ?) ",
                           (type, water,thickness,type, water,thickness,type, water,thickness,type, water,thickness,))
        dat = res1.fetchall()
        if dat:
            pdf = FPDF()
            for data in dat:
                pdf.add_page()
                pdf.add_font('sysfont', '', r"c:\WINDOWS\Fonts\arial.ttf", uni=True)
                pdf.set_font('sysfont', '', 18)
                pdf.cell(200, 40, txt="Отчет по артефакту(ам) типа " + data[5], ln=1, align="C")
                pdf.image(data[11], x=70, y=50, w=80, h=80)
                pdf.set_font('sysfont', '', 14)
                pdf.line(40, 40, 180, 40)
                pdf.ln(90)
                pdf.cell(20, 15, txt="ID артефакта: " + data[2], ln=1, align="L")
                pdf.cell(20, 15, txt="Тип артефакта: " + data[5], ln=1, align="L")
                pdf.cell(20, 15, txt="Цвет артефакта: " + data[4], ln=1, align="L")
                pdf.cell(20, 15, txt="Примеси: " + data[6], ln=1, align="L")
                pdf.cell(20, 15, txt="Толщина стенки: " + data[7], ln=1, align="L")
                pdf.cell(20, 15, txt="Показатель водопоглощения: " + data[8], ln=1, align="L")
                pdf.cell(20, 15, txt="Следы брака: " + data[9], ln=1, align="L")
                pdf.cell(20, 15, txt="Текстура массы: " + data[10], ln=1, align="L")
            pdf.output("artefact.pdf", "F")
            os.startfile(r'artefact.pdf')

        else:
            QMessageBox.information(QMessageBox(), 'Артефакт не найден.', 'Артефактов с такими признаками не найдено')
        cur.close()

    def closeWindow(self, Dialog):
        Dialog.hide()

    def search(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = search.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialogsome):
        Dialogsome.setObjectName("Dialogsome")
        Dialogsome.resize(600, 500)
        Dialogsome.setStyleSheet(" \n"
                                        "  font-size: 18px;\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialogsome)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialogsome)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_3 = QtWidgets.QComboBox(Dialogsome)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 60))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setStyleSheet(" QComboBox#comboBox_3 {\n"
                                      "  background-color: #EEDDFF;\n"
                                      "  border: 1px solid grey;\n"
                                      "  font-size: 18px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:pressed {\n"
                                      "     background-color: rgb(224, 0, 0);     \n"
                                      " }\n"
                                      "")
        cur = conn.cursor()
        cur.execute("SELECT * FROM types")
        for row in cur:
            self.comboBox_3.addItem(str(row[1]))
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(Dialogsome)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 60))
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Показатель водопоглащения")
        cur = conn.cursor()
        cur.execute("SELECT * FROM water_absorption")
        for row in cur:
            self.comboBox_2.addItem(str(row[1]))
        self.verticalLayout.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(Dialogsome)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 60))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Толщина стенки")
        cur = conn.cursor()
        cur.execute("SELECT * FROM thickness")
        for row in cur:
            self.comboBox.addItem(str(row[1]))
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(Dialogsome)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setStyleSheet(" QPushButton#pushButton {\n"
                                        "  background-color: #EEDDFF;\n"
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
        self.pushButton.clicked.connect(lambda: self.openWindow(Dialogsome))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(Dialogsome)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_3.setStyleSheet(" QPushButton#pushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.clicked.connect(lambda: self.openWindowtxt(Dialogsome))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(Dialogsome)
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
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(Dialogsome))
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialogsome)
        QtCore.QMetaObject.connectSlotsByName(Dialogsome)

    def retranslateUi(self, Dialogsome):
        Dialogsome.setWindowTitle(QtWidgets.QApplication.translate("Dialogsome", "Поиск артефакта по нескольким признакам", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialogsome", "Введите признаки для поиска артефакта", None, -1))

        self.pushButton.setText(QtWidgets.QApplication.translate("Dialogsome", "Открыть в pdf", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Dialogsome", "Открыть в txt", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialogsome", "Отмена", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogsome = QtWidgets.QDialog()
    ui = Ui_Dialogsome()
    ui.setupUi(Dialogsome)
    Dialogsome.show()
    sys.exit(app.exec_())

