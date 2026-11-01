carros = ["gol", "saveiro", "compass"]
print(carros)

for x in carros:
    print(x)

for x in range(len(carros)):
    print(carros[x])
# Se printar só x ele retorna os indíces

contador = 0
while contador < len(carros):
    print(carros[contador])
    contador += 1


print("\n============FATIAMENTO DE LISTAS============\n")
# ============FATIAMENTO DE LISTAS============

compras = ["arroz", "feijão", "farinha de trigo", "açúcar", "manteiga"]
print(compras)

print(compras[0:2])
print(compras[::])
print(compras[-1])
print(compras[2:4])
print(compras[1:6:2])
print(compras[-1::-1])