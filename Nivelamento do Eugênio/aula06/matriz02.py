# MULTIPLICAÇÃO DE MATRIZES
'''

O número de colunas da primeira matriz deve ser o número de linhas da segunda

'''
import numpy as np


matriz34 = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])

matriz42 = np.array([[1,2],
                     [3,4],
                     [5,6],
                     [7,8]])

prod = np.dot(matriz34, matriz42)
print(prod)

matrizT = matriz42.T