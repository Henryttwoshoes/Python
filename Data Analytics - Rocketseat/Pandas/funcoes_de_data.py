import pandas as pd

df_datas = pd.DataFrame({
    'Data_String':['2023-01-01','2023-01-02','2023-01-03','2023-01-04'],
    'Evento':['Feriado','Reunião','Lançamento','Manutenção']
})

print(df_datas)

print(df_datas.dtypes)

# Converter Data_String para datetime
df_datas['Data'] = pd.to_datetime(df_datas['Data_String'])
print(df_datas)
print(df_datas.dtypes)

df_datas_formatos = pd.DataFrame({
    'Data':['01/01/2023','02-Jan-2023','20230103'],
    'Valor':[10,20,30]
})
print(df_datas_formatos)
print(df_datas_formatos.dtypes)

df_datas_formatos['Data_Convertida'] = pd.to_datetime(df_datas_formatos['Data'], format='mixed')
print(df_datas_formatos)
print(df_datas_formatos.dtypes)

df_partes_data = pd.DataFrame({
    'Timestamp': pd.to_datetime(['2023-01-15 10:30:00', '2023-02-20 14:00:00', '2023-03-25 08:45:00'])
})

print(df_partes_data)
print(df_partes_data.dtypes)

df_partes_data['Ano'] = df_partes_data['Timestamp'].dt.year
df_partes_data['Mês'] = df_partes_data['Timestamp'].dt.month
df_partes_data['Dia'] = df_partes_data['Timestamp'].dt.day
df_partes_data['Hora'] = df_partes_data['Timestamp'].dt.hour
df_partes_data['Dia da Semana'] = df_partes_data['Timestamp'].dt.dayofweek
print(df_partes_data)
print(df_partes_data.dtypes)

# Criar um DF
df2 = pd.DataFrame({
    'Data' : pd.to_datetime(['2023-01-01','2023-01-15', '2023-02-01','2023-02-10','2023-03-05','2023-03-20']),
    'Valor':[100,120,150,130,180,160]
})

print(df2)
print()
# Filtrar por uma data específica
data_filtro = df2[df2['Data'] == '2023-01-15']
print(data_filtro)
print()
data_filtro = df2[df2['Data'].dt.month == 2]
print(data_filtro)
print()
data_filtro = df2[(df2['Data'] >= '2023-01-01') & (df2['Data']<= '2023-02-15')]
print(data_filtro)
print()

# between()
data_filtro = df2[df2['Data'].between('2023-01-01','2023-02-15')]
print(data_filtro)