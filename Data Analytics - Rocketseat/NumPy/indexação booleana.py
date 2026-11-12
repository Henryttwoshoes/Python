import numpy as np
dados = np.arange(1,11)
print(dados)
# Criando uma condição
condicao = dados > 5
print(f'Array de condição: {condicao}')
# Pegando os elementos
elementos = dados[condicao]
print(elementos)
# Condições combinadas
# Elementos pares e maior do que 5
condicao1 = dados % 2 == 0
condicao2 = dados > 3

elementos = dados[condicao1 & condicao2]
print(elementos)

# Filtragem em matriz
matriz = np.array([[10,20,30],
                   [40,50,60],
                   [70,80,90]])
print()
print(matriz)
# Filtrar elementos maiores que 50
filtro = matriz > 50
print(matriz[filtro])

# CÓPIA & VISÃO
array_original = np.arange(1,6)
print(array_original)

# Criar uma visão(fatiamento)
print()
visao = array_original[1:4]
print(f'Array fatiado(Visão): {visao}')

visao[0] = 99
print(f'Array fatiado(Visão)[modificado]: {visao}')
print(f'Array original: {array_original}')
print("^^^^^^^^ALTEROU O ARRAY ORIGINAL!^^^^^")
array_original = np.arange(1,6)
# Criar uma cópia
array_copia = array_original.copy()
print(f'Array copia do original: {array_copia}')

array_copia[0] = 99
print(f'array copia(ALTERADO): {array_copia}')
print(f'Array original: {array_original}')