# 1) Importação das bibliotecas necessárias ao desenvolvimento da entrega:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2) Carregamento dos dados
df_base = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')

# 3) Rotinas de preprocessamento da base
# 3.1) Descobrindo os nomes das colunas da base de dados
nomes_colunas = df_base.columns
print(nomes_colunas)

# 3.2) Criando um df auxiliar APENAS com o recorte temporal e séries de dados necessárias ao desenvolvimento da entrega
df_carros_surrupiados = df_base[['recuperacao_veiculos', 'roubo_veiculo', 'ano']].query("2018 <= ano <= 2023")
print(df_carros_surrupiados)

# 4) Visualização de dados
# Iniciando a figura para visualização
plt.figure(figsize=(15, 10))

# Título geral
plt.suptitle('Análise de dados de roubo e recuperação de veículos')

# Gráfico 1 - roubo_veiculos
plt.subplot(2, 2, 1)  # Define o primeiro subplot na grade 2x2
sns.boxplot(data=df_carros_surrupiados, x='ano', y='roubo_veiculo')
plt.title('Distribuição roubo de veículos por ano')

# Gráfico 2 - recuperacao de veiculos
plt.subplot(2, 2, 2)  # Define o segundo subplot na grade 2x2
sns.boxplot(data=df_carros_surrupiados, x='ano', y='recuperacao_veiculos')
plt.title('Distribuição recuperação de veículos por ano')

# Calculando médias e desvios padrão
medias_desvios = df_carros_surrupiados.groupby('ano').agg({'recuperacao_veiculos': ['mean', 'std'], 'roubo_veiculo': ['mean', 'std']})
medias_desvios.columns = ['recuperacao_veiculos_media', 'recuperacao_veiculos_desvio_padrao', 'roubo_veiculo_media', 'roubo_veiculo_desvio_padrao']
medias_desvios.reset_index(inplace=True)
medias_desvios['ano'] = medias_desvios['ano'].astype(int).astype(str)  # Convertendo o ano para texto

# Tabelas de médias e desvios padrão
# Recuperação de Veículos
plt.subplot(2, 2, 3)  # Define o terceiro subplot na grade 2x2
plt.axis('off')  # Desativa os eixos para este subplot
plt.table(cellText=medias_desvios[['ano', 'recuperacao_veiculos_media', 'recuperacao_veiculos_desvio_padrao']].round({'recuperacao_veiculos_media': 2, 'recuperacao_veiculos_desvio_padrao': 4}).values,
          colLabels=['Ano', 'Média', 'Desvio Padrão'], loc='center', cellLoc='center')
plt.title('Recuperação de Veículos: Média e Desvio Padrão por Ano')

# Roubo de Veículos
plt.subplot(2, 2, 4)  # Define o quarto subplot na grade 2x2
plt.axis('off')  # Desativa os eixos para este subplot
plt.table(cellText=medias_desvios[['ano', 'roubo_veiculo_media', 'roubo_veiculo_desvio_padrao']].round({'roubo_veiculo_media': 2, 'roubo_veiculo_desvio_padrao': 4}).values,
          colLabels=['Ano', 'Média', 'Desvio Padrão'], loc='center', cellLoc='center')
plt.title('Roubo de Veículos: Média e Desvio Padrão por Ano')

# Ajustando o layout e exibindo os gráficos
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajusta o layout para deixar espaço para o título principal
plt.show()