import pandas as pd
import matplotlib.pyplot as plt


total_de_casos = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\Total de casos por ano.xlsx'

ocorrencia_por_raca = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\ocorrência por raça.xlsx'

casos_por_estado = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\Casos por Estado.xlsx'

dados = pd.read_excel(
    total_de_casos,
    sheet_name='Total de casos',
    usecols='A:B',
    skiprows=3,
    nrows=13,
    header=None,
    names=['Ano', 'Casos'],
)

plt.figure(figsize=(10, 7))
barras = plt.bar(dados['Ano'].astype(str), dados['Casos'])
rotulos = [f'{valor:,.0f}'.replace(',', '.') for valor in dados['Casos']]
plt.bar_label(barras, labels=rotulos, padding=3)
plt.title('Total de casos por ano')
plt.xlabel('Ano')
plt.ylabel('Total de casos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()