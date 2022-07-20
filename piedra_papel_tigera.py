import random

# Define aleatoriamente la elección de la maquina
def aleatoriedad():
    eleccion_maquina = random.randint(1, 3)
    if eleccion_maquina == 1:
        return 'piedra'
    elif eleccion_maquina == 2:
        return 'papel'
    elif eleccion_maquina == 3:
        return 'tijera'


# Define al ganador
def piedra_papel_tijera(eleccion_jugador):
    eleccion_maquina = aleatoriedad()
    print('Mi elección es ' + '¡' + eleccion_maquina.capitalize() + '!')
    if eleccion_jugador == 'piedra' and eleccion_maquina == 'tijera':
        print('\U0001f973 ¡Felicidades! \U0001f382, ¡Ganaste! \U0001f3c6')
    elif eleccion_jugador == 'papel' and eleccion_maquina == 'piedra':
        print('\U0001f973 ¡Felicidades! \U0001f382, ¡Ganaste! \U0001f3c6')
    elif eleccion_jugador == 'tijera' and eleccion_maquina == 'papel':
        print('\U0001f973 ¡Felicidades! \U0001f382, ¡Ganaste! \U0001f3c6')
    elif eleccion_jugador == eleccion_maquina:
            print('\U0001f62f\U0001f92f Es Empate \U0001f921')
    else:
        print('\U0001f606 Jaja \U0001f92a Perdiste \U0001fae1')


# Inicia el Juego
def run():
    eleccion_jugador = input('''Hola, vamos a jugar piedra \u270A, papel \u270B o tijera \u270C\uFE0F

Piedra \u270A, Papel \u270B  o ¡Tijeras! \u270C\uFE0F


1- Piedra \U0001faa8
2- Papel \U0001f4dc
3- Tijera \u2702\uFE0F

Selecciona una opción: ''')
    while eleccion_jugador == 1 or eleccion_jugador == 2 or eleccion_jugador == 3:
        continue
    if eleccion_jugador == '1':
        piedra_papel_tijera('piedra')
    elif eleccion_jugador == '2':
        piedra_papel_tijera('papel')
    elif eleccion_jugador == '3':
        piedra_papel_tijera('tijera')
    else:
        print('\u274C Esa opcón no es \U0001f645 valida')
        return run()


if __name__ == '__main__':
    run()