dia = int(input('Digite o dia '))
mes = int(input('Digite o mês '))
ano = int(input('Digite o ano '))

if dia > 30 or dia < 1 or mes < 1 or mes > 12 or ano > 2025 or ano < 1:
    print('Data inválida')
else:
    print('Data valida')