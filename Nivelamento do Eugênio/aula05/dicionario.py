# Dicionário: funciona como conjunto em que elementos tem uma chave para que sejam recuperados

d = {5:10, 3:'aaa', 'teste': 123, 'aaa': 'aaa'}
# (CHAVE) : {VALOR}


print(d.keys())
print(d.values())

for chave in d.keys():
    print(d[chave])