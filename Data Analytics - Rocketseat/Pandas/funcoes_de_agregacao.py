import pandas as pd

dados = {
    'Cidade':['São Paulo','Rio de Janeiro','São Paulo','Belo Horizonte','Rio de Janeiro','São Paulo'],
    'Vendas':[100,150,120,80,200,90],
    'Produto':['A','B','A','C','B','A']
}

df = pd.DataFrame(dados)
print(df)

# Agrupar por cidade e calcular soma das vendas
vendas_por_cidade = df.groupby('Cidade')['Vendas'].sum()

print(vendas_por_cidade)