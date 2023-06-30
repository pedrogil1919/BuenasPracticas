'''
Created on 29 jun 2023

Estructuración del código. Crear clase Posicion. Test de la clase.

@author: Pedro

'''   
from posicion05 import Posicion

# Valor correcto.
pos = Posicion(2, 3, 'N')
print("Posición:", pos)

# Valor incorrecto, pero el programa no nos avisa.
pos = Posicion(2.3, 4, 'S')
print("Posición:", pos)
