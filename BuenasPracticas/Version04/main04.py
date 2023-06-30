'''
Created on 29 jun 2023

Versión con la función navegar extraida del programa principal.

@author: Pedro

'''
from navegacion04 import navegar

print("Ejemplo 1")
# Posición inicial
ini = {'x' : 2, 'y' : 1, 'd' : 'N'}
# Posición final.
fin = {'x' : 5, 'y' : 4, 'd' : 'E'}
navegar(ini, fin)

print("Ejemplo 2")
# Posición inicial
ini = {'x' : 6, 'y' : 3, 'd' : 'O'}
# Posición final.
fin = {'x' : 2, 'y' : 5, 'd' : 'O'}
navegar(ini, fin)

# print("Ejemplo 3")
# # Posición inicial
# ini = {'x' : 6, 'y' : -2, 'd' : 'E'}
# # Posición final.
# fin = {'x' : -3, 'y' : 5, 'd' : 'O'}
# navegar(ini, fin)