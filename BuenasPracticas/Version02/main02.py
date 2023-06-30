'''
Created on 29 jun 2023

Versión con errores, ideal para detectar el error depurando.

@author: Pedro

'''
ini = {'x' : 2, 'y' : 7, 'd' : 'N'}
pos = ini.copy()
fin = {'x' : 5, 'y' : 4, 'd' : 'E'}

while pos['x'] < fin['x']:
    # print(pos)
    if pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['x'] += 1

while pos['y'] > fin['x']:
    # print(pos)
    if pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['x'] -= 1

while pos['y'] < fin['y']:
    # print(pos)
    if pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['y'] += 1

while pos['y'] > fin['y']:
    # print(pos)
    if pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['y'] -= 1

while pos['d'] != fin['d']:
    # print(pos)
    if pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['d'] ='E'

print("Posición inicial:", ini)
print("Posición actual:", pos)
print("Posición final:", fin)
print("Fin del programa")