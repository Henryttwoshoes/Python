import numpy as np

# COMO CRIAR ARRAYS
# Array com a função .array()
array1 = np.array([1,2,3,4,5,6])
print(array1)
print(type(array1))

# Criar matrizes
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)

# Arrays com 3 dimensões

array3 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

print(array3)

# Criando um array com n dimensões

array4 = np.array([1,2,3,4], ndmin=7)

print(array4)

# Verificando dimensões de um array

print(array4.ndim)

# NP Arange - Criar um array de 0 a 20
print()
array5 = np.arange(0,21,1)
print(array5)

# np.linspace

array7 = np.linspace(0,100,5)
print(array7)

# Criar um array com 5 zeros
array_zeros = np.zeros(5)
print(array_zeros)
print()
    # Com mais dimensões
array_zeros = np.zeros((5,3))
print(array_zeros)