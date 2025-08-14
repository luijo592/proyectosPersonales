def pedir_numero():
    numeros = []
    while True:
        dato_usuario = input("Ingresa un numero, escribe fin para terminar: ")
        if dato_usuario.lower() == "fin":
            break
        try:
            dato = float(dato_usuario)  # Convierte a número (acepta enteros y decimales)
            numeros.append(dato)
        except ValueError:
            print("Entrada no válida, intenta de nuevo.")
    return numeros



print("\nBienvenidos a la calculadora by Luijo")
print("\nSelecciona la operacion que quisieras realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir\n")


while True:

    opcion = int(input("Que operacion quieres realizar (Selecciona del 1 al 5)?: "))
    if opcion == 1:
        lista_recibida = pedir_numero()
        resultado = sum(lista_recibida)
        print(resultado)
       
    elif opcion == 2:

        lista_recibida = pedir_numero()
        resultado = lista_recibida[0]
        for numero in lista_recibida[1:]:
            resultado -= numero
        print(resultado)
        
    elif opcion == 3:
        
        lista_recibida = pedir_numero()
        resultado = lista_recibida[0]
        for numero in lista_recibida[1:]:
            resultado *= numero
        print(resultado)
        
    elif opcion == 4:

        lista_recibida = pedir_numero()
        resultado = lista_recibida[0]
        try:
            for numero in lista_recibida[1:]:
                resultado /= numero
            print(f"{resultado:.2f}")
        except ZeroDivisionError:
            print("no esta permitida la division por 0.")

    elif opcion == 5:
        print("Saliendo de la calculadora")
        break
    
    else:
        print("debes seleccionar una opcion valida entre: ")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. Salir")

