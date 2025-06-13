dias = int(input('Quantos dias ficou com o carro? '))
kms = float(input('Quantos quilômetros foram rodados? '))
total = (dias * 60) + (kms * 0.15)
print(f'O preço a pagar é {total:.2f}')