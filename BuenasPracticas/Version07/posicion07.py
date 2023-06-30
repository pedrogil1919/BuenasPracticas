'''
Created on 29 jun 2023

Abstracción de la posición del robot.

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
            raise TypeError("Orientación debe ser un carácter")
        if not d in orientacion:
            raise ValueError("Orientación debe tomar los valores: O, S, E, N")
        self.d = d

    def localizar(self, objetivo):
        """Determina la posición del objetivo en función de su orientación
        
        """
        # Las coordenadas de posición es relativa a la orientación del robot.
        # No obstante, para la orientación conservo su valor absoluto, en lugar
        # de relativo a la orientación del robot por no complicar la función
        # en exceso.

        # Calculamos la distancia entre puntos en ambas dimensiones.
        dx = objetivo.x - self.x
        dy = objetivo.y - self.y
        
        if self.d == 'E':
            x = +dx
            y = +dy
        elif self.d == 'N':
            x = +dy
            y = -dx
        elif self.d == 'O':
            x = -dx
            y = -dy
        elif self.d == 'S':
            x = -dy
            y = +dx
        d = objetivo.d

        return Posicion(x, y, d)

    def objetivo_delante(self, objetivo):
        obj_aux = self.localizar(objetivo)
        return obj_aux.x > 0

    def objetivo_detras(self, objetivo):
        obj_aux = self.localizar(objetivo)
        return obj_aux.x < 0

    def objetivo_derecha(self, objetivo):
        obj_aux = self.localizar(objetivo)
        return obj_aux.y < 0

    def objetivo_izquierda(self, objetivo):
        obj_aux = self.localizar(objetivo)
        return obj_aux.y > 0

    def objetivo_alcanzado(self, objetivo):
        obj_aux = self.localizar(objetivo)
        return (obj_aux.x == 0 and obj_aux.y == 0)
    
    def __str__(self):
        """Imprimir en pantalla."""
        return "\n\tX: %.1f\n\tY: %.1f\n\td: %c\n" % (self.x, self.y, self.d)

    # def __eq__(self, pose):
    #     """Comparar dos posiciones."""
    #     if self.x != pose.x:
    #         return False
    #     if self.y != pose.y:
    #         return False
    #     if self.d != pose.d:
    #         return False
    #     # Solo cuando todos los valores son iguales devolvemos True.
    #     return True