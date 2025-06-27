import random


numero = int(input('Digite um número: '))
lista = [1,2,3,4,5]

escolhido = random.choice(lista)

if numero == escolhido :
    print('Parabéns! Você acertou o número.')
else:
    print(f'Você errou, o número escolhido foi {escolhido}')