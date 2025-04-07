# ALGORITMO DE ORDENAÇÃO COM 3 NÚMEROS
a = int(input('Digite o primeiro número: ')) # entrada
b = int(input('Digite o segundo número: ')) # entrada 
c = int(input('Digite o terceiro número: ')) # entrada

if (a <= b and b <= c):
    print(a, b, c)
elif (a <= c and c <= b):
    print(a, c, b)
elif (b <= a and a <= c):
    print(b, a, c)
elif (b <= c and c <= a):
    print(b, c, a)
elif (c <= a and a <= b):
    print(c, a, b)
else:
    print(c, b, a)