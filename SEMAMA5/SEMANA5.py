import math


def ejer2():
    
    annio = int(input("Ingrese el año: "))

    if (annio %4 == 0 and annio %100 != 0) or (annio %400 == 0):
        print("\nEl año es biciesto")
    else:
        print("\El no es biciesto")


    if annio % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def ejer3():

    monto = float(input("ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion = int(input("\nIngrese una opción: "))

    match opcion:
        case 1:
            print(f"Dolares {round(monto / 3.75, 0)}")
        case 2:
            print(f"Euros {monto / 4.05:.2f}")
        case 3:
            print("Opción incorrecta")

def ejer4():
    print("Bienvenido al sistema de calculos de áreas\n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            lado = int(input("Ingrese el lado: "))
            print(f"Área del cuadrado: {lado * lado}")
        case 2:
            base = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print(f"Área del rectangulo: {(base*alt)}")
        case 3:
            base = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print(f"Área del triangulo: {(base*alt)/2}")
        case 4:
            radio = float(input("Ingrese el radio: "))
            print(f"Área del circulo: {round(math.pi * radio ** 2),2}")
        case _:
            print("Opción incorrecta")

ejer4()