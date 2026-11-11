import numpy as np

array1 = np.array([1,2,3,4,5])

# AS QUE EU JÁ SEI
soma = array1.sum()
media = array1.mean()
desv_pad = array1.std()


# min
minimo = array1.min()
print(minimo)
# max
maximo = array1.max()
print(maximo)
# argmax - Retorna o índice(ou indices) do maior valor ao longo de um eixo
indice = array1.argmax()
print(indice)