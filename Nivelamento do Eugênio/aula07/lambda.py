# Lambda é uma função definida dentro da atribuição

x = lambda a: a + 1

print( x(3))

soma = lambda a,b: a + b
print(soma(10,20))

# Exemplo de uso de lambda:

def multiplicador(n):
    return lambda a: a * n

dobro = multiplicador(2)
triplo = multiplicador(3)