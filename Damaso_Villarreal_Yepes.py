## Punto 1:

import numpy as np
import matplotlib.pyplot as plt

class Generador_matrices:
    def __init__(self, size, fill_type, num_matrices):
        self.size = size
        self.fill_type = fill_type
        self.num_matrices = num_matrices
        self.matrices = []
        
    def generacion_matriz(self):
        if self.fill_type == "zeros":
            matriz = np.zeros(self.size)
        elif self.fill_type == "onces":
            matriz = np.ones(self.size)
        elif self.fill_type == "random":
            matriz = np.random.uniform(20, 40, self.size)
        else:
            raise ValueError("No es válido. debe elegir 'zeros', 'onces' o 'aleatorio'.")
        
        self.matrices.append(matriz)
        
    def multiplicar_matrices(self):
        if len(self.matrices) < 2:
            print("no hay suficientes matrices para multiplicarlas.")
            return
        
        result = self.matrices[0]
        for matriz in self.matrices[1:]:
            if matriz.shape[0] != result.shape[1]:
                print("los tamaños de las matrices no se pueden multiplicar.")
                return
            result = np.dot(result, matriz)
        
        return result
    
    def mostrar_matrices(self):
        if len(self.matrices) == 0:
            print("Sin matrices para imprimir.")
            return
        
        for i, matriz in enumerate(self.matrices):
            plt.subplot(1, len(self.matrices), i+1)
            plt.imshow(matriz)
            plt.axis('off')
        
        plt.show()
    
    def suma_elementos(self):
        if len(self.matrices) == 0:
            print("Sin matrices para sumar.")
            return
        
        sums = []
        for matriz in self.matrices:
            sums.append(np.sum(matriz))
        
        return sums
##ejecutores:

matriz_gen = Generador_matrices((3, 3), "random", 2)
matriz_gen.generacion_matriz()
matriz_gen.generacion_matriz()

result = matriz_gen.multiplicar_matrices()
print("Resultado de la multiplicación:")
print(result)

matriz_gen.mostrar_matrices()

sums = matriz_gen.suma_elementos()
print("Suma de los elementos de las matrices:")
print(sums)


## Punto 2:

class Hola:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.__nombre} y tengo {self.__edad} años.")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

saludo = Hola(nombre, edad)

saludo.saludar()