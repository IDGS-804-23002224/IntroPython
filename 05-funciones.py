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
    print("El resultado de la suma de {0} + {1} es: {2}".format(a,b,resultado))

def funcionResta():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a - b 
    print("El resultado de la resta de {0} - {1} es: {2}".format(a,b,resultado))
    
def funcionMultiplicacion():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a * b
    print("El resultado de la multiplicación de {0} x {1} es: {2}".format(a,b,resultado))

def funcionDivision():
    print("Ingresa dos numeros:")

    a = int(input('ingresa el primer numero'))
    b = int(input('ingresa el segundo numero'))

    resultado = a / b
    print("El resultado de la división de {0} / {1} es: {2}".format(a,b,resultado))

def main():
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")

    opcion = int(input("Selecciona que deseas hacer:"))

    if opcion == 1:
        funcionSuma()
    elif opcion == 2:
        funcionResta()
    elif opcion == 3:
        funcionMultiplicacion()
    elif opcion == 4:
        funcionDivision()
    else:
        print("Opción no válida...")

if __name__ == "__main__":
    main()