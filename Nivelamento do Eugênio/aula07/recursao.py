# Recursão é quando uma função faz uma chamada para ela mesma Se for feita sem querer, normalmente provoca um loop infinito Cuidado com a recursão indireta, como abaixo:
def f():
  g()

def g():
  h()

def h():
  f()

