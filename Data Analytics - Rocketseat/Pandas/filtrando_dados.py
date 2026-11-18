import pandas as pd
dados = {
    'Nome': ['Alice','Roberto','Carlos','Davi','Everaldo','Franklin'],
    'Idade':[25,30,35,40,28,32],
    'Cidade':['São Paulo','Goiania','Fortaleza','Campina Grande','Campinas','São Paulo'],
    'Pontuacao':[85,92,78,95,88,70]
}

df = pd.DataFrame(dados)
print(df)
print()
# Filtrar pessoas com idade maior que 30
filtro_idade = df[df['Idade'] < 30]
print(filtro_idade)
print()

# Cidade São Paulo e pontuação > 80
filtro_cid_pont = df[(df['Cidade'] == 'São Paulo') & (df['Pontuacao'] > 80)]
print(filtro_cid_pont)
print()
# Cidade Fortaleza ou Campina Grande
filtro_cidade = df[(df['Cidade'] == 'São Paulo') | (df['Cidade'] == 'Campina Grande')]
print(filtro_cidade)
print()
# isin()

filtro_isin = df[df['Cidade'].isin(['Goiânia','Campinas','São Paulo'])]

print(filtro_isin)