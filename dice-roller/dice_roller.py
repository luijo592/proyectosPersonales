print("Lanza el dado")
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input("Presiona Enter para lanzar el dado...")
        result = roll_dice()
        print(f"Has sacado un {result}")
        while True:
            respuesta = input("¿Quieres lanzar de nuevo? (s/n): ").lower()
            if respuesta == 's':
                print("Lanzando de nuevo...")
                break
            elif respuesta == 'n':
                print("Gracias por jugar.")
                return
            else:
                print("Por favor, responde con 's' para sí o 'n' para no.")
            
    print("Gracias por jugar. ¡Hasta luego!")

if __name__ == "__main__":
    main()
# Ejercicio: Simulador de lanzamiento de dados
# Este programa simula el lanzamiento de un dado de seis caras.
# El usuario puede lanzar el dado tantas veces como desee.
# Utiliza la biblioteca random para generar números aleatorios.
# Asegúrate de que el archivo se guarde en la ruta correcta: Ejercicios/dice_roller.py
# Guarda este código en Ejercicios/dice_roller.py
# y ejecútalo para probar su funcionamiento.