a = {1,2,3}
b = {3,4,5}
c = {7,8,9}
d = {1,2,5,8,9}


print(a)
print(b)
print(c)
print(d)
print()
# Copy
aux = a.copy()
print(aux)
print()
# Método união(union)
a = {1,2,3}
b = {3,4,5}
    # 1a forma
aux = a.union(b)
print(aux)
    # 2a forma
aux = a | b
print(aux)

# Interseção
a = {1,2,3}
d = {1,2,5,8,9}
    # 1a forma
aux = a.intersection(d)
print(aux)
    # 2a forma
aux = a & d
print(aux)

# Diferença
c = {7,8,9}
d = {1,2,5,8,9}
    # 1a forma
aux = c.difference(d)
print(aux)
    # 2a forma
aux = c - d
print(aux)

# Diferença simétrica
a = {1,2,3}
b = {3,4,5}
    # 1a forma
aux = a.symmetric_difference(b)
print(aux)
