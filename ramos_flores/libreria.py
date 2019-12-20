# el programa pedira un numero cualquiera
def pedir_numero(msg):
    numero_invalido=True
    valor=(msg)
    while(numero_invalido):
        valor=input(msg)
        numero_invalido=(valor.isdigit()==False)
    return int(valor)
#fin_def



# el programa calculara un area de un cubo
def area_cubo(a,b,c):
    a_invalido=True
    b_invalido=True
    c_invalido=True
    numero=0
    while(a_invalido):
        numero=(input("ingrese valor:"))
        a_invalido=(numero.isdigit()==False)
    while (b_invalido):
        numero =(input("ingrese valor:"))
        b_invalido = (numero.isdigit() == False)
    while (c_invalido):
        numero =(input("ingrese valor:"))
        c_invalido = (numero.isdigit() == False)
    return int(a*b*c)
#fin_def


def pedir_rango(msg,r1,r2):
    rango_invalido=True
    valor=0
    while(rango_invalido):
        valor=pedir_numero(msg)
        rango_invalido=(valor < r1 or valor > r2)
    #fin_while
    return valor
#fin_def

def pedir_temperatura(msg):
    return pedir_rango(msg,0,45)
#fin_def

def pedir_tamaño(msg):
    return pedir_rango(msg,0.5,2.5)
#fin_def

def pedir_sueldo(msg):
    return pedir_rango(msg,850,8000)
#fin_def


def area_elipse(a,b):
    a_invalido=True
    valor_a=0
    b_invalido=True
    valor_b=0
    while(a_invalido):
        valor_a=input("ingrese valor a:")
        a_invalido=(valor_a.isdigit()==False)
    while(b_invalido):
        valor_b=input("ingrese el valor b:")
        b_invalido=(valor_b.isdigit()==False)
    return a*b
#fin_def


def pedir_tiempo(a,b):
    a_invalido = True
    valor_a = 0
    b_invalido = True
    valor_b = 0
    while (a_invalido):
        valor_a = input("ingrese la distancia a:")
        a_invalido = (valor_a.isdigit() == False)
    while (b_invalido):
        valor_b = input("ingrese el velocidad b:")
        b_invalido = (valor_b.isdigit() == False)
    return a/b
#fin_def

def pedir_nombre(msg):
    msg_invalido=True
    nombre=""
    while(msg_invalido):
        nombre=input(msg)
        msg_invalido=(len(nombre)<=2)
    return msg
#fin_def


def numero_celular(msg):
    numero_celular_invalido=True
    numero=0
    while(numero_celular_invalido):
        numero=input(msg)
        numero_celular_invalido=(numero.isdigit()==False)
        numero_celular_invalido=(len(numero)!=9)
    return numero
#fin_def


def diferencia_de_cuadrados(a,b):
    resultado=(a+b)*(a-b)
    return resultado
#fin_def



def binomio_cuadrado(a,b):
    resultado=(a*2)+(b*2)+(2*a*b)
    return resultado
#fin_def
def binomio_cubo(a,b):
    resultado=(a*3)+(b*3)+(3*a*b)
    return resultado
#fin_def

def diferencia_cubos(a,b):
    resultado=(a-b)((a*2)+(2*a*b)+(b*2))
    return resultado
#fin_def



def caida_libre_cuerpo(gravedad,tiempo):
    resultado=(1/8)(gravedad)(tiempo**2)
    return resultado

#fen_def


def tiempo_vuelo_cuerpo(gravedad,velocidad):
    resultado=((velocidad**2)/(2*gravedad))
    return resultado
#def_def


def energia_total(masa,velocidad_luz):
    resultado=((masa)*(velocidad_luz)**2)
    return resultado
#fin_def

def fuerza(masa,aceleracion):
    resultado=(masa*aceleracion)
    return resultado
#fin_def