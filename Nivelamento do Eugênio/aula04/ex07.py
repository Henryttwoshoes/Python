# Escreva um programa que imprime todos os milhares (4 algarismos) cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima.

for n in range(10000):
    x = n % 100
    y = n // 100
    if ((x + y)*2) == n:
        print(n)
