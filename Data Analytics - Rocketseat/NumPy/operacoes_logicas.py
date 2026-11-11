import numpy as np

array1 = np.array([10,20,30,40,50])
array2 = np.array([5,20,35,40,45])

# Igualdade
igual = array1 == array2
print(igual)
# Maior que
maior_que = array1 > array2
print(maior_que)
# Maior ou igual a
maior_ou_igual = array1 >= array2
print(maior_ou_igual)
# Menor que
menor_que = array1 < array2
print(menor_que)
# Menor ou igual a
menor_ou_igual = array1 <= array2
print(menor_ou_igual)

# OPERADORES LÓGICOS
array1 = np.array([True, False, True])
array2 = np.array([False, False, True])

# AND
array_and = array1 & array2
    # ou
np.logical_and(array1,array2)
# OR
array_or = array1 | array2
print(array_or)
# NOT
array_not = ~array1
print(array_not)

# Filtrar elementos
dados = np.array([1,5,10,15,20,25])

filtro = dados > 10

print(f"Array filtrado: {filtro}")
# Usar o filtro para selecionar elementos
elementos_filtrados = dados[filtro]
print(f"Elementos filtrados: {elementos_filtrados}")