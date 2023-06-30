'''
Created on 29 jun 2023

@author: Pedro
'''

from posicion09 import Posicion

ini = Posicion(6, 2, 'N')
fin = Posicion(3, 4, 'S')
dis = ini.distancia(fin)
if dis != 5:
    print("Error en el cálculo de distancias.")
else:
    print("Cálculo de distancia correcto.")
