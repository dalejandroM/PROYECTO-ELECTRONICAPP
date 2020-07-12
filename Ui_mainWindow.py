# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JACP\OneDrive - Universidad Nacional de Colombia\Primer Semestre\Programacion Basica\Proyecto\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(282, 488))
        MainWindow.setMaximumSize(QtCore.QSize(282, 488))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVentana1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnVentana1.setGeometry(QtCore.QRect(10, 180, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnVentana1.setFont(font)
        self.btnVentana1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVentana1.setStyleSheet("border-image: url(:/newPrefix/boton.png);")
        self.btnVentana1.setObjectName("btnVentana1")
        self.btnVentana2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnVentana2.setGeometry(QtCore.QRect(10, 240, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.btnVentana2.setFont(font)
        self.btnVentana2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVentana2.setStyleSheet("border-image: url(:/newPrefix/boton.png);")
        self.btnVentana2.setObjectName("btnVentana2")
        self.btnVentana3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnVentana3.setGeometry(QtCore.QRect(10, 360, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.btnVentana3.setFont(font)
        self.btnVentana3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVentana3.setStyleSheet("border-image: url(:/newPrefix/boton.png);")
        self.btnVentana3.setObjectName("btnVentana3")
        self.btnVentana4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnVentana4.setGeometry(QtCore.QRect(10, 300, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.btnVentana4.setFont(font)
        self.btnVentana4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVentana4.setStyleSheet("border-image: url(:/newPrefix/boton.png);")
        self.btnVentana4.setObjectName("btnVentana4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 491))
        self.label.setStyleSheet("border-image: url(:/newPrefix/principal.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 201, 161))
        self.label_2.setStyleSheet("\n"
"border-image: url(:/newPrefix/logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.btnVentana1.raise_()
        self.btnVentana2.raise_()
        self.btnVentana3.raise_()
        self.btnVentana4.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElectronicApp"))
        self.btnVentana1.setText(_translate("MainWindow", "Codigo de colores"))
        self.btnVentana2.setText(_translate("MainWindow", "Ley Ohm"))
        self.btnVentana3.setText(_translate("MainWindow", "Suma de resistencias"))
        self.btnVentana4.setText(_translate("MainWindow", "Divisor de Tension y Corriente"))
import imagesMain
