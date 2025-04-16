# Dados n números inteiros, imprimir na ordem inversa da leitura

n = int(input('digite n: '))
v = []


for i in range(n):
    x = int(input('digite um número '))
    v = v + [x]

for i in reversed(range(n)):
    print(v[i])