
sumap = sumai = 0

while True:

    num = int(input("Ingrese un número positivo (0 salir): "))


    if num < 0:
        
        print("Número invalido. Ingrese nuevamente")
        continue

    if num == 0:
        break

    if num % 2 == 0:
        sumap+=num
    else:
        sumai += num

print(f"\nSuma pares: {sumap}")
print(f"\nSuma impares: {sumai}")