import pandas as pd
import random
from pandas import read_excel

def seleccionar_palabra_aleatoria(puede_ir_cualquier_cosa):
    # Leer el archivo de Excel con pandas
    df = pd.read_csv("Prueba.csv")
    
    # Convertir la columna de palabras en una lista de Python
    palabras = df['Palabras'].tolist()
    
    # Seleccionar una palabra aleatoria de la lista
    palabra_aleatoria = random.choice(palabras)
    
    return palabra_aleatoria

palabra_aleatoria = seleccionar_palabra_aleatoria('Prueba.csv')
print('La palabra aleatoria es:', palabra_aleatoria)

