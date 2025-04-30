nota100 = 100.00
c100 = 0

nota50 = 50.00
c50 = 0

nota20 = 20.00
c20 = 0 

nota10 = 10.00
c10 = 0 

nota5 = 5.00
c5 = 0


valor = float(input('Digite o valor: '))

while valor >= nota100:
    valor = valor - 100
    c100 += 1

while valor >= 50:
    valor = valor - 50
    c50 += 1

while valor >= 20:
    valor = valor - 20
    c20 += 1

while valor >= 10:
    valor = valor - 10
    c10 += 1

while valor >= 5:
    valor = valor - 5
    c5 += 1

print(f'Cabe {c100} notas de 100 neste valor')
print(f'Cabe {c50} notas de 50 neste valor')
print(f'Cabe {c20} notas de 20 neste valor')
print(f'Cabe {c10} notas de 10 neste valor')
print(f'Cabe {c5} notas de 5 neste valor')