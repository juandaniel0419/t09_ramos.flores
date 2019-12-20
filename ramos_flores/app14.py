import libreria
import os
gravedad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
d=libreria.caida_libre_cuerpo(gravedad,tiempo)
print(d)
