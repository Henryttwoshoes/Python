import numpy as np

# Matriz com 3 linhas e 4 colunas:

matriz34 = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])

matriz32zeros = np.zeros((5,4))

matrizId = np.eye(3)

print(matrizId)

print(matriz34)
print(matriz34[1,2])
print(matriz32zeros)

# Usando o caractere : seleciona-se toda a coluna escolhida

print(matriz34[:,1])
print(matriz34[1,:])