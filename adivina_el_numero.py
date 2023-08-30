import random


# Adivina el numero



def adivina_el_numero(x):

    print("=" * 50)
    print("Bienvenido(a) al juego!!!")
    print("=" * 50)
    print("Tu meta es adivinar el número generado por la computadora")

    numero_aleatorio = random.randint(1, x) # Numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        # EL usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande")

    print(f"¡Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(15)