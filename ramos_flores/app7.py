import libreria
import os
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
t=libreria.pedir_tiempo(a,b)
print("la distancia de un recorrido es",a,"\n recorre a una velocidad de",b,"entonces su tiempo es:",t)