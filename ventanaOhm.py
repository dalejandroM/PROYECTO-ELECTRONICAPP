import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from ventanaui import *
from leyde import *



def error(texto):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(texto)
    x = msg.exec_()

    
class leyohm(QDialog):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)

        self.ventana.boton.clicked.connect(self.calcular)

        self.show()



    def calcular(self):
        contadordenone=0
        resis = self.ventana.resiscaja.text()

        if resis == "":
            resis=None
            contadordenone+=1
        else:
            resis = float(resis)

        corient = self.ventana.corrientecaja.text()
        if corient == "":
            corient=None
            contadordenone += 1
        else:
            corient = float(corient)
        poten = self.ventana.potenciacaja.text()
        if poten == "":
            poten=None
            contadordenone += 1
        else:
            poten = float(poten)
        volta = self.ventana.voltacaja.text()
        if volta == "":
            volta=None
            contadordenone += 1
        else:
            volta = float(volta)

        if contadordenone>=3:
            error("Error datos insuficicentes")
            valor=""
        else:
            if self.ventana.voltacheck.isChecked() == True:
                try:
                    valor = str(voltaje(resis, corient, poten))
                except:
                    error("Error ya pusiste el valor del voltaje")
                    valor = ""
            elif self.ventana.corrientecheck.isChecked()==True:
                try:
                    valor = str(amperaje(resis, volta, poten))
                except:
                    error("Error ya pusiste el valor de la corriente")
                    valor=""
            elif self.ventana.resischeck.isChecked()==True:
                try:
                    valor = str(resistencia(corient,volta,poten))
                except:
                    error("Error ya pusiste el valor de la resistencia")
                    valor=""
            elif self.ventana.potencheck.isChecked()==True:
                try:
                    valor=str(potencia(resis,corient,volta))
                except:
                    error("Error ya pusiste el valor de la potencia")
                    valor=""
            else:
                error("Error selecciona algo")
                valor=""
        self.ventana.resultado.setText(valor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaCodigo = leyohm()
    ventanaCodigo.show()
    sys.exit(app.exec_())
