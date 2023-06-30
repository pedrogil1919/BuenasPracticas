'''
Created on 29 jun 2023

Solución inicial, simple pero funcional.

@author: Pedro

'''
ini = {'x' : 2, 'y' : 1, 'd' : 'N'}
# ini = {'x' : 2, 'y' : 7, 'd' : 'N'}
pos = ini.copy()
fin = {'x' : 5, 'y' : 4, 'd' : 'E'}

while pos['x'] < fin['x']:
    if pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['x'] += 1

while pos['y'] > fin['x']:
    if pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['x'] -= 1

while pos['y'] < fin['y']:
    if pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['d'] = 'E'
    elif pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['y'] += 1

while pos['y'] > fin['y']:
    if pos['d'] == 'E':
        pos['d'] = 'N'
    elif pos['d'] == 'N':
        pos['d'] = 'O'
    elif pos['d'] == 'O':
        pos['d'] = 'S'
    elif pos['d'] == 'S':
        pos['y'] -= 1

while pos['d'] != fin['d']:
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