import pandas as pd

# Criando um DataFrame a partir de um dicionário
dados = {
    'Nome':['Alice','Eduardo','Carlos','Davi'],
    'Idade':[25,30,19,27],
    'Cidade':['São Paulo','Curitiba','Natal','Fortaleza']
}

print(dados)

df = pd.DataFrame(dados)
print(df)
print()
# Acessando uma coluna específica do DF
print(df.Nome)
# ou
print(df['Cidade'])

# Criar um DF a partir de uma lista de dicionários

list_dict = [
    {'Nome': 'Rodrigo', 'Idade': '28', 'Cidade':'Belém'},
    {'Nome': 'Osvaldo', 'Idade': '43', 'Cidade':'Goiás'},
    {'Nome': 'Priscila', 'Idade': '20', 'Cidade':'Rio de Janeiro'},
]

df2 = pd.DataFrame(list_dict)
print()
print()
print(df2)