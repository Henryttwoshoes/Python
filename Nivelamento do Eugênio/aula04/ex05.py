# MDC
# Dados dois números inteiros, calcular o MDC entre eles
x = int(input('digite um número: '))
y = int(input('digite outro número: '))
p = x 
q = y
r = p % q
while r != 0:
    p = q
    q = r
    r = p % q
print(f'o MDC entre {x} e {y} é {q}')