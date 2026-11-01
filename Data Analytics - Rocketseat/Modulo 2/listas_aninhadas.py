colaboradores = [ 
    ["Nome", "Cargo", "Departamento"],
    ["Alice", "Analista", "Financeiro"],
    ["Carlos", "Gerente", "Vendas"],
    ["Julia", "Estagiária", "RH"]
]

print(colaboradores)

# Acessendo um item da lista aninhada
print(colaboradores[2][1])

# Modificando um elemento da lista aninhada
print(colaboradores[1][1])
colaboradores[1][1] = "Coordenadora"
print(colaboradores[1][1])
# Percorrendo listas
for x in colaboradores:
    for y in x:
        print(y, end=" ")
    print()

for dados in colaboradores[1:]:
    nome, cargo, departamento = dados # atribui os valores em sequência
    print(f"{nome} trabalha como {cargo}, no departamento de {departamento}")