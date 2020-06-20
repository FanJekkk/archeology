# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classif.ui',
# licensing of 'classif.ui' applies.
#
# Created: Mon Jun  1 11:59:17 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
import analyz
from keras.utils.np_utils import to_categorical
conn = sqlite3.connect('database.db')

class Ui_MainWindow(object):
    def closeWindow(self, MainWindow):
        MainWindow.hide()
    def analyz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = analyz.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def classification(self):
        df = pd.read_sql_query(
            "SELECT color_id, type_id, admixture_id, thickness_id, water_absorption_id, texture_id, defect_id, classes" \
            " FROM train_artefacts", conn)
        df['color_id'] = pd.Categorical(df['color_id'])
        df['color_id'] = df.color_id.cat.codes
        df['type_id'] = pd.Categorical(df['type_id'])
        df['type_id'] = df.type_id.cat.codes
        df['admixture_id'] = pd.Categorical(df['admixture_id'])
        df['admixture_id'] = df.admixture_id.cat.codes
        df['thickness_id'] = pd.Categorical(df['thickness_id'])
        df['thickness_id'] = df.thickness_id.cat.codes
        df['water_absorption_id'] = pd.Categorical(df['water_absorption_id'])
        df['water_absorption_id'] = df.water_absorption_id.cat.codes
        df['texture_id'] = pd.Categorical(df['texture_id'])
        df['texture_id'] = df.texture_id.cat.codes
        df['defect_id'] = pd.Categorical(df['defect_id'])
        df['defect_id'] = df.defect_id.cat.codes
        df0 = pd.read_sql_query(
            "SELECT color_id, type_id, admixture_id, thickness_id, water_absorption_id, texture_id, defect_id, classes " \
            " FROM artefacts", conn)
        df0['color_id'] = pd.Categorical(df0['color_id'])
        df0['color_id'] = df0.color_id.cat.codes
        df0['type_id'] = pd.Categorical(df0['type_id'])
        df0['type_id'] = df0.type_id.cat.codes
        df0['admixture_id'] = pd.Categorical(df0['admixture_id'])
        df0['admixture_id'] = df0.admixture_id.cat.codes
        df0['thickness_id'] = pd.Categorical(df0['thickness_id'])
        df0['thickness_id'] = df0.thickness_id.cat.codes
        df0['water_absorption_id'] = pd.Categorical(df0['water_absorption_id'])
        df0['water_absorption_id'] = df0.water_absorption_id.cat.codes
        df0['texture_id'] = pd.Categorical(df0['texture_id'])
        df0['texture_id'] = df0.texture_id.cat.codes
        df0['defect_id'] = pd.Categorical(df0['defect_id'])
        df0['defect_id'] = df0.defect_id.cat.codes
        X1 = df0.iloc[:, 0:7].values
        df = df.dropna(how='any')
        #выбираем признаки классификации артефактов
        X = df.iloc[:, 0:7].values
        Y = df.iloc[:, 7].values
        sc = StandardScaler()
        X = sc.fit_transform(X)
        encoder = LabelEncoder()
        encoder.fit(Y)
        encoded_Y = encoder.transform(Y)
        # convert integers to dummy variables (i.e. one hot encoded)
        dummy_y = to_categorical(encoded_Y)
        X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size=0.4)

        model = Sequential()
        model.add(Dense(50, input_dim=7, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(y_train.shape[1], activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=200, batch_size=64)
        y_pred = model.predict(X_test)
        # Converting predictions to label
        pred = list()
        for i in range(len(y_pred)):
            pred.append(np.argmax(y_pred[i]))
        # Converting one hot encoded test label to label
        test = list()
        for i in range(len(y_test)):
            test.append(np.argmax(y_test[i]))
        a = accuracy_score(pred, test)
        history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200, batch_size=64)
        y_prob = model.predict(X1)
        y_classes = y_prob.argmax(axis=1)
        df2 = pd.read_sql_query(
            "SELECT classes, id_artefact, name, color_id, type_id, admixture_id, thickness_id, water_absorption_id, defect_id, texture_id, local " \
            " FROM artefacts", conn)
        df3 = pd.DataFrame({'classes': np.array(y_classes)})
        L1 = pd.DataFrame(np.array(y_classes))
        df2['classes'] = L1
        self.tableWidget.setColumnCount(len(df2.columns))
        self.tableWidget.setRowCount(len(df2.index))
        for i in range(len(df2.index)):
            for j in range(len(df2.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df2.iat[i, j])))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 620)
        MainWindow.setStyleSheet(" \n"
                                 "  font-size: 18px;\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.verticalLayout.addWidget(self.tableWidget)
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
        self.pushButton.clicked.connect(self.analyz)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.classification()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Классификация", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Результаты классификации", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Класс", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "ID артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Название", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Цвет артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Тип артефакта", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Примеси", None, -1))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "Толщина стенки", None, -1))
        self.tableWidget.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("MainWindow", "Показатель водопоглощения", None, -1))
        self.tableWidget.horizontalHeaderItem(8).setText(QtWidgets.QApplication.translate("MainWindow", "Брак", None, -1))
        self.tableWidget.horizontalHeaderItem(9).setText(QtWidgets.QApplication.translate("MainWindow", "Текстура", None, -1))
        self.tableWidget.horizontalHeaderItem(10).setText(QtWidgets.QApplication.translate("MainWindow", "Место обнаружения", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Назад", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

