
filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: "))

print()
i = 0

while i < filas:

    j = 0

    while j < columnas:
        print("*", end = "")
        j+=1
    print()
    i+=1