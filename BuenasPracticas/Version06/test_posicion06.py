'''
Created on 29 jun 2023

Control de errores. Excepciones. Añadir control de argumentos en el
constructor de la clase.

@author: Pedro
''' 
from posicion06 import Posicion

# Valor correcto.
pos = Posicion(2, 3, 'N')
print("Posición:", pos)

# Valor incorrecto. Comentar para poder continuar.
pos = Posicion(2.3, 4, 'S')

# Test excepción de tipo para coordenada x.
try:
    pos = Posicion(2.3, 4, 'S')
except TypeError as error:
    print(str(error))

# Test excepción de tipo para coordenada x.
try:
    pos = Posicion(2, 4.5, 'S')
except TypeError as error:
    print(str(error))

# Test excepción de tipo para orientacion.
try:
    pos = Posicion(2, 4, 24)
except TypeError as error:
    print(str(error))
    
# Test excepción de tipo para orientacion.
try:
    pos = Posicion(2, 4, 'T')
except ValueError as error:
    print(str(error))
