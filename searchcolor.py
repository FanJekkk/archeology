# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchcolor.ui',
# licensing of 'searchcolor.ui' applies.
#
# Created: Sat Mar 14 21:02:10 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import search
import os
import fpdf
import webbrowser
from fpdf import FPDF
from PIL import ImageFont
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import sys
import locale
import io


import sqlite3
conn = sqlite3.connect('database.db')

class Ui_Dialogcolor(object):
    def openWindowtxt(self, Dialogcolor):
        searchrol = str(self.comboBox.currentText())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE color_id=?", (searchrol,))
        dat = cur.fetchall()
        if dat:
            f = open('artefact.txt', 'w')
            for data in dat:
                f.write("Отчет по артефакту, где цвет " + data[4]+"\n")
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

    def openWindow(self, Dialogcolor):
        searchrol = str(self.comboBox.currentText())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE color_id=?", (searchrol,))
        dat = cur.fetchall()
        if dat:
            pdf = FPDF()

            for data in dat:
                pdf.add_page()
                pdf.add_font('sysfont', '', r"c:\WINDOWS\Fonts\arial.ttf", uni=True)
                pdf.set_font('sysfont', '', 18)
                pdf.cell(200, 40, txt="Отчет по артефакту, где цвет " + data[4], ln=1, align="C")
                pdf.set_font('sysfont', '', 14)
                pdf.image(data[11],x=70, y=50, w=80, h=80)
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
            QMessageBox.information(QMessageBox(), 'Артефакт не найден.', 'Артефактов с таким цветом не найдено')
        cur.close()

    def closeWindow(self, Dialog):
        Dialog.hide()

    def search(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = search.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialogcolor):
        Dialogcolor.setObjectName("Dialogcolor")
        Dialogcolor.resize(600, 400)
        Dialogcolor.setStyleSheet(" \n"
                                        "  font-size: 18px;\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialogcolor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialogcolor)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Dialogcolor)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 60))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        cur = conn.cursor()
        cur.execute("SELECT * FROM colors")
        for row in cur:
            self.comboBox.addItem(str(row[1]))
        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QtWidgets.QPushButton(Dialogcolor)
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
        self.pushButton.clicked.connect(lambda: self.openWindow(Dialogcolor))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(Dialogcolor)
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
        self.pushButton_3.clicked.connect(lambda: self.openWindowtxt(Dialogcolor))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(Dialogcolor)
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
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(Dialogcolor))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.retranslateUi(Dialogcolor)
        QtCore.QMetaObject.connectSlotsByName(Dialogcolor)

    def retranslateUi(self, Dialogcolor):
        Dialogcolor.setWindowTitle(QtWidgets.QApplication.translate("Dialogcolor", "Поиск по цвету артефакта", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialogcolor", "Выберите цвет артефакта", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialogcolor", "Открыть в pdf", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Dialogcolor", "Открыть в txt", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialogcolor", "Отмена", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogcolor = QtWidgets.QDialog()
    ui = Ui_Dialogcolor()
    ui.setupUi(Dialogcolor)
    Dialogcolor.show()
    sys.exit(app.exec_())

