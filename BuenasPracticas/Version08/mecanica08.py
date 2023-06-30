'''
Created on 29 jun 2023

Versión completa del robot.

@author: Pedro

'''
class Mecanica:
    """Movimiento del robot. Traduce modificaciones de coordenadas a
    instrucciones propias de un robot movil con tracción diferencial (con sus
    limitaciones en cuanto a los giros que puede hacer).
    
    """
    def __init__(self, posicion):
        # Almacenemos la posición actual del elemento a mover.
        self.posicion = posicion

    def avanzar(self):
        """Avanza una posición en la orientación actual del robot."""
        if self.posicion.d == 'E':
            self.posicion.x += 1
        elif self.posicion.d == 'N':
            self.posicion.y += 1
        elif self.posicion.d == 'O':
            self.posicion.x -= 1
        elif self.posicion.d == 'S':
            self.posicion.y -= 1
        else:
            raise RuntimeError

    def girar_180(self):
        """Girar el robot 180 grados"""
        if self.posicion.d == 'E':
            self.posicion.d = 'O'
        elif self.posicion.d == 'N':
            self.posicion.d = 'S'
        elif self.posicion.d == 'O':
            self.posicion.d = 'E'
        elif self.posicion.d == 'S':
            self.posicion.d = 'N'

    def girar_derecha(self):
        """Girar el robot 90 grados a la derecha"""
        if self.posicion.d == 'E':
            self.posicion.d = 'S'
        elif self.posicion.d == 'N':
            self.posicion.d = 'E'
        elif self.posicion.d == 'O':
            self.posicion.d = 'N'
        elif self.posicion.d == 'S':
            self.posicion.d = 'O'

    def girar_izquierda(self):
        """Girar el robot 90 grados a la derecha"""
        if self.posicion.d == 'E':
            self.posicion.d = 'N'
        elif self.posicion.d == 'N':
            self.posicion.d = 'O'
        elif self.posicion.d == 'O':
            self.posicion.d = 's'
        elif self.posicion.d == 'S':
            self.posicion.d = 'E'
    
