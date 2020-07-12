# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ley de ohm.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator, QIcon
from PyQt5.QtCore import QRegExp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 423)
        MainWindow.setMinimumSize(604,423)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.resiscaja = QtWidgets.QLineEdit(self.centralwidget)
        self.resiscaja.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.resiscaja.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resiscaja.setObjectName("resiscaja")
        self.resiscaja.setValidator(QRegExpValidator(QRegExp("[0-9]*\.?\d*")))


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.corrientecaja = QtWidgets.QLineEdit(self.centralwidget)
        self.corrientecaja.setGeometry(QtCore.QRect(120, 130, 101, 31))
        self.corrientecaja.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.corrientecaja.setObjectName("corrientecaja")
        self.corrientecaja.setValidator(QRegExpValidator(QRegExp("\d+\.?\d*")))
        self.potenciacaja = QtWidgets.QLineEdit(self.centralwidget)
        self.potenciacaja.setGeometry(QtCore.QRect(120, 170, 101, 31))
        self.potenciacaja.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.potenciacaja.setObjectName("potenciacaja")
        self.potenciacaja.setValidator(QRegExpValidator(QRegExp("\d+\.?\d*")))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(120, 290, 131, 31))
        self.resultado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 210, 241, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"font: 8pt \"MS Reference Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(130, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.boton.setFont(font)
        self.boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton.setStyleSheet("background-color: rgb(149, 149, 223);")
        self.boton.setObjectName("boton")
        self.voltacaja = QtWidgets.QLineEdit(self.centralwidget)
        self.voltacaja.setGeometry(QtCore.QRect(120, 210, 101, 31))
        self.voltacaja.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltacaja.setObjectName("voltacaja")
        self.voltacaja.setValidator(QRegExpValidator(QRegExp("\d+\.?\d*")))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.voltacheck = QtWidgets.QRadioButton(self.centralwidget)
        self.voltacheck.setGeometry(QtCore.QRect(290, 100, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.voltacheck.setFont(font)
        self.voltacheck.setObjectName("voltacheck")
        self.resischeck = QtWidgets.QRadioButton(self.centralwidget)
        self.resischeck.setGeometry(QtCore.QRect(390, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.resischeck.setFont(font)
        self.resischeck.setObjectName("resischeck")
        self.potencheck = QtWidgets.QRadioButton(self.centralwidget)
        self.potencheck.setGeometry(QtCore.QRect(390, 100, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.potencheck.setFont(font)
        self.potencheck.setObjectName("potencheck")
        self.corrientecheck = QtWidgets.QRadioButton(self.centralwidget)
        self.corrientecheck.setGeometry(QtCore.QRect(290, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.corrientecheck.setFont(font)
        self.corrientecheck.setObjectName("corrientecheck")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 70, 261, 111))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 581, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.groupBox.raise_()
        self.label.raise_()
        self.resiscaja.raise_()
        self.label_3.raise_()
        self.corrientecaja.raise_()
        self.potenciacaja.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.resultado.raise_()
        self.label_6.raise_()
        self.boton.raise_()
        self.voltacaja.raise_()
        self.label_7.raise_()
        self.voltacheck.raise_()
        self.resischeck.raise_()
        self.potencheck.raise_()
        self.corrientecheck.raise_()
        self.line.raise_()
        self.label_8.raise_()
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculadora"))
        self.label.setText(_translate("MainWindow", "Calculadora de ley de ohm"))
        self.label_3.setText(_translate("MainWindow", "Corriente"))
        self.label_4.setText(_translate("MainWindow", "Potencia"))
        self.label_5.setText(_translate("MainWindow", "Resultado"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Ingrese los valores y seleccione el </span></p><p><span style=\" font-weight:600;\">elemento a calcular, se necesitan </span></p><p><span style=\" font-weight:600;\">minimo dos</span></p></body></html>"))
        self.boton.setText(_translate("MainWindow", "calcular"))
        self.label_7.setText(_translate("MainWindow", "Voltaje"))
        self.voltacheck.setText(_translate("MainWindow", "Voltaje"))
        self.resischeck.setText(_translate("MainWindow", "Resistencia"))
        self.potencheck.setText(_translate("MainWindow", "Potencia"))
        self.corrientecheck.setText(_translate("MainWindow", "Corriente"))
        self.groupBox.setTitle(_translate("MainWindow", "Escoja una"))
        self.label_8.setText(_translate("MainWindow", "Resistencia"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
