import random

n1 = str(input('1o: '))
n2 = str(input('2o: '))
n3 = str(input('3o: '))
n4 = str(input('4o: '))


lista = [n1, n2, n3, n4]

random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)