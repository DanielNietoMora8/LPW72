# -*- coding: utf-8 -*-
"""Luis_Perez_Londoño.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lpf1dzMlQ7xxbMVbd_pUKXAzyMG756B6
"""

class Identificacion:
    def __init__(self, name, age ):
        self.__name = name
        self.__age = age
    
    def saludo(self):
        print(f"Feliz dia, soy {self.__name} y tengo {self.__age} años.")

individuo = Identificacion("Felipe Pérez", 26)
individuo.saludo()

import numpy as np
import matplotlib.pyplot as plt

class Matrices:
    def __init__(self, size, fill, num_matrices):
        self.size = size
        self.fill = fill
        self.num_matrices = num_matrices
        self.matrices = []

    def generate_matrices(self):
        for _ in range(self.num_matrices):
            if self.fill == "zeros":
                matrix = np.zeros(self.size)
            elif self.fill == "ones":
                matrix = np.ones(self.size)
            elif self.fill == "random":
                matrix = np.random.uniform(20, 40, self.size)
            else:
                raise ValueError("Invalid fill")
            
            self.matrices.append(matrix)

    def matrix_multiplication(self):
        if len(self.matrices) < 2:
            raise ValueError("Insufficient matrices to perform multiplication")
        
        result = self.matrices[0]
        for matrix in self.matrices[1:]:
            result = np.matmul(result, matrix)
        
        return result

    def show_matrices(self):
        for matrix in self.matrices:
            plt.imshow(matrix)
            plt.show()

    def sum_of_elements(self):
        sums = []
        for matrix in self.matrices:
            sums.append(np.sum(matrix))
        
        return sums