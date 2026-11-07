def potencia(valor):
    return valor**2

numero = potencia(10)

print(numero)

# Retornando valores de outros tipos
def retorna_texto(texto):
    return texto

print(retorna_texto("Python"))  

# Retornando estruturas de dados

def frutas():
    return ["banana","limão","abacate","uva"]


lista_frutas = frutas()

print(lista_frutas)
print(type(lista_frutas))

def dados_cliente():
    return {"nome":"Osvaldo", "idade":32, "cpf":"111.111.111-11"}

cliente = dados_cliente()

print(cliente)

# Utilizando pass
def funcao_a_ser_implementada():
    pass

# PARTE 2

# Bloqueando a utilização de parâmetros nomeados
def funcao_sem_parametros_nomeados(valor, /):
    print(valor)

# funcao_sem_parametros_nomeados(valor = 54)
# DÁ ERRO

# Bloqueando a utilização de parâmetros não-nomeados

def funcao_com_parametros_nomeados(*, valor):
    print(valor)

funcao_com_parametros_nomeados(valor = 4)