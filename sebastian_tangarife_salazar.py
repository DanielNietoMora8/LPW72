# -*- coding: utf-8 -*-
"""ejercicio_para_entregar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jkdGEhFnUEZ_6f09odSrjpZ5rnWIb0Se

SEGUNDO PUNTO DEL EXAMEN.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class  identificacion:
  def __init__(self, nombre:str, edad:int):
    self._nombre = nombre
    self._edad = edad

  def mensaje(self):
    print(f" Hola soy {self._nombre} y tengo {self._edad} años")

saludo = identificacion("sebastian", 33)
saludo.mensaje()

"""PRIMER PUNTO DEL EXAMEN"""

class  matriz:
  def __init__(self, tamano:tuple, como_llenar:str, numeros_matriz:int):
    self._tamano = tamano
    self._como_llenar = como_llenar
    self._numeros_matriz = numeros_matriz

  def set_tupla(self):
    tamano = np.array([2],[2])

  def set_como_llenar(self):
    if (como_llenar == "zeros", "ones", "random")

  def set_numeros_matriz(self):
    tamano = np.array([2],[2])