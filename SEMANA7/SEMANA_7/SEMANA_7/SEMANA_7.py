from ast import Num
import random

#Ejercicio 1
def ejer1():

    p = i = 0

    while True:

        num = int(input("Ingrese un número entero (Negativo para salir): "))

        if (num < 0):
            break
        if (num % 2) == 0:
            p += 1
        else:
            i += 1

    print(f"\nCantidad pares: {p}")
    print(f"Cantidad impares: {i}")

    #Ejercicio 1


#Ejercicio 2

def ejer2():
    
    print("****************************************")

    print("*    Bienvenido al juego adivinador    *")
    print("1. Adivinar el número entre 1 y 20")
    print("2. Tienes 3 intentos")

    print("****************************************")

    intentos = 3
    secreto = random.randint(1, 20)

    while intentos > 0:

        num = int(input("\nIngrese un número: "))

        if (secreto == num):
            print("\nCorrecto! Adivinastes el número.")
        else: 
            intentos -= 1
            if (num < secreto):
                print(f"\nPista: El número es mayor, te quedan {intentos} intentos")
            else:
                print(f"\nPista: El número es menor, te quedan {intentos} intentos")
    else:
        print(f"\nNo lograstes adivinar el número: {secreto}")


#Ejercicio 3

def ejer3():
    
   while True:
       suma = 0
       num = int(input("Ingrese un número: "))

       for i in range(1, num + 1):
           suma += i
           print(i, end = " ")                                                       
       print(f"\nSuma: {suma}")

       opc = input("¿Desea continuar?(S/N): ")

       if (opc == "N" or opc == "n"):
            break
       
ejer3()