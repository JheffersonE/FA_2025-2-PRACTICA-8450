
num = int(input("Ingrese un número positivo: "))

while num <= 0:
   num = int(input("Error. Ingrese un número positivo: "))


i = 1

while i <= 12:
    
    print(f"{i} * {num} = {i * num}")
    i+=1

