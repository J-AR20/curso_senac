import pandas as pd
import matplotlib.pyplot as plt

endereco = r'D:\BIG DATA - SENAC\UC2\AULA_05'
# r'' se chama 'raw string' que diz para o python o que são aquelas barras.. daí não precisamos corrigir na mão!!!!! 

df_veiculos = pd.read_excel(endereco + r'\veiculos.xlsx')

print(df_veiculos)

# Delimitar o dataframe por ano
df_ano = df_veiculos[['Ano','Roubo veículos', 'Furto veículos', 'Recuperação veículos']].groupby('Ano').sum()
print(df_ano)

# fazer a media
roubo_media = df_ano['Roubo veículos'].mean()
print(f'Média: {roubo_media}')

# Variancia
roubo_var = df_ano['Roubo veículos'].var()
print(f'Variancia: {roubo_var}')

# Desvio padrão
roubo_devp = df_ano['Roubo veículos'].std()
print(f'Desvio padrão: {roubo_devp}')

# O desvio padrão ajuda a entender o quanto um determinado conjunto de dados fica longe da média
# No nosso caso nós pudemos ver que o std() de quase 10.000 e uma média atual de 31.000
# Caso fosse normalizada, ela poderia ser 41.000 ou 21.000.. grosso modo, de forma erronea, o desvio padrão é tratado como "margem de erro"

# Visualizar o gráfico

plt.figure(figsize=(12,6))

#gráfico de barras
#definição do local do gráfico
plt.subplot(1, 2, 1) # uma linha, duas colunas e gráfico na posicao 1 (primeiro quadrante)
df_ano['Roubo veículos'].plot.bar(title='Roubo de veículos por ano')
plt.xlabel('Ano')
plt.ylabel('Total roubos')

#gráfico boxplot
#definição do local do gráfico
plt.subplot(1, 2, 2) # uma linha, duas colunas e gráfico na posicao 2 (segundo quadrante)
df_ano.boxplot(column=['Roubo veículos'])
plt.show()