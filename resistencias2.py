#funcion para sumar resistencias en serie
def serie(resistencias):
    sumar=0
    for i in resistencias:
        sumar+=float(i)
    return round(sumar,3)

#funcion para sumar resistencias en paralelo
def paralelo(resistencias):
    sumar=0
    for i in resistencias:
        sumar+=1/float(i)
    return round((1/sumar),3)

