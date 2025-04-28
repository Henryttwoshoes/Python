def calcularimc(peso, altura):
    return peso/(altura*altura)

peso = float(input('digite o peso:'))
altura = float(input('digite a altura:'))
imc = calcularimc(peso, altura)
print(f'O IMC é: {imc:.2f}')