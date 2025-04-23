import numpy as np

n = int(input('digite dimensão da matriz: '))
matriz = np.zeros((n,n))

p = n*n

print(f'digite os {p} elementos da matriz: ')
for i in range(n):
    for j in range(j):
        print(f'elemento matriz[{i},{j}]')
        matriz[i,j] = int(input)
permutacao = True
for i in range(n):
    contazero = 0
    contaum = 0
    for j in range(n):
        if matriz[i,j] == 1:
            contaum += 1
        if matriz[i,j] == 0:
            contazero += 1
    if contazero != n-1 and contaum != 1:
        permutacao = False

for i in range(n):
  contazero = 0
  contaum = 0
  for j in range(n):
    if matriz[j,i] == 1:
      contaum += 1
    if matriz[i,j] == 0:
      contazero += 1
  if contazero != n-1 and contaum != 1:
    permutacao = False

if permutacao:
  print('é permutação')
else:
   print('não é permutação')