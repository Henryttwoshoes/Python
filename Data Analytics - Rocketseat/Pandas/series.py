import pandas as pd
# Criando uma series a partir de uma lista
numeros = [10,20,30,40,50]

serie1 = pd.Series(numeros)

print(serie1)
print(type(serie1))

# Acesar um elemento da série
print(serie1[3])

# Criar uma Series com índice personalizado
lista_numeros = [100,200,300]
index = ['A', 'B', 'C']

serie_personalizada = pd.Series(lista_numeros, index)
print(serie_personalizada['C'])

# Criar uma series a partir de um dicionario
dados ={'primeiro':1,
       'segundo':2,
       'terceiro':3}
print(dados)

serie_dict = pd.Series(dados)
print(serie_dict)