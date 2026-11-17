import pandas as pd

caminho = r"C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Data Analytics - Rocketseat\Pandas\ANÁLISE CENSO DO RPG.xlsx"

df = pd.read_excel(caminho)
print(df.head())

df3 = pd.DataFrame({
  'Fruta': ['Maçã', 'Banana', 'Laranja'],
  'Quantidade':[100,150,120]  
})

df3.to_excel('Frutas.xlsx', index=False)