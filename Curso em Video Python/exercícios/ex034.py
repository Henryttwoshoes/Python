atual = float(input('Digite seu salário: '))
porcento = 0
if atual <= 1250.00 :
    porcento = 0.15
    novo = atual+(atual*porcento)
elif atual > 1250.00:
    porcento = 0.10
    novo = atual+(atual*porcento)


print(f'O novo salário é {novo:.2f} e o aumento foi de {porcento*100:.0f}%!')