# Algoritmo para verificar se três números formam um triângulo retângulo

a = float(input('Digite o primeiro cateto: ')) # entrada
b = float(input('Digite o segundo cateto: ')) # entrada
c = float(input('Digite o último cateto: ')) # entrada
if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print('Os números formam um triângulo retângulo.')
else: 
    print('Os números não formam um triângulo retângulo.') 