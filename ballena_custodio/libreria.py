####ejercicio1
def area_recrangulo(base, altura):
    resultado = (base * altura)
    return resultado

####ejercicio2
def velocidad_final(vinicial,a,t):
    resultado=(vinicial+(a*t))
    return resultado

####ejercicio3
def distancia(velocidad,tiempo):
    resultado=(velocidad*tiempo)
    return resultado

###ejercicio4
def restar(a,b):
    resultado=(a-b)
    return resultado

####ejercicio5
def multiplicar(a,b):
    resultado=a*b
    return resultado

###ejercicio6
def raiz_cuadrada(a,b):
    resultado=(a*b)**(1/2)
    return resultado

###ejericio7
def distancia(Vf,Vi,t):
    resultado=((Vf+Vi)/2)*(t)
    return resultado

##ejercicio8
def fuerza(masa,aceleracion):
    resultado=(masa*aceleracion)
    return resultado

####ejercicio9
def trabajo_mecanico(fuerza,distancia):
    resultado=(fuerza*distancia)
    return resultado

###ejercicio10
def potencia(trabajo,tiempo):
    resultado=(trabajo*tiempo)
    return resultado

####ejercicio11
def energia_cinetica(masa,velocidad):
    resultado=((1/2)*(masa))*(velocidad)**2
    return resultado

###ejercicio12
def energia_mecanica(energia_potencial,energia_cinetica,energia_elastica):
    resultado=(energia_cinetica+energia_elastica+energia_potencial)
    return resultado

###ejercicio13
def energia_potencial(masa,gravedad,altura):
    resultado=(masa*gravedad*altura)
    return resultado

####ejercicio14
def energia_elastica(constante,deformacion):
    resultado=(1/2)*(constante)*((deformacion)**2)
    return resultado

###ejercicio15
def densidad(masa,volumen):
    resultado=masa*volumen
    return resultado

###ejercicio16
def presion(fuerza,area):
    resultado=fuerza/area
    return resultado

###ejercicio17
def empuje_del_agua(densidad,gravedad,volumen):
    resultado=(densidad*gravedad*volumen)
    return resultado

###ejercicio18
def calor(trabajo,energia_interna):
    resultado=(trabajo+energia_interna)
    return resultado

###ejeercicio19
def energia_total(masa,velocidad_luz):
    resultado=((masa)*(velocidad_luz)**2)
    return resultado

####ejercicio20
def diferencia_de_cuadrados(a,b):
    resultado=(a+b)*(a-b)
    return resultado

###ejercicio21
def binomio_cuadrado(a,b):
    resultado=(a**2)+(b**2)+(2*a*b)
    return resultado

###ejercicio22
def binomio_cubo(a,b):
    resultado=(a**3)+(b**3)+(3*a*b)
    return resultado

###ejercicio23
def diferencia_cubos(a,b):
    resultado=(a-b)*((a**2)+(2*a*b)+(b**2))
    return resultado

###ejercicio24
def caida_libre_cuerpo(gravedad,tiempo):
    resultado=(1/8)*(gravedad)*(tiempo**2)
    return resultado

####ejercicio25
def tiempo_vuelo_cuerpo(gravedad,velocidad):
    resultado=((velocidad**2)/(2*gravedad))
    return resultado
