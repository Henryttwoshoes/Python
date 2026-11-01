# Criando listas
numeros = []

nomes = ['João', 'Maria', 'Joaquim']

numeros = [10, 30, 125]

alturas = [1.75, 1.69, 1.54]

x = ["José", 30, 1.98, True]

y = ["Laranja", ["limão", "morango"]]

print(nomes[0])
print(nomes[1])

print(nomes[-1])

# Verificando a existência de um item na lista

if "João" in nomes:
    print("O nome João está dentro da lista.")
else:
    print("O nome João não está dentro da lista.")

# Modificando o valor dentro de uma lista

frutas = ["laranja", "abacaxi", "morango"]
print(frutas)

frutas[1] = "maracujá"

print(frutas)