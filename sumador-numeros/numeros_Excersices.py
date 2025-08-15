"""Crea un programa que pida 5 números enteros al usuario.

Guárdalos en una lista.

Muestra:

El número más grande (max()).

El número más pequeño (min()).

La suma total (sum()).

El promedio."""
numberList = list()
i = 1
print("Ingresa 5 numeros a continuacion.")

for i in range(1,6):
    while True:
        try:
            number = int(input(f"Ingresa un numero entero {i}: "))
            if number >= 0:
                numberList.append(number)
                break
            else:
                print("ingresa un numero entero positivo")
        except ValueError:
            print("debe ser un numero entero")
print(numberList)
print(f"el numero mayor es: {max(numberList)}")
print(f"el numero menor es: {min(numberList)}")
print(f"la suma de los numeros es : {sum(numberList)}")
print(f"el promedio es : {sum(numberList)/len(numberList): .2f}")
