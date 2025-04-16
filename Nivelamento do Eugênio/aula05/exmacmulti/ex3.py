n = int(input('digite n: '))
v = []

for i in range(n):
    r = int(input())
    v = v + [r]
resultados = [0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    resultados[v[i]] += 1

print('frequências:')
for i in range(1, 7):
    print(f'{i}: {resultados[i]} vezes')