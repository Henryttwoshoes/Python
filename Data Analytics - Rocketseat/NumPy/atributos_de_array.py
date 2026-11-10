import numpy as np

# dtype - indica o tipo de dado dos elementos armazenados no array

array1 = np.array([5,17,32,-50])
print(array1.dtype)
array1 = np.array([5.0,17.5,32,-50])
print(array1.dtype)
array1 = np.array([True, False])
print(array1.dtype)
array1 = np.array(["ASSSS", "ADSGSAGSF"])
print(array1.dtype)

# shape - retorna uma tupla indicando o número de elementos em cada dimensão

array_dimensao = np.array([10,43,22,9])
print(array_dimensao.shape)
print()
array_dimensao = np.array([1,2,34,45,5,6,7], ndmin=5)
print(array_dimensao.shape)

# size - Retorna o número total de elementos
print(array_dimensao.size)
# ndim - Retorna o número de dimensões
print(array_dimensao.ndim)

# Conversão de arrays

array2 = np.array([5,17,32,-50])
array1 = np.array([5.0,17.5,32,-50])
array_float = array1
print(array_float.dtype)

array_float = array_float.astype(int)
print(array_float)
print(array_float.dtype)