# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:40:15 2022

@author: carme
"""

class Persona:
    def __init__(self, p_nombre,p_fechanac):
        self.__nombre=p_nombre
        self.__fechanac=p_fechanac
        self.__peso=None
        self.__altura=None
    
    def set_peso(self,p_peso):
        """
        metodos para establecer peso de la persona

        Parameters
        ----------
        p_peso : float
            peso positivo y mayor a 1.5kg.

        Returns
        -------
        None.

        """
        self.__peso=p_peso
        
        proposicion_1=isinstance(p_peso, float)
        proposicion_2=p_peso>=1.5
        proposiciones=[proposicion_1,proposicion_2]
            
        if all(proposiciones):
            self.__peso=p_peso
        elif not proposicion_2 :
            raise ValueError("el peso no puede ser menor a 1.5kg")
        elif not proposicion_1:
            raise TypeError("el peso debe ser de tipo flotante")
            
    
    def set_altura(self,p_altura):
        self.__altura=p_altura
    def _str__(self):
        return str(self.__dict__)
    def calcular_IMC(self):
        p=self.__peso
        a=self.__altura
    def get_nombre(self):
        return self.__nombre
        
if __name__=="__main__":
    p1=Persona("Pepe", "1978-10-31")
    print(p1)