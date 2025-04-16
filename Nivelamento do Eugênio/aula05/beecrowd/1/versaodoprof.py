X = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    X[i] = int(input())

for i in range(10):
    if X[i] <= 0:
        X[i] = 1 # Altera o valor da posição i baseado na checagem anterior se o valor ter a condição

for i in range(10):
    print(f'X[{i}] = {X[i]}')