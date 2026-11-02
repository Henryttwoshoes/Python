pessoas = {
    "nome": "Sonia dos Santos",
    "idade": 32,
    "altura": 1.69,
    "habilitado": False
}

print(pessoas)
# Retornando um valor a partir de uma chave
print(pessoas.get("idade"))
# Retornando um dicionário de todas as chaves
print(pessoas.keys())
# Retornando todos os valores do dicionário
print(pessoas.values())
# Retornando uma tupla de todas chaves e itens
print(pessoas.items())
# Alterando valores no dicionario
pessoas.update({"altura":1.88, "idade": 42, "habilitado":True})
print(pessoas)
# Adicionando chaves e valores
pessoas["cpf"] = "000.000.000-00"
    # ou
pessoas.update({"rg":"55.555.555-55"})
print(pessoas)
# Removendo um item chave:valor
pessoas.pop("rg")
print(pessoas)
# Removendo o último item
pessoas.popitem()
print(pessoas)
# Utilizando del

# .clear também funciona

pessoas.clear()

del pessoas["cpf"]
del pessoas
print(pessoas)