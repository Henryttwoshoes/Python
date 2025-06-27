velocidade = int(input('Qual a velocidade do seu carro? '))
if velocidade <= 80:
    print('Dirija com segurança e tenha uma boa viagem.')
else:
    print(f'Você esta acima do limite e terá que pagar uma multa de R${(velocidade-80)*7:.2f}')