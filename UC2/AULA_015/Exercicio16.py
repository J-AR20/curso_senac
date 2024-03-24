# importando as bibliotecas necessarias para a atividade
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# caregando os dados
df_base = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')
print(df_base)

# rotinas de preprocessamento da base
# descobrindo os nomes das colunas da base de dados
nomes_colunas = df_base.columns
print(nomes_colunas)

# criando um df apenas com as séries de dados necessárias para a realização do exercício
df_carros_surrupiados = df_base[['recuperacao_veiculos','roubo_veiculo', 'ano']]
print(df_carros_surrupiados)

# recortando da base apenas os anos desejados
df_carros_surrupiados = df_carros_surrupiados[(df_carros_surrupiados['ano'] >= 2018) & (df_carros_surrupiados['ano'] <= 2023)]
print(df_carros_surrupiados.head())

#VISUALIZAR OS DADOS
# criando painel de visualização
fig = plt.subplots(2, 2, figsize=(15,10))

# título
plt.suptitle('Análise de dados de roubo e recuperação de veículos')

# gráfico 1 - roubo_veiculos
plt.subplot(2, 2, 1)
sns.boxplot(data = df_carros_surrupiados,
            x = 'ano',
            y = 'roubo_veiculo')
plt.title('Distribuição roubo de veículos por ano')


# gráfico 2 - recuperacao de veiculos
plt.subplot(2, 2, 2)
sns.boxplot(data = df_carros_surrupiados,
            x = 'ano',
            y = 'recuperacao_veiculos')
plt.title('Distribuição recuperacao de veículos por ano')
plt.tight_layout()
plt.show()


# Calculando médias e desvios padrão
medias_desvios = df_carros_surrupiados.groupby('ano').agg({'recuperacao_veiculos': 'mean', 'roubo_veiculo': 'mean'}).merge(
    df_carros_surrupiados.groupby('ano').agg({'recuperacao_veiculos': 'std', 'roubo_veiculo': 'std'}),
    left_index=True, right_index=True, suffixes=('_media', '_desvio_padrao'))

# Convertendo o índice para uma coluna
medias_desvios.reset_index(inplace=True)
