# Fatorial de um número
fatorial = 1
n = int(input('Digite um número inteiro: '))
for i in range(1,n+1):
    fatorial *= i

print(f'O fatorial de {n} é igual a {fatorial}.')