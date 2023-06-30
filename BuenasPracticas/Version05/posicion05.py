'''
Created on 29 jun 2023

Estructuración del código. Crear clase Posicion.

@author: Pedro

'''
orientacion = ['O', 'S', 'E', 'N']

class Posicion:
    """Operaciones con coordenadas en 2d
    
    """
    def __init__(self, x, y, d):
        # Constructor sin control de tipo de datos.
        self.x = x
        self.y = y
        self.d = d
    
    # def __str__(self):
    #     return "\n\tX: %.1f\n\tY: %.1f\n\td: %c\n" % (self.x, self.y, self.d)
    