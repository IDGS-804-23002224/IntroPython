import os

"""
def funcion1():
    print("Esta es la funcion 1")

def funcion2():
    os.system("cls")

def funcion3():
    print("Esta es la funion 3")

def main():
    funcion1()
    funcion3()

if __name__ == "__main__":
    main()
"""
"""
Crear un programa que permita realizar las operaciones básicas +,-,*,/
utilizando una funcion para cada operacion y un menu principal para desplegar y 
elegir que operación realizaremos
"""
resultado = 0
a = 0
b = 0

def funcionSuma():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a + b
    print(resultado)

def funcionResta():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a - b 
    print(resultado)

def funcionMultiplicacion():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a * b
    print(resultado)

def funcionDivision():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a / b
    print(resultado)

