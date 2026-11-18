import pandas as pd

dados = {
    'Produto': ['A','B','C','D','E'],
    'Preco':[10.5,20.0,15.75,30.0,25.25],
    'Estoque':[100,50,75,20,90]

}

index = ['item1', 'item2','item3','item4','item5']

df = pd.DataFrame(dados, index)
print(df)
print()
print(df['Produto'])
print(df[['Produto', 'Estoque']])

# Loc
# Seleção do item 3
print(df.loc['item3'])
# Seleção de coluna
print()
print(df.loc[['item1','item5'],['Preco','Estoque']])
print()

# Iloc - para buscar o item 2
print(df.iloc[2])
# Iloc para linhas e colunas
print()
print(df.iloc[0:2, 1:3])