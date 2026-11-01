cores = ["azul", "amarelo", "vermelho"]

print(cores)

print(len(cores))

cores.append("Verde")
print(cores)

cores.insert(0, "branco")
print(cores)

cores2 = ["laranja", "marrom"]

cores.extend(cores2)

print(cores)


cores.remove("marrom")
print(cores)

cores.pop()
print(cores)


del cores[0]
print(cores)

cores.clear()
print(cores)