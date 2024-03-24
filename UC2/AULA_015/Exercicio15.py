import pandas as pd

# endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

# carga de dados
df_injuria = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/Base_Injuria_Preconceito.csv', sep=';', encoding='ISO-8859-1')

# dados de DP
df_dp = pd.read_csv(endereco + r'\DP.csv')

# relacionar os DFs qdo os nomes das colunas são diferentes
df_injuria_dp = pd.merge(df_injuria, df_dp, \
                         left_on='Cisp', right_on='codDP')

# totalizar Nome da DP por vítimas
# ordenar decrescentemente
df_vitimas_dp = df_injuria_dp[['nome','Vítimas']] \
                .groupby('nome').sum('Vítimas') \
                .sort_values('Vítimas',ascending=False) \
                .reset_index()

#TOP 10
df_vitimas_dp_top10 = df_vitimas_dp.head(10)

#VISUALIZAR OS DADOS
import matplotlib.pyplot as plt

# criar painel de visualização
fig = plt.subplots(1, 2, figsize=(15,10))

# título
plt.suptitle('Análise de dados')

# gráfico 1 - TOP 10
plt.subplot(1, 2, 1)
plt.bar(df_vitimas_dp_top10['nome'] \
        , df_vitimas_dp_top10['Vítimas'])
plt.title('Top 10 DPs')

#gráfico 2 - Distribuição
plt.subplot(1, 2, 2)
plt.boxplot(df_vitimas_dp['Vítimas'], labels=['Vítimas por DP'])
plt.title('Distribuição')

#ajustar o layout
plt.tight_layout()

#exibir
plt.show()