import numpy as np

# dada uma matriz m x n, verificar se há números repetidos



m = int(input('digite um número de linhas: '))
n = int(input('digite um número de colunas '))

matriz = np.zeros((m,n))
p = m*n

print(f'digite os {p} elementos da matriz:')
for i in range(m):
    for j in range(n):
# i para linha e j pra coluna
        print(f'elemento [{i},{j}]')
        matriz[i,j] = int(input())

for i in range(m):
    for j in range(n):
# para cada elemento, checa-se se ele é igual a algum outro da própria matriz
        for i1 in range(m):
            for j1 in range(n):
                if ( (i != i1 and j != j1) and matriz[i,j] == matriz[i1,j1]):
                    print(f'{matriz[i,j]} se repete')
                    quit()

print(matriz)

    