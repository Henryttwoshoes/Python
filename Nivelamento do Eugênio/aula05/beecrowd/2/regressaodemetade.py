# Beecrowd 1178

N = []
v = float(input())
N = N + [v]

for i in range(1,100):
    v = N[i-1]/2
    N = N + [v]

for i in range(100):
    print(f'N[{i}] = {N[i]:.4f}')

# .Xf -> determina o números de casas decimais do float