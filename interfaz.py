import sys
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from resisui import *
from resistencias2 import *


def error(texto):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(texto)
    x = msg.exec_()
    
class ventana(QDialog):
    def __init__(self):
        super().__init__()


        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.ventana.botonCalcular.clicked.connect(self.calcular)
        self.show()
    def calcular(self):
        numeros=["0","1","2","3","4","5","6","7","8","9","+",".",","]
        paila=False
        resu=self.ventana.lineEdit.text()
        if resu=="" :
            error("No sea vago, compita, ponga algo")
            r="error"
        else :
            for i in resu:
                if i not in numeros :
                    paila=True
            if paila == True :
                error("Error¿qujeso,compa? sea serio home")
                r="error"
            else:
                print("asas")
                try:
                    lista=resu.split("+")
                    a=len(lista)
                except:
                    error("No sea mediocre, pana, coloque algo más")
                    a=0
                    r="error"
                if self.ventana.serie.isChecked()== True and a >1:
                    r=str(serie(lista))
                elif self.ventana.paralelo.isChecked()==True and a>1:
                    r=str(paralelo(lista))
                else:
                    error("Sea serio, hombe, ponga algo más")
                    r="error"
        self.ventana.resultados.setText(r)

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    #aqui debe poner lo que puso en la clase de arriba
#    ventanaCodigo = ventana()
#    ventanaCodigo.show()
#    sys.exit(app.exec_())
