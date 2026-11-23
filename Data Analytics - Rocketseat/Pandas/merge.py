import pandas as pd

df_clientes = pd.DataFrame({
    'ID_Cliente':[1,2,3,4],
    'Nome':['João Paulo', 'Maria da Silva','Pablo Gomes','Iris da Costa'],

})

df_pedidos = pd.DataFrame({
    'ID_Pedido':[101,102,103,104,105],
    'ID_Cliente':[2,1,3,2,5],
    'Produto':['Livro','Caneta','Caderno','Mochila','Lápis']
})

print(f'df clientes:\n {df_clientes}')
print(f'df pedidos:\n {df_pedidos}')

# Inner Merge
merge_inner = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='inner')

print(f'Inner Merge:\n {merge_inner}')

# Left Merge
merge_left = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='left')

print(f'Left Merge:\n {merge_left}')

# Right Merge
merge_right = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='right')

print(f'Right Merge:\n {merge_right}')

# Outer Merge
merge_outer = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='outer')

print(f'Outer Merge:\n {merge_outer}')
# Retorna tudo e quem não tem correspondência recebe nulo