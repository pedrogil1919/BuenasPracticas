'''
Created on 29 jun 2023

@author: Pedro
'''

import unittest
from posicion09 import Posicion

class DistanciaTest(unittest.TestCase):

    def test_distancia(self):
        ini = Posicion(6, 2, 'N')
        fin = Posicion(3, 4, 'S')
        dis = ini.distancia(fin)
        self.assertEqual(dis, 5, "Error en el cálculo de distancias.")

        # ini = Posicion(6, 7, 'N')
        # fin = Posicion(3, 5, 'S')
        # dis = ini.distancia(fin)
        # self.assertEqual(dis, 5, "Error en el cálculo de distancias")
        
        # ini = Posicion(3, 5, 'N')
        # fin = Posicion(6, 3, 'S')
        # dis = ini.distancia(fin)
        # self.assertEqual(dis, 5, "Error en el cálculo de distancias")
        

    # def test_constructor(self):
    #     # Comprobar que las excepciones saltan correctamente.
    #     self.assertRaises(TypeError, Posicion, x=3.2, y=2, d='N')
    #     self.assertRaises(TypeError, Posicion, x=3, y=2.5, d='N')
    #     self.assertRaises(TypeError, Posicion, x=3, y=2, d=3)
    #     self.assertRaises(ValueError, Posicion, x=3, y=2, d='A')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()