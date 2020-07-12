from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from funciones import *
from UI import *
import sys



def error(texto):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(texto)
    x = msg.exec_()
    sonido()
    


class launcher(QDialog):
    def __init__(self):
        super().__init__()

        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.ventana.btnv.clicked.connect(self.calculadoraTension)
        self.ventana.btni.clicked.connect(self.calculadoraCorriente)
        self.show()
        
    def calculadoraTension(self):
        contadordenone=0
        vin = self.ventana.txtvin.text()
        if vin == "":
            contadordenone+=1
        else:
            vin = float(vin)

        r1 = self.ventana.txtr1.text()
        if r1 == "":
            contadordenone += 1
        else:
            r1 = float(r1)

        r2 = self.ventana.txtr2.text()
        if r2 == "":
            contadordenone += 1
        else:
            r2 = float(r2)

        vout = self.ventana.txtvout.text()
        if vout == "":
            contadordenone += 1
        else:
            vout = float(vout)

        if contadordenone >= 2:
            error("Error datos insuficicentes")
        else:
            if vin == "":
                valor = str(fvin(r1,r2,vout))
                self.ventana.txtvin.setText(valor)
            elif r1 == "":
                valor = str(fr1(r2,vout,vin))
                self.ventana.txtr1.setText(valor)
            elif r2 == "":
                valor = str(fr2(r1,vin,vout))
                self.ventana.txtr2.setText(valor)
            elif vout == "":
                valor = str(fvout(r2,r1,vin))
                self.ventana.txtvout.setText(valor)
            else:
                error("Todo está lleno socio")




    def calculadoraCorriente(self):
        contadordenone=0
        a = self.ventana.txtit.text()

        if a == "":
            contadordenone+=1
        else:
            it = float(a)

        b = self.ventana.txtr1i.text()
        if b == "":
            contadordenone += 1
        else:
            r1i = float(b)

        c = self.ventana.txtr2i.text()
        if c == "":
            contadordenone += 1
        else:
            r2i = float(c)

        if contadordenone != 0:
            error("Error datos insuficicentes")
            valor = ""
            self.ventana.txti1.setText(valor)
            self.ventana.txti2.setText(valor)
        else:
            respuesta1 = str(fi1(it,r1i,r2i))
            respuesta2 = str(fi2(it,r1i,r2i))
            self.ventana.txti1.setText(respuesta1)
            self.ventana.txti2.setText(respuesta2)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = launcher()
    dialogo.show()
    sys.exit(app.exec_())
    
