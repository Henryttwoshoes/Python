import pandas as pd

dados = {
    'Nome':['Alice','Robert','Carla'],
    'Idade':[25,30,35],
    'Status':['ativo','inativo','ativo']
}

df = pd.DataFrame(dados)
print(df)

# Apply()
def categoria_idade(idade):
    if idade <30:
        return 'Jovem'
    else:
        return 'Adulto'

df['Categoria_Idade'] = df['Idade'].apply(categoria_idade)

print(df)

# map()
mapeamento_status = {'ativo':'Ativo','inativo':'Inativo'}

df['Status'] = df['Status'].map(mapeamento_status)
print(df)

# Apply
df['Idade_Dobrada'] = df['Idade'].apply(lambda x : x *2)
print(df)