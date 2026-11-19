import pandas as pd

dados = {
    'Produto':['A','B','C','D'],
    'Preco_Unitario':[10,20,15,25],
    'Quantidade_Vendida':[5,3,7,2]
}

df = pd.DataFrame(dados)
print(df)

df['Valor_Total'] = df['Preco_Unitario'] * df['Quantidade_Vendida']
print(df)

# Coluna com valor fixo
df['Desconto_Aplicado'] = 0.10
print(df)

# Renomear a coluna produto
df_novo = df.rename({'Produto':'Produto_Loja'})
print(df_novo)