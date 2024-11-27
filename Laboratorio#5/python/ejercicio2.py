# Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que
# se cumpla una condición específica. Nota: Esta tarea la realizo en el mismo menu, donde el usuario debe salir ingresando 3

def condicionales_y_bucles():
    while True:
        print("\n--- Menú de Ejercicios ---")
        print("1. Determinar si un número es par o impar")
        print("2. Mostrar el cuadrado de una lista de números")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "3":
            print("¡Saliendo del programa! Hasta luego.")
            break
        
        if opcion == "1":
            numero = int(input("Ingresa un número: "))
            if numero % 2 == 0:
                print(f"El número {numero} es par.")
            else:
                print(f"El número {numero} es impar.")
        
        elif opcion == "2":
            numeros = [10, 20, 30, 40, 50]
            for numero in numeros:
                print(f"El cuadrado de {numero} es {numero ** 2}")
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú
condicionales_y_bucles()
