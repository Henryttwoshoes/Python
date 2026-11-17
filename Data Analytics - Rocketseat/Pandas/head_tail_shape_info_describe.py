import pandas as pd

# Criando um DF
dados = {
    'Nome': ['Ana', 'Bruno', 'Carla','Daniel','Eduarda','Fernando','Gabriela','Hugo','Isabela','Julio'],
    'Idade':[22,35,28,41,29,33,25,45,30,38],
    'Cidade':['São Paulo','Rio de Janeiro','Belo Horizonte','Curitiba','Porto Alegre','São Paulo',' Rio de Janeiro','Fortaleza','Belém','Goiânia'],
    'Salario':[3000,5500,4000,7000,4200,6000,3500,8000,4800,6500]
}

df = pd.DataFrame(dados)
print(df)

# head() - Primeiras n linhas
print(df.head())

# tail() - Últimas n linhas
print(df.tail())

# shape - Retorna o shape do DF
print(df.shape)

# info() - Resumo do DataFrame
print(df.info())

# describe() - Retorna estatísticas sobre o DF
print(df.describe())