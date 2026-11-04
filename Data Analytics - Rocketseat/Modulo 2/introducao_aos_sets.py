# sintaxe de um set
frutas = {"banana","laranja","uva"}
print(frutas)
print(type(frutas))

# criando um set vazio
frutas1 = {} # X Acaba criando um dict
frutas1 = set() # V Cria um set vazio

# Não é possível utilizar valores duplicados em um set
print()
numeros = {1, 2, 3, 4, 4, 5, 1, 2, 5}
frutas = {"banana","laranja","uva","banana","banana"}

print(frutas)
print(numeros)

# Tamanho de um set
print(len(frutas))

# Acessando um item de um set
for x in frutas:
    print(x)

# Verificando a existência de um item em um set
if "melancia" in frutas:
    print(True)
else:
    print(False)

# Não é possível editar um elemento mas é possível adicionar novos elementos
frutas.add("melancia")
print(frutas)

# A função update também funciona mas itera sobre o que foi adicionado
numeros.update("Python")
print(numeros)

# Concatenando sets
frutas1 = {"banana","laranja"}
frutas2 = {"morango","kiwi"}

frutas1.update(frutas2)
print(frutas1) # :D

# Excluindo valores dentro de um set
frutas1.remove("laranja")
frutas.discard("kiwi")
print(frutas1)

# Verificando se duas listas são iguais

frutas1 = ["banana", "morango", "kiwi"]
frutas2 = ["morango", "morango", "banana", "kiwi", "kiwi", "banana", "morango"]

if frutas == frutas2:
    print(True)
else:
    print(False)
# -> FALSE

if frutas == set(frutas2):
    print(True)
else:
    print(False)
# -> TRUE
# Visto que set não permite valores repetidos

# Método clear