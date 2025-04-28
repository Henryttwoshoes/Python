# Dado um número n, checar se ele é primo

def ehprimo(n):
    for i in range(2, n): # passa por todos os números a partir de 2 até n
        # começa no 2 pois se começasse por 1 já ia dar True
        if n % i == 0: # se for divisível por i e dar 0, não é primo
            # o range(2, n) vai até n-1, ou seja, se for 7 vai só até 6
            return False
    return True # se não, é primo

print(ehprimo(7))

n = int(input('digite n: '))

cont = 0
soma = 0
p = 2
while cont < n:
    if ehprimo(p):
        soma += p
        cont += 1
    p += 1

print(soma)