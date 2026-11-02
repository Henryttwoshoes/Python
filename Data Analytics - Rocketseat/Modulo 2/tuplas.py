carros = ("Gol", "Voyage", "Fusca")
print(carros)
print(type(carros))

print(carros[0])

# Tuplas são imutáveis

# carros [0] = "hilux" # -> Dá erro

# Alterando dados em uma tupla

frutas = ("abacaxi", "banana", "limão", "laranja", "maracujá", "maçã")

print(frutas)

auxiliar = list(frutas) # Cast para fazer a conversão 

print(type(auxiliar))
print(auxiliar)

auxiliar[1] = "kiwi"

frutas = tuple(auxiliar)
print(frutas)

# Tuplas permitem elementos iguais

frutas = ("abacaxi", "abacaxi", "limão", "laranja", "maracujá", "maçã")

# Tamanho de uma tupla

print(len(frutas))

# Extraindo dados de uma tupla em variáveis

numeros = (10, 50, 14)

(n1, n2, n3) = numeros
i = 1
for n in numeros: 
    print(f"n{i} = {n}")
    i += 1

## Se não souber a quantidade

(n1, n2, *n3) = numeros

# Percorrendo uma tupla

for x in frutas:
    print(x)

# Juntando tuplas

tupla_final = frutas + numeros

print(tupla_final)

# Contar quanto de um mesmo dado há em uma tupla

print(tupla_final.count("abacaxi"))