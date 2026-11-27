import colorsys
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter


casos_por_estado = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\Casos por Estado.xlsx'
caminho_de_salvamento = Path(
    r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\extração de gráficos\Casos por Estado'
)

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
anos = dados.iloc[:, 0].astype(int)
cores = [
    colorsys.hsv_to_rgb((indice * 0.61803398875) % 1, 0.8, 0.85)
    for indice in range(len(estados))
]

fig, ax = plt.subplots(figsize=(18, 10))
for indice, estado in enumerate(estados):
    ax.plot(
        anos,
        dados.iloc[:, indice + 1],
        color=cores[indice],
        marker='o',
        linewidth=1.5,
        label=estado,
    )

ax.set_title(f'Casos de dengue por estado ({anos.iloc[0]}–{anos.iloc[-1]})')
ax.set_xlabel('Ano')
ax.set_ylabel('Total de casos')
ax.set_xticks(anos)
ax.tick_params(axis='x', labelrotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(lambda valor, _: f'{valor:,.0f}'.replace(',', '.')))
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.legend(title='Estado', bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
fig.tight_layout()

caminho_de_salvamento.mkdir(parents=True, exist_ok=True)
fig.savefig(caminho_de_salvamento / 'grafico_de_linhas.png', dpi=150, bbox_inches='tight')
plt.show()