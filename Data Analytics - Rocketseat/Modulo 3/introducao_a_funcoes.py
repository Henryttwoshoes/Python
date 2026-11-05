def nome_da_funcao():
    print("DEUS")

nome_da_funcao()

def soma():
    n1 = int(input("Digite o 1° numero: "))
    n2 = int(input("Digite o 2° numero: "))
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")

soma()

n1 = 3
n2 = 4
def soma(valor1, valor2):
    soma = valor1 + valor2
    print(f"{valor1} + {valor2} = {soma}")

soma(n1, n2)

# Quando não se tem um numero definido de parametros

def funcao(*valores):
    print(valores)

# Parametros com nome

def imprime_dados(idade, nome, altura):
    print(f"A pessoa de nome {nome} possui altura {altura:.2f} e {idade} anos de idade.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite a sua altura: "))
# Referencia pela ordem de envio
imprime_dados(nome, idade, altura)
# Referencia pelo nome do parametro
imprime_dados(nome=nome, idade=idade, altura=altura)

# Kwargs
def funcao_com_key_wargs(**valores):
    print(valores)
    # Envia como um dicionário

# Percorrendo
def funcao_com_key_wargs(**valores):
    for x in valores.keys():
        print(x)

    for y in valores.values():
        print(y)

    for z in valores.items():
        print(z)

funcao_com_key_wargs(nome = "Osvaldo",  idade = 33, cpf = "000.000.000-00")