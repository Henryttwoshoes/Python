import math

def calcularAreaCirculo(raio):
  area = math.pi * raio ** 2
  return area

r = float(input('digite o raio:'))
a = calcularAreaCirculo(r)
print(f'a área do círculo com raio {r} é {a}')