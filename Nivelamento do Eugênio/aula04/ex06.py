# Número perfeito: igual a soma de seus divisores menores que ele mesmo: exemplo: 6 = 1 + 2 + 3 dado n

n = int(input('digite n: '))
soma = 0
divisor = 1
while divisor <= n//2:
    if n % divisor == 0:
        soma += divisor
    divisor += 1
if soma == n:
    print('número perfeito!')
else:
    print('número imperfeito!')