import numpy as np

# Empilhamento Vertical(vstack()) e horizontal(hstack())
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

# Empilhamento Vertical(vstack)
array_vertical = np.vstack((array1, array2))
print(f'Array vertical: {array_vertical}')
print(f'Shape do array vertical: {array_vertical.shape}')

# Empilhamento Horizontal(hstack)
array_horizontal = np.hstack((array1, array2))
print(f'Array Horizontal: {array_horizontal}')
print(f'Shape do array horizontla: {array_horizontal.shape}')

# Com matrizes
matriz1 = np.array([[1,2,3],
                    [4,5,6]])
matriz2 = np.array([[7,8,9],
                    [10,11,12]])

matriz_vertical = np.vstack((matriz1, matriz2))
print(f'Matriz vertical:\n{matriz_vertical}')

matriz_horizontal = np.hstack((matriz1, matriz2))
print(f'Matriz horizontal:\n{matriz_horizontal}')

# Funções mais gerais de combinação
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

# concatenate() - ao longo do eixo 0
array3 = np.concatenate((array1, array2), axis=0)
print(f'Arrays concatenados:\n {array3}')

matriz1 = np.array([[1,2,3],
                    [4,5,6]])
matriz2 = np.array([[7,8,9],
                    [10,11,12]])

# Matrizes ao longo do 0(linhas)
matriz3 = np.concatenate((matriz1, matriz2), axis=0)
print(f'Matrizes concatenadas pelo eixo 0(linhas):\n {matriz3}')
# Matrizes ao longo do 1(colunas)
matriz3 = np.concatenate((matriz1, matriz2), axis=1)
print(f'Matrizes concatenadas pelo eixo 1(colunas):\n {matriz3}')

# stack()
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array5 = np.stack((array1, array2))
array5 = np.stack((array1, array2), axis=0) # Possui um parâmetro para o eixo
print(f'Arrays concatenados:\n {array5}')

# DIVISÃO DE ARRAYS
array_original = np.arange(16)
print(f'Array original:\n {array_original}')

# Reshape - para 4 linhas e 4 colunas
array_reshape = array_original.reshape(4,4)
print(f'Array reshapado:\n {array_reshape}')

# Divisão Vertical - vsplit()
array_dividido = np.vsplit(array_reshape, 2)
print(f'Array dividido:\n {array_dividido}')
print(f'Primeira parte da divisão: {array_dividido[0]}')
print(f'Segunda parte da divisão: {array_dividido[1]}')

# Divisão Horizontal  - hsplit()
array_dividido = np.hsplit(array_reshape, 4)
print(f'Array dividido por colunas:\n {array_dividido}')
print(f'Primeira parte da divisão: {array_dividido[0]}')
print(f'Segunda parte da divisão: {array_dividido[1]}')
print(f'Terceira parte da divisão: {array_dividido[2]}')
print(f'Quarta parte da divisão: {array_dividido[3]}')

# Divisão genérica - split()
array_original = np.arange(10,90,10)
print(f'Array original:\n {array_original}')

# Dividir o array em 4 partes iguais
array_dividido = np.split(array_original, 4)
print(f'Array dividido em 4 partes:\n {array_dividido}')
print(f'Primeira parte da divisão: {array_dividido[0]}')
print(f'Segunda parte da divisão: {array_dividido[1]}')
print(f'Terceira parte da divisão: {array_dividido[2]}')
print(f'Quarta parte da divisão: {array_dividido[3]}')

matriz_original = np.arange(20)
print(f'Matriz original: {matriz_original}')

matriz_2d = matriz_original.reshape(4,5)
print(f'Matriz com reshape:\n {matriz_2d}')

# Dividir a matriz em 2 partes ao longo do eixo de linhas
matriz_split = np.split(matriz_2d, 2, axis=0)
print(f'Matriz dividida:\n {matriz_split}')
print(f'Primeira parte da divisão: {matriz_split[0]}')
print(f'Segunda parte da divisão: {matriz_split[1]}')

# Dividir a matriz em 5 partes ao longo do eixo de colunas
matriz_split = np.split(matriz_2d, 5, axis=1)
print(f'Matriz dividida:\n {matriz_split}')
print(f'Primeira parte da divisão: {matriz_split[0]}')
print(f'Segunda parte da divisão: {matriz_split[1]}')
print(f'Terceira parte da divisão: {matriz_split[2]}')
print(f'Quarta parte da divisão: {matriz_split[3]}')
print(f'Quinta parte da divisão: {matriz_split[4]}')