import pandas as pd

dados = {
    'Produto':['Maçã','Banana','Laranja','Uva','Pera'],
    'Preco':[2.50,1.80,3.00,4.20,2.10],
    'Quantidade':[100,150,75,200,120]
}

df = pd.DataFrame(dados)

# Ordenar por preço em ordem crescente
df_preco = df.sort_values(by='Preco',)
print(df_preco)

# Ordenar por quantidade em ordem decrescente
df_qtd = df.sort_values(by='Quantidade', ascending=False)
print(df_qtd)

df_multi = df.sort_values(by=['Preco', 'Quantidade'], ascending=[True, False])
print()
print(df_multi)