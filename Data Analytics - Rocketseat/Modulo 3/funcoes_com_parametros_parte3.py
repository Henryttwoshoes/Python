# Utilizando um valor default
def imprimir_cidade(cidade="Nenhuma cidade definida."):
    print(cidade)

imprimir_cidade()

# Utilizando parâmetros de funções com lista
def imprimir_lista_frutas(frutas):
    print(frutas)
    print(type(frutas))

frutas = ["banana","laranja","abacaxi","maracujá"]

imprimir_lista_frutas(frutas)

# Utilizando parâmetros de funções com dicionários
def imprimir_cliente(clientes):
    print(clientes)
    print(type(clientes))

    for ind, valor in clientes.items():
        print(f"{ind}:{valor}")

cliente = {
    "nome":"Osvaldo da Silva",
    "idade":26,
    "cpf":"000.000.000-00"
}

imprimir_cliente(cliente)