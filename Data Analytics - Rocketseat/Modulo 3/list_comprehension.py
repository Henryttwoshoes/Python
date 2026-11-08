# Sintaxe
# [expressao for item in iteravel]

# Criando uma lista com os quadrados dos números de 1 a 10
    # Criando normalmente

lista_quadrados = []

for i in range(1,11):
    lista_quadrados.append(i**2)

print(lista_quadrados)

    # Criando com List Comprehension

quadrados = [i ** 2 for i in range(1,11)]
print(quadrados)

# Utilizando if else - Lista de números pares entre 1 e 20

pares = [i for i in range(1,21) if i % 2 ==0]
print(pares)

# Utilizando strings
frase = "amigo estou aqui."

palavras = [palavra.upper() for palavra in frase.split()]
print(palavras)

# Utilizando if else
par_impar = ["par" if i % 2 == 0 else "impar" for i in range(1,11)]

print(par_impar)