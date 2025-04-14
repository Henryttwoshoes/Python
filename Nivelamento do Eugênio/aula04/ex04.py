# Dado n, verificar se ele é triangular.1 * 2 * 3 2 * 3 * 4 3 * 4 * 5 ... até que o produto seja igual ou maior que n

n = int(input('digite n: '))
i = 1

while i * (i +1 ) * (i+2) < n:
    i += 1

if n == i * (i +1 ) * (i+2):
    print('n é triangular')
else:
    print('n não é triangular')