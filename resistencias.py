import random

def resistencia_num(resistenciaColor):
    banda1=resistenciaColor[0]
    banda2=resistenciaColor[1]
    banda3=resistenciaColor[2]
    tolerancia=resistenciaColor[3]
    codigoColor={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"purple":7,"gray":8,"white":9,"gold":(-1,5),"silver":(-2,10)}
    if banda3=="gold" or banda3=="silver":
        resistencia=[codigoColor[banda1],codigoColor[banda2],10**codigoColor[banda3][0],codigoColor[tolerancia][1]]
    else:
        resistencia=[codigoColor[banda1],codigoColor[banda2],10**codigoColor[banda3],codigoColor[tolerancia][1]]
    return resistencia

def calc_valor(resistencia):
    valor=[round(((resistencia[0]*10)+resistencia[1])*resistencia[2],2),resistencia[3]]
    return valor


def random_resistencia_color():
    colores=["black","brown","red","orange","yellow","green","blue","purple","gray","white","gold","silver"]
    resistenciaColor=[0,0,0,0]
    i=0
    while i<4:
        color=random.choice(colores)
        if i<2:
            if (color!="gold" and color!="silver"):
                resistenciaColor[i]=color
                i+=1
        elif i==2:
            resistenciaColor[i]=color
            i+=1
        elif (color=="gold" or color=="silver"):
            resistenciaColor[i]=color
            i+=1

    return resistenciaColor

#resistenciaColor=random_resistencia_color()
#print(resistenciaColor)
#resistencia=resistencia_num(resistenciaColor)
#print(resistencia)
#valor=calc_valor(resistencia)
#print(valor)

#if valor[0]>=(10**9):
#    ohm=valor[0]/(10**9)
#    print("EL valor es: "+str(ohm)+"GΩ ± "+str(valor[1])+"%")
#elif valor[0]>=(10**6):
#    ohm=valor[0]/(10**6)
#    print("EL valor es: "+str(ohm)+"MΩ ± "+str(valor[1])+"%")
#elif valor[0]>=(10**3):
#    ohm=valor[0]/(10**3)
#    print("EL valor es: "+str(ohm)+"KΩ ± "+str(valor[1])+"%")
#else:
#    print("EL valor es: "+str(valor[0])+"Ω ± "+str(valor[1])+"%")

