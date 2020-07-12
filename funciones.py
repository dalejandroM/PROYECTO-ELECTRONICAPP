import winsound

#función error
def sonido():
    winsound.PlaySound("*",winsound.SND_ALIAS)
        

# Vin
def fvin(r1,r2,vout):
    vin = vout / (r2 / (r2 + r1))
    return(round(vin,3))

# R1
def fr1(r2,vout,vin):
    r1 = r2 * (vin - vout) / vout
    return(round(r1,3))

# R2
def fr2(r1,vin,vout):
    r2 = (vout * r1) / (vin - vout)
    return(round(r2,3))

# Vout
def fvout(r2,r1,vin):
    vout = vin * (r2 / (r2 + r1))
    return(round(vout,3))



#función divisor corriente r1
def fi1(it,r1i,r2i):
    i1 = (it * r2i) / (r1i + r2i)  
    return(round(i1,3))

#función divisor corriente r2
def fi2(it,r1i,r2i):
    i2 = (it * r1i) / (r1i + r2i)  
    return(round(i2,3))
