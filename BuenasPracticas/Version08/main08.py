'''
Created on 29 jun 2023

Versión completa del robot.

@author: Pedro

'''
from navegacion08 import Navegacion
from posicion08 import Posicion

print("Prueba 1")
robot = Navegacion(2, 4, 'E')
destino = Posicion(6, 5, 'S')
while not robot.desplazarse(destino):
    pass

print("Prueba 2")
robot = Navegacion(2, 4, 'N')
destino = Posicion(6, -5, 'S')
while not robot.desplazarse(destino):
    pass

print("Fin")