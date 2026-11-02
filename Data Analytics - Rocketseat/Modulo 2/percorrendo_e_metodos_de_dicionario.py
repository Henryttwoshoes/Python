# Percorrendo um dicionario
pessoas = {
    "nome": "Joaquim dos Santos Reis",
    "idade": 19,
    "altura": 1.79,
    "habilitado": False
}

print(pessoas)

for k in pessoas:
    print(pessoas[k])

# Impressão chave:valor
for k in pessoas:
    print(f"{k}:{pessoas[k]}")

# Método keys()
for chave in pessoas.keys():
    print(chave)

# Método values()
for valores in pessoas.values():
    print(valores)

# Método items()
for chave, valor in pessoas.items():
    print(f"{chave}:{valor}")

# Fazendo uma cópia de um dicionário
produto1 = {
    "id": 1045,
    "nome": "Notebook Dell",
    "preco": 3899.90,
    "estoque": 17,
    "categoria": "eletrônicos"
}

produto2 = produto1.copy()

print("PRODUTO 1==========")
print(produto1)

produto2.update({"id":"200000"})

print("PRODUTO 2==========")
print(produto2)