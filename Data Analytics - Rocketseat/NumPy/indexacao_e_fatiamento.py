import numpy as np
# INDEXAÇÃO
# Array de 1 dimensão
array1 = np.arange(10,60,10)
print(array1)
print(array1[1])
# Array de 2 dimensões
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)
print(array2[1][0])
print(array2[1,2])
# FATIAMENTO
# Sintaxe [inicial, final-1: passo]
array = np.arange(10)
print(array)
# Fatiar do indice 2 ao 5
fat = array[2:6:1]
print(fat)
print(array[2:6:1])
# 2 dimensões
print(array2[0:2,1:3])