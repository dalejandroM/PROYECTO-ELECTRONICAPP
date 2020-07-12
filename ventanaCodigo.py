import sys
from PyQt5.QtWidgets import QDialog,QApplication
from Ui_ventanaCodigo import *
from resistencias import *

banda = "banda1"
banda1 = "black"
banda2 = "black"
banda3 = "black"
tolerancia = "gold"

class VentanaCodigoColores(QDialog):
    def __init__(self):
        super().__init__()

        self.ventana=Ui_Dialog()
        self.ventana.setupUi(self)

        self.ventana.btnCalcular.clicked.connect(self.calcular_ohm)

        self.ventana.btnBanda1.clicked.connect(self.banda1)
        self.ventana.btnBanda2.clicked.connect(self.banda2)
        self.ventana.btnBanda3.clicked.connect(self.banda3)
        self.ventana.btnTolerancia.clicked.connect(self.tolerancia)

        self.ventana.btnBlack.clicked.connect(self.black)
        self.ventana.btnBrown.clicked.connect(self.brown)
        self.ventana.btnRed.clicked.connect(self.red)
        self.ventana.btnOrange.clicked.connect(self.orange)
        self.ventana.btnYellow.clicked.connect(self.yellow)
        self.ventana.btnGreen.clicked.connect(self.green)
        self.ventana.btnBlue.clicked.connect(self.blue)
        self.ventana.btnPurple.clicked.connect(self.purple)
        self.ventana.btnGray.clicked.connect(self.gray)
        self.ventana.btnWhite.clicked.connect(self.white)
        self.ventana.btnGold.clicked.connect(self.gold)
        self.ventana.btnSilver.clicked.connect(self.silver)
        self.ventana.btnGold.setVisible(False)
        self.ventana.btnSilver.setVisible(False)

        self.show()
    
    def banda1(self):
        global banda
        banda="banda1"
        self.ventana.btnBlack.setVisible(True)
        self.ventana.btnBrown.setVisible(True)
        self.ventana.btnRed.setVisible(True)
        self.ventana.btnOrange.setVisible(True)
        self.ventana.btnYellow.setVisible(True)
        self.ventana.btnGreen.setVisible(True)
        self.ventana.btnBlue.setVisible(True)
        self.ventana.btnPurple.setVisible(True)
        self.ventana.btnGray.setVisible(True)
        self.ventana.btnWhite.setVisible(True)
        self.ventana.btnGold.setVisible(False)
        self.ventana.btnSilver.setVisible(False)


    def banda2(self):
        global banda
        banda="banda2"
        self.ventana.btnBlack.setVisible(True)
        self.ventana.btnBrown.setVisible(True)
        self.ventana.btnRed.setVisible(True)
        self.ventana.btnOrange.setVisible(True)
        self.ventana.btnYellow.setVisible(True)
        self.ventana.btnGreen.setVisible(True)
        self.ventana.btnBlue.setVisible(True)
        self.ventana.btnPurple.setVisible(True)
        self.ventana.btnGray.setVisible(True)
        self.ventana.btnWhite.setVisible(True)
        self.ventana.btnGold.setVisible(False)
        self.ventana.btnSilver.setVisible(False)

    def banda3(self):
        global banda
        banda="banda3"
        self.ventana.btnBlack.setVisible(True)
        self.ventana.btnBrown.setVisible(True)
        self.ventana.btnRed.setVisible(True)
        self.ventana.btnOrange.setVisible(True)
        self.ventana.btnYellow.setVisible(True)
        self.ventana.btnGreen.setVisible(True)
        self.ventana.btnBlue.setVisible(True)
        self.ventana.btnPurple.setVisible(True)
        self.ventana.btnGray.setVisible(True)
        self.ventana.btnWhite.setVisible(True)
        self.ventana.btnGold.setVisible(True)
        self.ventana.btnSilver.setVisible(True)

    def tolerancia(self):
        global banda
        banda="tolerancia"
        self.ventana.btnBlack.setVisible(False)
        self.ventana.btnBrown.setVisible(False)
        self.ventana.btnRed.setVisible(False)
        self.ventana.btnOrange.setVisible(False)
        self.ventana.btnYellow.setVisible(False)
        self.ventana.btnGreen.setVisible(False)
        self.ventana.btnBlue.setVisible(False)
        self.ventana.btnPurple.setVisible(False)
        self.ventana.btnGray.setVisible(False)
        self.ventana.btnWhite.setVisible(False)
        self.ventana.btnGold.setVisible(True)
        self.ventana.btnSilver.setVisible(True)

    def black(self):
        global banda1
        global banda2
        global banda3
        global tolerancia
        
        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'black\'")
            banda1="black"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'black\'")
            banda2="black"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'black\'")
            banda3="black"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'black\'")
            tolerancia="black"

    def brown(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'brown\'")
            banda1="brown"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'brown\'")
            banda2="brown"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'brown\'")
            banda3="brown"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'brown\'")
            tolerancia="brown"

    def red(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'red\'")
            banda1="red"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'red\'")
            banda2="red"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'red\'")
            banda3="red"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'red\'")
            tolerancia="red"

    def orange(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'orange\'")
            banda1="orange"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'orange\'")
            banda2="orange"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'orange\'")
            banda3="orange"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'orange\'")
            tolerancia="orange"

    def yellow(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'yellow\'")
            banda1="yellow"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'yellow\'")
            banda2="yellow"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'yellow\'")
            banda3="yellow"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'yellow\'")
            tolerancia="yellow"

    def green(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'green\'")
            banda1="green"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'green\'")
            banda2="green"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'green\'")
            banda3="green"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'green\'")
            btolerancia="green"

    def blue(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'blue\'")
            banda1="blue"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'blue\'")
            banda2="blue"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'blue\'")
            banda3="blue"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'blue\'")
            tolerancia="blue"

    def purple(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'purple\'")
            banda1="purple"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'purple\'")
            banda2="purple"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'purple\'")
            banda3="purple"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'purple\'")
            tolerancia="purple"

    def gray(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'gray\'")
            banda1="gray"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'gray\'")
            banda2="gray"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'gray\'")
            banda3="gray"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'gray\'")
            tolerancia="gray"

    def white(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:\'white\'")
            banda1="white"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:\'white\'")
            banda2="white"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:\'white\'")
            banda3="white"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:\'white\'")
            tolerancia="white"

    def gold(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
            banda1="gold"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
            banda2="gold"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
            banda3="gold"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
            tolerancia="gold"

    def silver(self):
        global banda1
        global banda2
        global banda3
        global tolerancia

        if banda == "banda1":
            self.ventana.btnBanda1.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.16 rgba(136, 136, 136, 255), stop:0.225 rgba(166, 166, 166, 255), stop:0.285 rgba(204, 204, 204, 255), stop:0.345 rgba(235, 235, 235, 255), stop:0.415 rgba(245, 245, 245, 255), stop:0.52 rgba(209, 209, 209, 255), stop:0.57 rgba(187, 187, 187, 255), stop:0.635 rgba(168, 168, 168, 255), stop:0.695 rgba(202, 202, 202, 255), stop:0.75 rgba(218, 218, 218, 255), stop:0.815 rgba(208, 208, 208, 255), stop:0.88 rgba(187, 187, 187, 255), stop:0.9375 rgba(137, 137, 137, 255), stop:1 rgba(40, 40, 40, 255))")
            banda1="silver"
        elif banda == "banda2":
            self.ventana.btnBanda2.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.16 rgba(136, 136, 136, 255), stop:0.225 rgba(166, 166, 166, 255), stop:0.285 rgba(204, 204, 204, 255), stop:0.345 rgba(235, 235, 235, 255), stop:0.415 rgba(245, 245, 245, 255), stop:0.52 rgba(209, 209, 209, 255), stop:0.57 rgba(187, 187, 187, 255), stop:0.635 rgba(168, 168, 168, 255), stop:0.695 rgba(202, 202, 202, 255), stop:0.75 rgba(218, 218, 218, 255), stop:0.815 rgba(208, 208, 208, 255), stop:0.88 rgba(187, 187, 187, 255), stop:0.9375 rgba(137, 137, 137, 255), stop:1 rgba(40, 40, 40, 255))")
            banda2="silver"
        elif banda == "banda3":
            self.ventana.btnBanda3.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.16 rgba(136, 136, 136, 255), stop:0.225 rgba(166, 166, 166, 255), stop:0.285 rgba(204, 204, 204, 255), stop:0.345 rgba(235, 235, 235, 255), stop:0.415 rgba(245, 245, 245, 255), stop:0.52 rgba(209, 209, 209, 255), stop:0.57 rgba(187, 187, 187, 255), stop:0.635 rgba(168, 168, 168, 255), stop:0.695 rgba(202, 202, 202, 255), stop:0.75 rgba(218, 218, 218, 255), stop:0.815 rgba(208, 208, 208, 255), stop:0.88 rgba(187, 187, 187, 255), stop:0.9375 rgba(137, 137, 137, 255), stop:1 rgba(40, 40, 40, 255))")
            banda3="silver"
        else:
            self.ventana.btnTolerancia.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.16 rgba(136, 136, 136, 255), stop:0.225 rgba(166, 166, 166, 255), stop:0.285 rgba(204, 204, 204, 255), stop:0.345 rgba(235, 235, 235, 255), stop:0.415 rgba(245, 245, 245, 255), stop:0.52 rgba(209, 209, 209, 255), stop:0.57 rgba(187, 187, 187, 255), stop:0.635 rgba(168, 168, 168, 255), stop:0.695 rgba(202, 202, 202, 255), stop:0.75 rgba(218, 218, 218, 255), stop:0.815 rgba(208, 208, 208, 255), stop:0.88 rgba(187, 187, 187, 255), stop:0.9375 rgba(137, 137, 137, 255), stop:1 rgba(40, 40, 40, 255))")
            tolerancia="silver"

    def calcular_ohm(self):
        resultado=""
        valBanda1 = banda1
        valBanda2 = banda2
        valBanda3 = banda3
        valTolerancia = tolerancia
        colorResistencia = [valBanda1,valBanda2,valBanda3,valTolerancia]
        resistencia = resistencia_num(colorResistencia)
        valor=calc_valor(resistencia)

        if valor[0]>=(10**9):
            ohm=valor[0]/(10**9)
            resultado="El valor es: "+str(ohm)+"GΩ ± "+str(valor[1])+"%"
        elif valor[0]>=(10**6):
            ohm=valor[0]/(10**6)
            resultado="El valor es: "+str(ohm)+"MΩ ± "+str(valor[1])+"%"
        elif valor[0]>=(10**3):
            ohm=valor[0]/(10**3)
            resultado="El valor es: "+str(ohm)+"KΩ ± "+str(valor[1])+"%"
        else:
            resultado="El valor es: "+str(valor[0])+"Ω ± "+str(valor[1])+"%"

        self.ventana.lblResultado.setText(resultado)


#if __name__ == '__main__':
    #app =QApplication(sys.argv)
    #ventanaCodigo= VentanaCodigoColores()
    #ventanaCodigo.show()
    #sys.exit(app.exec_())