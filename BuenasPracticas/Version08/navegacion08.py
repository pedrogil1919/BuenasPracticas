'''
Created on 29 jun 2023

Versión completa del robot.

@author: Pedro

'''
from posicion08 import Posicion
from mecanica08 import Mecanica

class Navegacion:

    def __init__(self, x, y, d):
        # Almacenamos la posición actual del robot en un objeto de clase
        # Posicion.
        self.posicion = Posicion(x, y, d)
        # Creamos una instancia de la clase que permitira desplazarse.
        self.mecanica = Mecanica(self.posicion)


    def desplazarse(self, destino):
        # Función de control para alcanzar el destino.
        print(self.posicion)
        if self.posicion.objetivo_alcanzado(destino):
            return True
        # Localizamos dónde está el objetivo, y nos desplazamos en consecuencia.
        if self.posicion.objetivo_delante(destino):
            self.mecanica.avanzar()
        elif self.posicion.objetivo_detras(destino):
            self.mecanica.girar_180()
        elif self.posicion.objetivo_derecha(destino):
            self.mecanica.girar_derecha()
        elif self.posicion.objetivo_izquierda(destino):
            self.mecanica.girar_izquierda()
        return False
