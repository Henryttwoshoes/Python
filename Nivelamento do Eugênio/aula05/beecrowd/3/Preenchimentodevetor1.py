# Beecrowd 1173
N = []
v = int(input('Digite v: '))
check = 0

for i in range(10):
    N.append(v) # Adiciona o valor atual de v à lista
    v *= 2 # Atualiza v para o próximo valor (v * 2)
    print(f'N[{i}] = {N[i]}')