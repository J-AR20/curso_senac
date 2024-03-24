import pandas as pd

# carga de dados
df_injuria = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/Base_Injuria_Preconceito.csv', sep=';', encoding='ISO-8859-1')

# Filtrar o dataframe por Injúria por preconceito
df_inj_preconceito = df_injuria[df_injuria['Titulo'] == 'Injúria por preconceito']

# 1.	Ranking através do sexo, do total de vítimas 
df_vitimas_sexo = df_inj_preconceito[['Sexo','Vítimas']]

# Totalizar vítimas por sexo
df_vitimas_sexo = df_vitimas_sexo.groupby('Sexo').sum('Vítimas') \
                    .sort_values('Vítimas', ascending=False)

# 2.	Ranking através da cor, do total de vítimas
df_vitimas_cor = df_inj_preconceito[['Cor','Vítimas']]

# Totalizar vítimas por cor
df_vitimas_cor = df_vitimas_cor.groupby('Cor').sum('Vítimas') \
                    .sort_values('Vítimas', ascending=False)

# 3.	Ranking da idade, do total de vítimas
df_vitimas_idade = df_inj_preconceito[['Idade','Vítimas']]

# Totalizar vítimas por cor
df_vitimas_idade = df_vitimas_idade.groupby('Idade').sum('Vítimas') \
                    .sort_values('Vítimas', ascending=False)

# 4.	A evolução do total de vítimas ao longo dos meses
#df_vitimas_mes = df_inj_preconceito[['Mês','Vítimas']]

# Totalizar vítimas por cor
df_vitimas_mes = df_inj_preconceito[['Mês','Vítimas']].groupby('Mês') \
                    .sum('Vítimas').sort_values('Mês', ascending=False)

# visualizar os resultados em um painel de gráficos
# Importar bibliotecas na parte superior do script
import matplotlib.pyplot as plt

# criar o painel de gráficos
fig = plt.subplots(2, 2, figsize = (15,10))

# Título do painel
plt.suptitle('Análise de dados', fontsize=14, color='blue')

# gráfico #1
plt.subplot(2,2,1)
plt.bar(df_vitimas_sexo.index,df_vitimas_sexo['Vítimas'])
plt.title('Vítimas por sexo')

# gráfico #2
plt.subplot(2,2,2)
plt.bar(df_vitimas_cor.index,df_vitimas_cor['Vítimas'])
plt.title('Vítimas por cor')

# gráfico #3
plt.subplot(2,2,3)
plt.bar(df_vitimas_idade.index,df_vitimas_idade['Vítimas'])
plt.title('Vítimas por idade')

# gráfico #4
plt.subplot(2,2,4)
plt.plot(df_vitimas_mes.index,df_vitimas_mes['Vítimas'])
plt.title('Evolução por mês')

# ajustar o layout
plt.tight_layout()

# exibir o painel
plt.show()