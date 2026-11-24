import pandas as pd

df_vendas_a = pd.DataFrame({
    'Item':['TV','Geladeira','Fogão'],
    'Vendas_A':[100,50,30]
}, index=['TV','Geladeira','Fogão'])

df_vendas_b = pd.DataFrame({
    'Vendas_B':[80,60,20],
    'Estoque_B':[10,5,2]

}, index=['TV','Geladeira','Máquina de Lavar'])

print(df_vendas_a)
print(df_vendas_b)

# Left Join(Padrão)

left_join = df_vendas_a.join(df_vendas_b)


# Inner join
inner_join = df_vendas_a(df_vendas_b, how='inner')

# Outer Join
inner_join = df_vendas_a(df_vendas_b, how='outer')

# Right Join
inner_join = df_vendas_a(df_vendas_b, how='right')