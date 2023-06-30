'''
Created on 29 jun 2023

Versión con la función navegar extraida del programa principal.

@author: Pedro

'''
def navegar(ini, fin):
    """Cálculo de la trayectoria del robot.

    Argumentos:
    ini -- Posición inicial del robot.
    fin -- Posición final del robot.
    
    En ambos casos, la posición debe venir dada como un diccionario
    con las siguientes claves:
    x: Coordenada horizontal.
    y: Coordenada vertical.
    d: Orientación (N, O, S, E)

    """
    # Hacemos una copia de la posición inicial para no alterarla.
    pos = ini.copy()

    # Comprobamos si tenemos que ir hacia la derecha.
    while pos['x'] < fin['x']:
        print(pos)
        # Colocamos el robot mirando hacia la derecha para poder avanzar.
        if pos['d'] == 'N':
            pos['d'] = 'O'
        elif pos['d'] == 'O':
            pos['d'] = 'S'
        elif pos['d'] == 'S':
            pos['d'] = 'E'
        # Una vez mirando hacia la derecha, avanzamos hasta alcanzar
        # la posición final.
        elif pos['d'] == 'E':
            pos['x'] += 1

    # Comprobamos si tenemos que ir hacia la izquierda.
    while pos['x'] > fin['x']:
        print(pos)
        # Colocamos el robot mirando hacia la izquierda para poder avanzar.
        if pos['d'] == 'S':
            pos['d'] = 'E'
        elif pos['d'] == 'E':
            pos['d'] = 'N'
        elif pos['d'] == 'N':
            pos['d'] = 'O'
        # Una vez mirando hacia la izquierda, avanzamos hasta alcanzar
        # la posición final.
        elif pos['d'] == 'O':
            pos['x'] -= 1

    # Comprobamos si tenemos que ir hacia arriba.
    while pos['y'] < fin['y']:
        print(pos)
        # Colocamos el robot mirando hacia arriba para poder avanzar.
        if pos['d'] == 'O':
            pos['d'] = 'S'
        elif pos['d'] == 'S':
            pos['d'] = 'E'
        elif pos['d'] == 'E':
            pos['d'] = 'N'
        # Una vez mirando hacia arriba, avanzamos hasta alcanzar la
        # posición final.
        elif pos['d'] == 'N':
            pos['y'] += 1

    # Comprobamos si tenemos que ir hacia abajo.
    while pos['y'] > fin['y']:
        print(pos)
        # Colocamos el robot mirando hacia abajo para poder avanzar.
        if pos['d'] == 'E':
            pos['d'] = 'N'
        elif pos['d'] == 'N':
            pos['d'] = 'O'
        elif pos['d'] == 'O':
            pos['d'] = 'S'
        # Una vez mirando hacia abajo, avanzamos hasta alcanzar la
        # posición final.
        elif pos['d'] == 'S':
            pos['y'] -= 1

    # Comprobamos si hay que modificar la orientación final.
    while pos['d'] != fin['d']:
        print(pos)
        if pos['d'] == 'E':
            pos['d'] = 'N'
        elif pos['d'] == 'N':
            pos['d'] = 'O'
        elif pos['d'] == 'O':
            pos['d'] = 'S'
        elif pos['d'] == 'S':
            pos['d'] ='E'
