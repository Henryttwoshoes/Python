import numpy as np
matriz_original = np.array([[1,2,3], [4,5,6]])

print(f'Matriz Original: {matriz_original}')
print(f'Shape da Matriz Original: {matriz_original.shape}')

# Transpondo a Matriz Original
matriz_transposta = matriz_original.T
print(f'Matriz Transposta: {matriz_transposta}')
print(f'Shape da Matriz Transposta: {matriz_transposta.shape}')

# flatten() vs ravel(): achatar Arrays
    # flatten -> retorna uma cópia do array original
    # ravel -> retorna uma visão do array original sempre que possível

matriz_original = np.array([[1,2,3], [4,5,6]])
print()
print('Matriz original:')
print(matriz_original)
matriz_copia = matriz_original.flatten()
print(f'Array achatado com flatten(): {matriz_copia}')
print("-----Retorna uma cópia")
print()
matriz_ravel = matriz_original.ravel()
print(f'Array achatado com ravel(): {matriz_ravel}')
print("-----Retorna uma visão sempre que possível")