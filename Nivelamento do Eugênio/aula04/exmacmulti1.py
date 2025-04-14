'''

while - usado para quando não há um número definido de repetições
'''
#  Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.
n = int(input('digite um número:'))
while n != 0 :
    print(n*n)
    n = int(input('digite mais um número:'))