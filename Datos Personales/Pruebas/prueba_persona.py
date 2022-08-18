# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:22:08 2022

@author: carme
"""

import unittest
from Modulos.persona import Persona
# import modulos.persona

class TestPersona(unittest.TestCase):
    
    def setUp(self):
        self.p=Persona('Manuel','03-06-1770')
    
    def test_creackion_de_persona(self):
        p=self.p
        p=Persona('Manuel', '03-06-1770')
        self.assertTrue(isinstance(p,Persona))
        self.assertEqual(p.get_nombre(),'Manuel')
        with self.assertRaises(AttributeError):
         apellido=p.getApellido()   
        # self.assertEqual(p.getApellido(), 'Belgrano')
    
    def test_IMC(self):
        self.p.set_altura(1.5)
        self.p.set_peso(100)
        imc=self.p.calcular_IMC()
        self.assertAlmostEqual(imc,44.444, delta=0.1)
        
if __name__ == '__main__':
    unittest.main()
    unittest.main()