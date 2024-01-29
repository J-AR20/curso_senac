import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo = 'D:/CURSOS/BIG DATA - SENAC/UC2/AULA_05/veiculos.xlsx' # computador de casa
caminho_arquivo = 'xxxyyy/UC2/AULA_05/veiculos.xlsx' # computador do trabalho
caminho_arquivo = 'penDrive/UC2/AULA_05/veiculos.xlsx' # p trabalhar do Senac

# Carregar o arquivo Excel em um DataFrame
dados = pd.read_excel(caminho_arquivo)

# Conhecendo a base de dados
print("Visão geral dos dados:")
print(dados.head())  # Mostra as primeiras linhas do DataFrame

# Quais são as categorias que temos:
reg = dados["Regiao"].unique()
print(reg) # Baixada Fluminense, Capital, Grande Niterói, Interior

years = dados["Ano"].unique()
print(years) # Últimos 20 anos, de 2003 a 2023

# Modificar os nomes das colunas para ser mais facil trabalhar
novas_colunas = ['ano', 'regiao', 'roubo', 'furto', 'recuperacao']
dados.columns = novas_colunas

print(dados.head())
