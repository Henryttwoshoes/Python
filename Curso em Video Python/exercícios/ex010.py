# 1 dólar = 3,27

reais = float(input('Digite o seu dinheiro em reais '))
dolar = float(round(reais/3.27, 2))

print(f'Com R${reais} você pode comprar U${dolar}')