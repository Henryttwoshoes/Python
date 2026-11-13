import numpy as np
# reshape()
array_original = np.arange(12)
print(f'Array original: {array_original}')

# Remodelar para uma matriz com 3 linhas e 4 colunas
matriz_3x4 = array_original.reshape(3,4)
print(matriz_3x4)

# Remodelar para uma matriz 4 linhas e 3 colunas
print()
matriz_4x3 = array_original.reshape(4,3)
print(matriz_4x3)
# Remodelar para um array que contenha 2 linhas
print()
matriz = array_original.reshape(2,-1)
print(matriz)
# Remodelar para 3 dimensões
print()
array_3d = array_original.reshape(2,2,3)
print(f'array 3D: {array_3d}')

# Adicionando e Removendo Dimensões
# newaxis, expand_dims, squeeze
print()
array = np.array([1,2,3,4])
print(f'Array original: {array}')
print(f'Shape: {array.shape}')

# Adicionar uma nova dimensão
array_coluna = array[:, np.newaxis]
print(f'Array coluna: {array_coluna}')
print(f'Shape do array coluna: {array_coluna.shape}')

# Adicionar uma nova dimensão na linha com np.newaxis
array_linha = array[np.newaxis, :]
                            # : se refere a todos os elementos do array
print(f'Array linha: {array_linha}')
print(f'Shape do Array linha: {array_linha.shape}')

# Adicionando com o expand_dims
print(f'Array original: {array}')

array1 = np.expand_dims(array, axis=0)
print(f'Array 1: {array1}')

array2 = np.expand_dims(array1, axis=0)
print(f'Array 2: {array2}')

array3 = np.expand_dims(array, axis=1)
print(f'Array 3: {array3}')

# Removendo dimensões
array4 = np.squeeze(array2)
print(f'Array 2 com 1 dimensão removida: {array4}')