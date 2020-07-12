import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow
from Ui_mainWindow import *
from ventanaCodigo import *
from interfaz import *
from launcher import launcher
from ventanaOhm import leyohm

class VentanaMain(QMainWindow):
    def __init__(self):

        super().__init__()

        self.ventana=Ui_MainWindow()
        self.ventana.setupUi(self)  
        self.ventana.btnVentana1.clicked.connect(self.abrirVentana1) 
        self.ventana.btnVentana2.clicked.connect(self.abrirVentana2) 
        self.ventana.btnVentana3.clicked.connect(self.abrirVentana3) 
        self.ventana.btnVentana4.clicked.connect(self.abrirVentana4) 
        self.show()
    
    def abrirVentana1(self):
        d = VentanaCodigoColores()
        d.show()
        d.exec_()

    def abrirVentana2(self):
        d = leyohm()
        d.show()
        d.exec_()

    def abrirVentana3(self):
        d = ventana()
        d.show()
        d.exec_()
        

    def abrirVentana4(self):
        d = launcher()
        d.show()
        d.exec_()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    ventanaPrincipal= VentanaMain()
    ventanaPrincipal.show()
    sys.exit(app.exec_())