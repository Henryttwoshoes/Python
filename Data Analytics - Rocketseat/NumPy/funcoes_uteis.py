import numpy as np
# Gerar números entre 0 e 1 - random().rand

numero = np.random.rand()
print(f'Número aleatório gerado: {numero}')
# Gerar arrays 1d aleatórios
array_1d = np.random.rand(5)
print(f'Arrays com 5 números aleatórios entre 0 e 1: {array_1d}')
# Gerar matriz 2x3 aleatória
matriz_2x3 = np.random.rand(2,3)
print(f'Matriz 2x3 de números aleatórios entre 0 e 1:\n {matriz_2x3}')

# Gerar numeros inteiros - random
numero = np.random.randint(10)
print(f'Número aleatório gerado: {numero}')

array_1d = np.random.randint(10, 21, size=3)
print(f'Arrays com 3 números aleatórios entre 10 e 20: {array_1d}')

matriz_2x2 = np.random.randint(1,101, size=(2,2))
print(f'Matriz 2x2 de números aleatórios:\n {matriz_2x2}')

# Escolher elementos aleatoriamente de um array existente - random.choice()
array_frutas = np.array(["maçã", "banana", "laranja", "limão", "abacaxi", "abacate"])
print()
print(f'Array de frutas: {array_frutas}')
print(f'Shape: {array_frutas.shape}')

fruta = np.random.choice(array_frutas)
print(f'Fruta aleatória escolhida: {fruta}')

frutas = np.random.choice(array_frutas, size=3)
print(f'Array com 3 elementos aleatórios: {frutas}')

# Outras funções
print()
array_original = np.array([1,5,10,5,3,8,2,2,1,10,7, 10])
print(f'Array original: {array_original}')
print(f'Shape: {array_original.shape}')

# Arrays com elementos únicos - unique()
array_unico = np.unique(array_original)
print(f'Array original com elementos únicos: {array_unico}')

# Verifica se há algum TRUE - any()
array1 = np.array([False, False, True, False])
array2 = np.array([False,False,False])
print()
print(np.any(array1))
print(np.any(array2))

# Verifica se todos são true - all()
array3 = np.array([True,True,True])
array4 = np.array([True,False,True])
print()
print(np.all(array3))
print(np.all(array4))

# Retorna uma cópia ordenada do array - np.sort()
array_numeros = array_original
print(f'Array de numeros: {array_numeros}')
array_ordenado = np.sort(array_numeros)
print(f'Array ordenado: {array_ordenado}')

array_numeros.sort() # MÉTODO -> modifica o array original ao invés de criar uma cópia

# Retorna os índices que ordenariam - np.argsort()

array_numeros = np.array([9,2,7,1,5,3])
array_indices = np.argsort(array_numeros)

print(f'Array de indices que ordenariam o array_numeros:\n {array_indices}')

# Ordenação de matrizes(linha ou coluna) 
matriz = np.array(([3,1,2],[6,5,4]))
print(f'Matriz não ordenada:\n {matriz}')
# Ordenar a matriz por linha
matriz_linha = np.sort(matriz, axis=1)
print(f'Matriz ordenada por linha:\n {matriz_linha}')
# Ordenar por coluna
matriz_coluna = np.sort(matriz, axis=0)
print(f'Matriz ordenada por coluna:\n {matriz_coluna}')