km = float(input('Digite a distância: '))
if km <= 200.00:
    print(f'O preço da viagem é: {km*0.5:.2f}km')
elif km > 200.00:
    print(f'O preço da viagem é: {km*0.45:.2f}km')