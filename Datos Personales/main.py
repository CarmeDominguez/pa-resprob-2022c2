# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:34:14 2022

@author: carme
"""

from Modulos.persona import Persona
import Modulos.funciones as fimc
persona=Persona()
otrapersona=Persona()

#Cargamos los datos personales
datos_personas=fimc.cargar_datos_personales("datos/datos_personales.txt")

# #Calcular IMCs
# IMC_p=fimc.calcular_IMCs(datos_personas)

# #Indicar quienes tienen sobrepeso
# sobrep=fimc.mostrar_personas_con_sobrepeso (IMCs_personas)

print("en el main")
print("1:", __name__)