import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path


ocorrencia_por_raca = r'C:\Users\pc-henrique\Documentos locais\Programação\Repositórios\Python\Planilhas de Analise de Dados\Dengue - separadas\ocorrência por raça.xlsx'
pasta_saida = Path(ocorrencia_por_raca).parents[1] / 'extração de gráficos' / 'Casos por raça'

tabela = pd.read_excel(
    ocorrencia_por_raca,
    sheet_name='Ocorrência por Raça',
    usecols='A:H',
    skiprows=1,
    nrows=14,
    header=None,
)

categorias = tabela.iloc[0, 1:-1].tolist()
categorias = ['Indígena' if categoria == 'Indigena' else categoria for categoria in categorias]
dados = tabela.iloc[1:].reset_index(drop=True)
anos = dados.iloc[:, 0].astype(int)
cores = plt.colormaps['tab10'].colors

fig, ax = plt.subplots(figsize=(12, 7))
for indice, categoria in enumerate(categorias):
    ax.plot(
        anos,
        dados.iloc[:, indice + 1],
        color=cores[indice],
        marker='o',
        linewidth=2,
        label=categoria,
    )

totais_por_raca = dados.iloc[:, 1:-1].sum()
fig_acumulado, ax_acumulado = plt.subplots(figsize=(13, 7))
barras_acumulado = ax_acumulado.bar(
    categorias,
    totais_por_raca.values,
    color=cores[:len(categorias)],
)
rotulos_acumulados = [f'{valor:,.0f}'.replace(',', '.') for valor in totais_por_raca]
ax_acumulado.bar_label(barras_acumulado, labels=rotulos_acumulados, padding=4)
ax_acumulado.set_title(f'Total acumulado por raça ({anos.iloc[0]}–{anos.iloc[-1]})')
ax_acumulado.set_xlabel('Raça')
ax_acumulado.set_ylabel('Total acumulado de casos')
ax_acumulado.tick_params(axis='x', labelrotation=25)
ax_acumulado.yaxis.set_major_formatter(FuncFormatter(lambda valor, _: f'{valor:,.0f}'.replace(',', '.')))
ax_acumulado.grid(axis='y', linestyle='--', alpha=0.4)
fig_acumulado.tight_layout()
fig_acumulado.savefig(pasta_saida / 'grafico_total_acumulado_por_raca.png', dpi=150)

plt.show()
