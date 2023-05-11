import numpy as np
import matplotlib.pyplot as plt

def generar_matrices(tam):
    m_aleatoria = np.random.randint(1, 11, size=(tam, tam))
    m_cincos = np.ones((tam, tam)) * 5
    return m_aleatoria, m_cincos
# Generar las matrices
out1, out2 = generar_matrices(4)

# Sumar las matrices
suma = out1 + out2

# Graficar las filas de la matriz suma
fig, axs = plt.subplots(4, 1, figsize=(5,10))
for i in range(4):
    axs[i].bar(range(4), suma[i])
plt.show()
