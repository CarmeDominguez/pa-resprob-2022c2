# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:52:17 2022

@author: carme
"""
from persona import Persona

#Cargamos los datos personales
def cargar_datos_personales(p_nombre_archivo):
   
    datos_personas = dict()
    
    with open (p_nombre_archivo, 'rt') as archivo:
        for linea in archivo:
            print(linea)
            nombre,fecha,peso,altura=linea.split(" ")
            print(nombre,fecha,peso,altura)
            peso=float(peso)
            altura=float(altura)
            
            persona=Persona(nombre,fecha)
            persona.set_peso(peso)
            persona.set_altura(altura)
            
            datos_personas[persona.get_nombre()]=persona
            
    return datos_personas

def calcular_IMCs(p_datos_personas):
    IMCs_personas = []
    for clave in p_datos_personas:
        persona = p_datos_personas[clave]
        IMC= persona.calcular_IMC()
        IMCs_personas.append(IMC)
    return IMCs_personas


def mostrar_personas_con_sobrepeso(p_datos_personas):
    print("personas con sobrepeso:")
    for nombre in p_datos_personas:
        persona=p_datos_personas[nombre]
        if persona.calcular_IMC( )>=30.0:
            print("\t", persona.get_nombre())


print("fuera del if")

if __name__ == "__main__" :
    print("pruebas en funciones.py")
    print("__main__")
    print("2:", __name__)
 
    datos_personas=cargar_datos_personales('../Datos/datos_personas.txt')
    
    print(datos_personas)
    
for clave in datos_personas:
    print(clave)
for clave,valor in datos_personas.items():
    print(clave,":", valor)