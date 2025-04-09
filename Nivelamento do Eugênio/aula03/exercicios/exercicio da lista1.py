# Soma dos numeros inteiros
soma = 0
n = int(input('Digite um número inteiro: '))
for i in range(n+1):
    soma += i

print(f'A soma dos números positivos até {n} é igual a {soma}.')