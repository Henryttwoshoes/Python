import random

n1 = input('')
n2 = input('')
n3 = input('')
n4 = input('')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}')