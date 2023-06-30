'''
Created on 29 jun 2023

Abstracción de la posición del robot.

@author: Pedro

''' 
from posicion07 import Posicion

# Orientación este.
ini = Posicion(2, 3, 'E')
fin = Posicion(4, 6, 'N')
loc = ini.localizar(fin)

print(loc)
# Comprobamos las funciones más genéricas.
print(ini.objetivo_delante(fin))
print(ini.objetivo_izquierda(fin))
# Si lo hacemos al revés, el resultado ¿será el inverso?
print(fin.objetivo_delante(ini))
print(fin.objetivo_izquierda(ini))

# Orientación norte.
ini = Posicion(2, 3, 'N')
fin = Posicion(4, 6, 'N')
loc = ini.localizar(fin)
print(loc)

pos = Posicion(3, -2, 'N')
# Para poder comparar, hay que implementar el método __eq__
if loc == pos:
    print("Iguales")
else:
    print("Distintos")