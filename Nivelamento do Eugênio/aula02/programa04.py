# Calculo de IMC com if, elif e else

peso = float(input('Digite o seu peso: ')) # entrada
altura = float(input('Digite a sua altura: ')) # entrada
imc = peso / (altura ** 2) # calculo
print("O seu IMC é:", imc) # saida
if imc < 18.5:
    print('Magro')
elif imc < 25:
    print('Normal')
elif imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')