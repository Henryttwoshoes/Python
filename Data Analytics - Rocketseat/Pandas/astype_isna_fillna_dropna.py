import pandas as pd
import numpy as np

# Criar o DF
dados = {
    'Numero_String':['1','2','3','4'],
    'Preco_Float':[10.5,20.0,15.75,30.0]
}

df = pd.DataFrame(dados)
print(df)
df.info()

# Converter 'Numero String' para int
df['Numero_String'] = df['Numero_String'].astype(int)

df.info()

# Converter Preco_Float para int
df['Preco_Float'] = df['Preco_Float'].astype(int)
print(df)
df.info()

# Valores ausentes
df2 = pd.DataFrame({
    'A':[1,2,np.nan,4,5],
    'B':[np.nan,2,3,4,np.nan],
    'C':[1,2,3,4,5]
})

print(df2)

# isna() - Retorna um array de booleanos para ver se existem valores ausentes
print(df2.isna())

filtro_ausentes = df2[df2[['A', 'B', 'C']].isna().any(axis=1)]

print(filtro_ausentes)

# fillna - Preencher com 0 onde existem valoresn ulos
df_nulos = df2.fillna({'A':0})
print(df_nulos)

# fillna - preencher com a média de valores
df_media = df2.fillna(df2.mean()) # Retorna a média da coluna
print(df_media)

# dropna - Remover as linhas com valores ausentes
df_drop_linhas = df2.dropna()
print(df_drop_linhas)

df_drop_cols = df2.dropna(axis=1)
print(df_drop_cols)