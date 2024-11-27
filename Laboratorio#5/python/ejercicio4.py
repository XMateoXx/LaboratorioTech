def calculadora():
    while True:
        operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división, salir): ").lower()
        if operacion == "salir":
            print("Gracias por usar la calculadora.")
            break
        
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == "suma":
            print(f"Resultado: {num1 + num2}")
        elif operacion == "resta":
            print(f"Resultado: {num1 - num2}")
        elif operacion == "multiplicación":
            print(f"Resultado: {num1 * num2}")
        elif operacion == "división":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Operación no válida.")

calculadora()

import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intento = None
    
    while intento != numero_secreto:
        intento = int(input("Adivina el número entre 1 y 100: "))
        if intento < numero_secreto:
            print("Es mayor.")
        elif intento > numero_secreto:
            print("Es menor.")
    print("¡Felicidades, adivinaste. Pasate el juego 🥳🥳🥳!")

juego_adivinanza()