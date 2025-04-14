# Dados dois números inteiros positivos, x e y, calcule x//y, mas sem utilizar o operador // Podemos resolver este problema usando o while, a subtração 10 // 3

x = int(input('Digite x:'))
y = int(input('Digite y:'))
resto = x
quociente = 0
while resto >= y :
    resto -= y
    quociente += 1
print(f'quociente = {quociente}')
print(f'resto = {resto}')