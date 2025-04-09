n = int(input('digite um número '))
maior = n

for i in range(4):
    n = int(input('digite um número '))
    if n > maior:
        maior = n


print(f'o maior número é {maior}.')