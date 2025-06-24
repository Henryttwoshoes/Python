nome = str(input('Digite seu nome completo: '))
maiusculo = nome.upper()
minusculo = nome.lower()
junto1 = nome.split()
junto2 = ''.join(junto1)
qtletras = len(junto2)

nome1 = junto1[0]
qtnome1 = len(nome1)



print(f'Seu nome em maiúsculas é {maiusculo}')
print(f'Seu nome em minúsculas é {minusculo}')
print(f'Seu nome ao todo tem {qtletras} letras.')
print(f'Seu primeiro nome tem {qtnome1} letras.')