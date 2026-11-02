carros = {}

pessoas = {
    "nome": "Joaquim da Silva",
    "idade": 32,
    "altura": 1.88,
    "habilitado": True

}

print(pessoas)
print(type(pessoas))

print(pessoas["nome"])
print(pessoas["idade"])
print(pessoas["altura"])
print(pessoas["habilitado"])

# Não aceita valores duplicados

carro = {
    "nome": "Gol",
    "marca": "Volkswagen",
    "modelo": "G5"
} # Retorna a primeira ocorrência do dado duplicado

print(carro)
# Modificando o dicionario

carro["modelo"] = "G2"

print(carro)
# Tamanho
print(len(carro))