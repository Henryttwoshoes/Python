a = float(input('Digite o primeiro valor '))
b = float(input('Digite o segundo valor '))
c = float(input('Digite o terceiro valor '))

# verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')