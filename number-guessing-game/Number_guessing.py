import random

print("\nBienvenidos al juego de azar para adivinar numeros.")
print("debes ingresar un numero e intentar adivinar el numero")
print("generado por la maquina del 1 al 100.\n")
print("Ingresa numeros, intentando adivinar el numero en el menor")
print("numero de intentos posibles.")
print("\nPara salir del juego, escribe la palabra (SALIR) ")
print("NOTA: Recuerda que debes ingresar un numero del 1 al 100\n")

while True:
    numero_secreto = random.randint(1,100)
    intentos = 0
    print("He pensado un numero entre el 1 y el 100...")
    print("lo logras adivinar?")
        
    while True:
        seleccion_del_usuario = input("elige un numero: ")

        if seleccion_del_usuario.lower() == "salir":
            print("Juego terminado.")
            exit()

        try: 
            seleccion_del_usuario = int(seleccion_del_usuario)
        except  ValueError:
            print("entrada no valida, ingresa un numero")
            continue

        if seleccion_del_usuario < 1 or seleccion_del_usuario > 100:
            print("El numero debe estar en un rango del 1 al 100!!!")
            continue
        intentos += 1

        if numero_secreto == seleccion_del_usuario:
            print("Acertaste!!!")
            print(f"el numero era: {seleccion_del_usuario}")
            print(f"lo lograste en: {intentos} intentos")
            break
                
        elif seleccion_del_usuario < numero_secreto:
            print("el numero secreto es mas grande, sigue intentando")
            print(f"llevas {intentos} intentos")
                
        elif seleccion_del_usuario > numero_secreto:
            print("el numero secreto es menor, intenta nuevamente")
            print(f"llevas {intentos} intentos")
            
    jugar_otra_vez = input("Quieres jugar otra vez? (s/n): ").lower()     
    if jugar_otra_vez != "s":
        print("Gracias por jugar")
        break