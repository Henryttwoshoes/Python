import pandas as pd
import matplotlib.pyplot as plt
import unicodedata
from pathlib import Path


total_de_casos = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\Total de casos por ano.xlsx'

ocorrencia_por_raca = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\ocorrência por raça.xlsx'

casos_por_estado = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\Casos por Estado.xlsx'

caminho_de_salvamento = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\extração de gráficos\Casos por Estado'


tabela = pd.read_excel(
    casos_por_estado,
    sheet_name='Casos por Estado',
    usecols='A:AB',
    skiprows=1,
    nrows=14,
    header=None,
)

estados = tabela.iloc[0, 1:].tolist()
estados[22] = 'Rio Grande do Sul'
dados = tabela.iloc[1:].reset_index(drop=True)
anos = dados.iloc[:, 0].astype(int).astype(str)
pasta = Path(caminho_de_salvamento)
pasta.mkdir(parents=True, exist_ok=True)

for indice, estado in enumerate(estados, start=1):
    casos = dados.iloc[:, indice]
    fig, ax = plt.subplots(figsize=(10, 7))
    barras = ax.bar(anos, casos)
    rotulos = [f'{valor:,.0f}'.replace(',', '.') for valor in casos]
    ax.bar_label(barras, labels=rotulos, padding=3)
    ax.set_title(f'Casos de Dengue nos últimos 12 anos - {estado}')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Total de casos')
    ax.tick_params(axis='x', labelrotation=45)
    fig.tight_layout()

    nome_arquivo = unicodedata.normalize('NFKD', estado).encode('ascii', 'ignore').decode('ascii')
    if estado in ('Amapá', 'Paraná'):
        nome_arquivo = estado
    fig.savefig(pasta / f'{nome_arquivo}.png')
    plt.close(fig)