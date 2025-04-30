'''

Tupla - conjunto de valores

'''


t = (1,9,3.14, 'aula')
tuplaVazia = ()
print(t[0])
print(t[1:3]) # intervalo a partir do índice 1 e com indíce menor que 3
print(t[2:]) # começa no índice 2 e vai até o final
# t[0] = 0 -> dá erro pois não é permitido alterar o valor de um elemento da tupla
tAreoportos = ('JFK', 'GRU', 'CGN', 'CDG', 'KLA', 'KAT')
print(tAreoportos[3:])