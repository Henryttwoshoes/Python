clientes = {
    "cliente1":{
        "nome":"Ana Paula",
        "idade":32,
        "email":"ana.paula@gmail.com",
        "cidade":"São Paulo"
    },
    "cliente2":{
            "nome":"Roberto Lima",
            "idade":45,
            "email":"roberto.lima@gmail.com",
            "cidade":"Rio de Janeiro"
        },
    "cliente3":{
                "nome":"Mariana Rocha",
                "idade":28,
                "email":"mariana.rocha@gmail.com",
                "cidade":"Curitiba"
            }
}
# Acessar os elementos do dicionario aninhado
print(clientes["cliente1"])
# Acessar o email do cliente1
print(clientes["cliente1"]["email"])
# Percorrendo um dicionario aninhado
for chave, valor in clientes.items():
    for chave2, valor2 in valor.items():
        print(f"{chave2}:{valor2}")
    print()

# Adicionando elementos em um dicionario aninhado
clientes["cliente4"] = {
    "nome":"José da Silva",
    "idade": 19,
    "email":"jose.silva@gmail.com",
    "cidade":"Fortaleza"
}

print()
print(clientes["cliente4"])
clientes["cliente4"]["cidade"] = "Recife"
print(clientes["cliente4"])

del clientes["cliente2"]
print(clientes)