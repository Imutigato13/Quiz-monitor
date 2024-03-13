import re

def validar_entero(msj):
    '''Valida que el valor ingresado corresponda a un numero entero y retorne dicho numero entero'''
    patron_entero = re.compile(r'^[+-]?\d+$')
    while True:
        try:
            entero = input(msj)
            if patron_entero.match(entero):
                return int(entero)
        except:
                print("Ingrese un número entero válido")

def validar_alfabetico(msj):
    '''Valida que la entrada corresponde a caracteres alfabeticos y retorna la misma entrada validada'''
    patron = re.compile(r'^[a-zA-Z]+$')
    while True:
        try:
            alfab = input(msj)
            if patron.match(alfab):
                return alfab
        except:
                print("Ingrese solo caracteres alfabéticos")

def validar_alfanumerico(msj):
    '''Valida que la entrada corresponda a un caracter alfanumerico y retorna la entrada validada'''
    patron = re.compile(r'^[a-zA-Z0-9\s]+$')
    while True:
        try:                
            alfanum = input(msj)
            if patron.match(alfanum):
                return alfanum
        except:
            print("Ingrese solo caracteres alfanuméricos")
