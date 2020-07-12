def amperaje(resistencia,voltaje,potencia):
    if potencia is None:
        a=voltaje/resistencia
    elif voltaje is None:
        a=(potencia/resistencia)**0.5
    else:
        a=potencia/voltaje
    return a

def voltaje(resistencia,corriente,potencia):
    if potencia is None:
        a=corriente*resistencia
    elif corriente is None:
        a=(potencia*resistencia)**0.5
    else:
        a=potencia/corriente
    return a

def potencia(resistencia,corriente,voltaje):
    if corriente is None:
        a=voltaje**2/resistencia
    elif voltaje is None:
        a = (corriente**2)*resistencia
    else:
        a = voltaje * corriente
    return a

def resistencia(corriente,voltaje,potencia):
    if potencia is None:
        a=voltaje/corriente
    elif voltaje is None:
        a=potencia/corriente**2
    else:
        a=voltaje**2/potencia
    return a