# Faça um programa que lê 5 números, imprimindo a soma de todos os números no final
soma = 0 # é uma variável acumuladora

for i in range(5):
    n = int(input('digite um número: '))
    soma = soma + n

print(f'A soma dos números é {soma}')