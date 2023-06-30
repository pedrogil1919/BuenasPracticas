'''
Created on 29 jun 2023

Control de errores. Excepciones. Añadir control de argumentos en el
constructor de la clase.

@author: Pedro

'''   
orientacion = ['O', 'S', 'E', 'N']

class Posicion:
    """Operaciones con coordenadas en 2d
    
    """
    # def __init__(self, x, y, d):
    #     # Constructor sin control de tipo de datos.
    #     self.x = x
    #     self.y = y
    #     self.d = d
    
    def __init__(self, x, y, d):
        if not isinstance(x, int):
            raise TypeError("Coordenada x deber ser un número entero.")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("Coordenada y deber ser un número entero.")
        self.y = y
        if not isinstance(d, str):
            raise TypeError("Orientación debe ser un carácter.")
        if not d in orientacion:
            raise ValueError("Orientación debe tomar los valores: O, S, E, N.")
        self.d = d
    
    def __str__(self):
        return "\n\tX: %.1f\n\tY: %.1f\n\td: %c\n" % (self.x, self.y, self.d)
    