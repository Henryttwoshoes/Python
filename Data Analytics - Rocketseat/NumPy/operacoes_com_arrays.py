import numpy as np

array1 = np.arange(1,5)
array2 = np.arange(5,9)

# Soma

soma = array1 + array2
print(soma)

# Subtração
subtracao = array1 - array2

print(subtracao)

# Multiplicao
multi = array1*array2
print(multi)

# Divisao
div = array1/array2
print(div)

# Potência
pot = array1**4
print(pot)


# OPERAÇÕES COM ESCALAR

array = np.array([10,20,30,40,50,60])
numero = 5

soma = array + numero
print(soma)

multi = array1*numero
print(multi)

# Broadcasting
array1 = np.array([[1,2,3], [4,5,6]])
print(array1)
print(array1.shape)

array2 = np.array([10,20,30])
print(array2)
print(array2.shape)

soma = array1 + array2
print(soma)