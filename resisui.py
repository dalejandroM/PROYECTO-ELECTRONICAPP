# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyhon.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)



        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        Form.setStyleSheet("\n"
"background-color: rgb(255, 170, 127);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 381, 31))
        palette = QtGui.QPalette()
        
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.serie = QtWidgets.QRadioButton(Form)
        self.serie.setGeometry(QtCore.QRect(310, 60, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.serie.setFont(font)
        self.serie.setObjectName("serie")
        self.paralelo = QtWidgets.QRadioButton(Form)
        self.paralelo.setGeometry(QtCore.QRect(310, 90, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.paralelo.setFont(font)
        self.paralelo.setObjectName("paralelo")
        self.botonCalcular = QtWidgets.QPushButton(Form)
        self.botonCalcular.setGeometry(QtCore.QRect(310, 130, 75, 23))
        self.botonCalcular.setStyleSheet("background-color: rgb(0, 189, 91);")
        self.botonCalcular.setObjectName("botonCalcular")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 361, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("R1+R2+Rn...")
       
        self.resultados = QtWidgets.QLabel(Form)
        self.resultados.setGeometry(QtCore.QRect(90, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resultados.setFont(font)
        self.resultados.setText("")
        self.resultados.setObjectName("resultados")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "suma de resistencias"))
        self.label_2.setText(_translate("Form", "escriba el valor de las resistencias, separadas por +"))
        self.serie.setText(_translate("Form", "Serie"))
        self.paralelo.setText(_translate("Form", "Paralelo"))
        self.botonCalcular.setText(_translate("Form", "calcular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())