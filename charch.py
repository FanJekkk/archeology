# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charch.ui',
# licensing of 'charch.ui' applies.
#
# Created: Sat Mar 14 17:20:48 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import dbarch
from PyQt5.QtWidgets import *
from change import *
import webbrowser
import sqlite3
conn = sqlite3.connect('./database.db')

class Ui_Dialog1(QDialog):
    def chooseImage(self):
        fname,_ = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image file (*.jpg)')
        if fname:
            self.lineEdit_4.setText(fname)
            pixmap = QtGui.QPixmap(fname)
            pixmap = pixmap.scaledToWidth(300)
            self.imagelabel.setPixmap(pixmap)
    def convertImage(self):
        fname = self.lineEdit_4.text()
        if fname != '':
            with open(fname, 'rb') as file:
                picture = file.read()
                return picture
    def closeWindow(self, Dialog1):
        Dialog1.hide()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dbarch.Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def changeInf(self, Dialog1):
        id_artefact_last = str(self.lineEdit.text())
        id_artefact_new = str(self.lineEdit_3.text())
        local_last = str(self.lineEdit_5.text())
        local_new = str(self.lineEdit_6.text())
        name = str(self.lineEdit_2.text())
        cur = conn.cursor()
        cur.execute("SELECT * from artefacts WHERE id_artefact=?", (id_artefact_new,))
        data = cur.fetchall()
        picture = self.convertImage()
        color_id = str(self.comboBox_4.currentText())
        type_id = str(self.comboBox_3.currentText())
        admixture_id = str(self.comboBox.currentText())
        thickness_id = str(self.comboBox_2.currentText())
        water_absorption_id = str(self.comboBox_5.currentText())
        defect_id = str(self.comboBox_6.currentText())
        texture_id = str(self.comboBox_7.currentText())
        if data:
            self.lineEdit_3.setText("")
            self.lineEdit_3.setPlaceholderText("Такой ID уже существует, введите другой")
        elif id_artefact_new == '' and self.lineEdit_4.text() != '' and local_new != '':
            id_artefact_new = id_artefact_last
            cur.execute("UPDATE artefacts SET picture = ?, id_artefact = ?, name = ?, color_id = ?, type_id = ?, admixture_id = ?,"
                        "thickness_id = ?, water_absorption_id = ?, defect_id = ?, texture_id = ?, local = ? WHERE id_artefact = ?",
                        (picture, id_artefact_new, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                         defect_id, texture_id, local_new, id_artefact_last))
            conn.commit()
            QMessageBox.information(QMessageBox(), 'Успешно!', 'Артефакт изменен')
            Dialog1.hide()
            self.openWindow()
        elif id_artefact_new == '' and self.lineEdit_4.text() == '' and local_new == '' :
            id_artefact_new = id_artefact_last
            local_new = local_last
            cur.execute("UPDATE artefacts SET id_artefact = ?, name = ?,  color_id = ?, type_id = ?, admixture_id = ?, "
                        "thickness_id = ?, water_absorption_id = ?, defect_id = ?, texture_id = ?, local = ? WHERE id_artefact = ?",
                        (id_artefact_new, name,  color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                         defect_id, texture_id, local_new, id_artefact_last))
            conn.commit()
            QMessageBox.information(QMessageBox(), 'Успешно!', 'Артефакт изменен')
            Dialog1.hide()
            self.openWindow()
        elif id_artefact_new == '' and self.lineEdit_4.text() == '' and local_new != '':
            id_artefact_new = id_artefact_last
            cur.execute("UPDATE artefacts SET id_artefact = ?, name = ?,  color_id = ?, type_id = ?, admixture_id = ?, "
                        "thickness_id = ?, water_absorption_id = ?, defect_id = ?, texture_id = ?, local = ? WHERE id_artefact = ?",
                        (id_artefact_new, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                         defect_id, texture_id, local_new, id_artefact_last))
            conn.commit()
            QMessageBox.information(QMessageBox(), 'Успешно!', 'Артефакт изменен')
            Dialog1.hide()
            self.openWindow()
        elif id_artefact_new == '' and self.lineEdit_4.text() != '' and local_new == '':
            id_artefact_new = id_artefact_last
            local_new = local_last
            cur.execute("UPDATE artefacts SET id_artefact = ?, name = ?,  color_id = ?, type_id = ?, admixture_id = ?, "
                        "thickness_id = ?, water_absorption_id = ?, defect_id = ?, texture_id = ?, local = ? WHERE id_artefact = ?",
                        (id_artefact_new, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                         defect_id, texture_id, local_new, id_artefact_last))
            conn.commit()
            QMessageBox.information(QMessageBox(), 'Успешно!', 'Артефакт изменен')
            Dialog1.hide()
            self.openWindow()
        else:
            cur.execute("UPDATE artefacts SET picture = ?, id_artefact = ?, name = ?,  color_id = ?, type_id = ?, admixture_id = ?, "
                        "thickness_id = ?, water_absorption_id = ?, defect_id = ?, texture_id = ?, local = ? WHERE id_artefact = ?",
                        (picture, id_artefact_new, name,  color_id, type_id, admixture_id, thickness_id, water_absorption_id,
                         defect_id, texture_id, local_new, id_artefact_last) )
            conn.commit()
            QMessageBox.information(QMessageBox(), 'Успешно!', 'Артефакт изменен')
            Dialog1.hide()
            self.openWindow()
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(429, 700)
        Dialog1.setMinimumSize(QtCore.QSize(700, 700))
        Dialog1.setMaximumSize(QtCore.QSize(700, 700))
        Dialog1.setStyleSheet(" \n"
                             "  font-size: 18px;\n")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setAcceptDrops(True)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox_4 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox = QtWidgets.QComboBox(Dialog1)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.comboBox_5 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setMaxVisibleItems(10)
        self.comboBox_5.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_6.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setMaxVisibleItems(10)
        self.comboBox_6.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_6.setObjectName("comboBox_6")
        self.verticalLayout.addWidget(self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(Dialog1)
        self.comboBox_7.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setMaxVisibleItems(10)
        self.comboBox_7.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_7.setObjectName("comboBox_7")
        self.verticalLayout.addWidget(self.comboBox_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_5.setAcceptDrops(True)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_6.setAcceptDrops(True)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.imagelabel = QtWidgets.QLabel(Dialog1)
        self.imagelabel.setGeometry(QtCore.QRect(0,0,200,200))
        self.imagelabel.setText("")
        self.horizontalLayout.addWidget(self.imagelabel)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.clicked.connect(self.chooseImage)

        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(Dialog1)
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
        self.pushButton.clicked.connect(lambda: self.changeInf(Dialog1))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog1)
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
        self.pushButton_2.clicked.connect(lambda: self.closeWindow(Dialog1))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(QtWidgets.QApplication.translate("Dialog1", "Изменение артефакта", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Dialog1", "ID артефакта", None, -1))
        self.lineEdit_3.setPlaceholderText(QtWidgets.QApplication.translate("Dialog1", "Введите новый ID артефакта, если необходимо", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("Dialog1", "Часть сосуда", None, -1))
        self.comboBox_3.setCurrentText(QtWidgets.QApplication.translate("Dialog1", "Удлиненная", None, -1))
        self.comboBox_3.setItemText(0, QtWidgets.QApplication.translate("Dialog1", "Удлиненная", None, -1))
        self.comboBox_3.setItemText(1, QtWidgets.QApplication.translate("Dialog1", "Закргуленная", None, -1))
        self.comboBox.setCurrentText(QtWidgets.QApplication.translate("Dialog1", "Черный", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("Dialog1", "Черный", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("Dialog1", "Красный", None, -1))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("Dialog1", "Серый", None, -1))
        self.comboBox.setItemText(5, QtWidgets.QApplication.translate("Dialog1", "Белый", None, -1))
        self.comboBox.setItemText(6, QtWidgets.QApplication.translate("Dialog1", "Синий", None, -1))
        self.comboBox_2.setCurrentText(QtWidgets.QApplication.translate("Dialog1", "1", None, -1))
        self.comboBox_2.setItemText(7, QtWidgets.QApplication.translate("Dialog1", "1", None, -1))
        self.comboBox_2.setItemText(8, QtWidgets.QApplication.translate("Dialog1", "1,5", None, -1))
        self.comboBox_2.setItemText(9, QtWidgets.QApplication.translate("Dialog1", "3", None, -1))
        self.comboBox_2.setItemText(10, QtWidgets.QApplication.translate("Dialog1", "4", None, -1))
        self.lineEdit_6.setPlaceholderText(QtWidgets.QApplication.translate("Dialog1", "Введите новое место нахождения, если необходимо", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Выбор картинки", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog1", "ОК", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog1", "Отмена", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

