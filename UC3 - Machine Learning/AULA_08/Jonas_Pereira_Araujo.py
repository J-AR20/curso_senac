# Importando as bibliotecas necessárias para a tarefa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregando os dados
dados = pd.read_csv(r'E:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_08\Brasile-real-estate-dataset.csv',\
                     sep=';',\
                     encoding='Windows-1254')

# Selecionando os dados
dados_rj = dados[dados['state'] == 'Rio de Janeiro']
# Manter apenas as colunas 'area_m2' e 'price_brl'
dados_rj = dados_rj[['area_m2', 'price_brl']]
print(dados_rj.head())



# 1.      Etapa de pré-processamento e exploração da base de dados
# 1.1.    Operação para retirar os NA da análise
dados_filt = dados_rj.dropna()
# Verificando a presença de valores NA ou NaN em cada coluna
valores_na = dados_rj.isna()
print(valores_na)

# Contando quantos valores NA ou NaN existem em cada coluna
contagem_na = dados_filt.isna().sum()
print("\nContagem de NA ou NaN por coluna:")
print(contagem_na)

# 1.2.    Verificando a correlação entre as variáveis de interesse e salvando-a num objeto
corr_preco_m2 = dados_filt['area_m2'].corr(dados_filt['price_brl'])
print(corr_preco_m2)




# 2.      Tarefa: Identificar os perfis de preço e m² dos imóveis do RJ
# 2.1.   Definindo as variáveis a serem utilizadas nesta tarefa
x = ['area_m2', 'price_brl']

# 2.2.    Criação da variável de normalização dos dados
scaler = StandardScaler() 

# 2.3.    Criando um conjunto de dados normalizados a partir do método de normalização
dados_filt_Normalizado = scaler.fit_transform(dados_filt[[x[0], x[1]]])
# print(dados_filt_Normalizado)

# # 2.4.  Implementação do método de cotovelo para descobrir com base nos dados 
# # a qtd ideal de clusters. Tal seção depois de implementada será comentada. 

# # 2.4.1. Criando a lista da inércia
# inercia = []

# # 2.4.2. Criando o intervalo de valores k (cluster)
# valores_k = range(1,10)

# # 2.4.3. Aplicando o Método de Cotovelo nos dados
# for k in valores_k:
#     #inicializar o modelo KMeans com o 'k' cluster
#     Kmeans = KMeans(n_clusters=k)

#     # Ajustar o modelo
#     Kmeans.fit(dados_filt_Normalizado)

#     # Adicionar a inércia na lista
#     inercia.append(Kmeans.inertia_)

# # 2.4.5. Plotando o gráfico do método de cotovelo que mostrará graficamente a qtd ideal de clusters
# plt.plot(valores_k,inercia)
# plt.xlabel('Qtd de clusters (k)')
# plt.ylabel('Inércia')
# plt.title('Método de Cotovelo')
# plt.show()

## k clusters
## k = 3 (segundo avaliação do método)

# 2.5.   Criando uma instância do algoritmo K-Means com a especificação que os
# nossos dados deverão estar divididos em 3 grupos (ou clusters)
Kmeans = KMeans(n_clusters=3)

# 2.5.1. Treinando os nossos dados a partir do modelo K-means padronizado em 3k
Kmeans.fit(dados_filt_Normalizado)

# 2.5.2. Adicionando os clusters ao df original
# Serve para adicionarmos os rótulos dos clusters às séries de dados do df original
dados_filt['cluster'] = Kmeans.labels_ 
print(dados_filt.head())

# 2.6.   Agrupar os dados por cluster e calcular a média para cada um
df_cluster_media = dados_filt.groupby('cluster')\
                              .mean()\
                              .reset_index()\
                              .sort_values(by='area_m2', ascending=False)

# 2.6.1. Exibir a média dos valores por cluster
print(df_cluster_media[['cluster', 'area_m2', 'price_brl']].round())

# 2.7.   Preparando os dados para visualização dos dados
preco_brl = dados_filt['price_brl']
area_m2 = dados_filt['area_m2']
cluster = dados_filt['cluster']

# 2.7.1. Plotando um gráfico
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw={'projection': '3d'})
scatter = ax.scatter(preco_brl, area_m2, c=cluster, cmap='viridis', label=cluster.unique())

ax.set_xlabel('Preço (BRL)')
ax.set_ylabel('Área (m²)')
ax.set_title('Clusters de Imóveis do RJ por Preço e Área')
plt.title('Clusters do preço preditivo')

# 2.7.2. Adicionar uma barra de cores
cbar = plt.colorbar(ax.scatter(preco_brl, area_m2, c=cluster,cmap='viridis'))
cbar.set_ticks(cluster.unique())

plt.tight_layout()
plt.show()


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregando o shapefile dos municípios do RJ
municipios_rj = gpd.read_file(r'E:/BIG DATA - SENAC/UC3 - Machine Learning/AULA_08/RJ_Municipios_2022/RJ_Municipios_2022.shp')

# Carregando os dados dos imóveis
dados_imoveis = pd.read_csv(r'E:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_08\Brasile-real-estate-dataset.csv',\
                     sep=';',\
                     encoding='Windows-1254')

dados_imoveis = dados_imoveis[dados_imoveis['state'] == 'Rio de Janeiro']

# Normalizando os dados de interesse (área e preço) para a clusterização
scaler = StandardScaler()
dados_imoveis.dropna(subset=['area_m2', 'price_brl'], inplace=True)
dados_normalizados = scaler.fit_transform(dados_imoveis[['area_m2', 'price_brl']])

# Criando os clusters
kmeans = KMeans(n_clusters=3)
dados_imoveis['cluster'] = kmeans.fit_predict(dados_normalizados)

# Limpar e converter as colunas de coordenadas para float
dados_imoveis['lat'] = dados_imoveis['lat'].str.replace('.', '').str.replace(',', '.').astype(float)
dados_imoveis['lon'] = dados_imoveis['lon'].str.replace('.', '').str.replace(',', '.').astype(float)

# Corrigir os valores de latitude e longitude
dados_imoveis['lat'] = dados_imoveis['lat'].apply(lambda x: float(str(x).replace('.', '').replace(',', '.')))
dados_imoveis['lon'] = dados_imoveis['lon'].apply(lambda x: float(str(x).replace('.', '').replace(',', '.')))

# Corrigir as latitudes que parecem ter um erro de digitação e deveriam ser negativas
dados_imoveis['lat'] = dados_imoveis['lat'].apply(lambda x: -x if x > 0 else x)

# Agora você pode criar o GeoDataFrame
gdf_imoveis = gpd.GeoDataFrame(dados_imoveis, geometry=gpd.points_from_xy(dados_imoveis.lon, dados_imoveis.lat))


fig, ax = plt.subplots(figsize=(12, 12))

# Plotar o shapefile dos municípios do RJ
municipios_rj.plot(ax=ax, color='white', edgecolor='black')

# Depois de plotar o shapefile
ax.scatter(gdf_imoveis.geometry.x, gdf_imoveis.geometry.y, s=50, c=gdf_imoveis['cluster'].map({0: 'red', 1: 'green', 2: 'blue'}))

# # Plotar os dados dos imóveis com um tamanho de marcador visível
# gdf_imoveis.plot(ax=ax, markersize=50, color=gdf_imoveis['cluster'].map({0: 'red', 1: 'green', 2: 'blue'}), legend=True)

# Ajustar os limites dos eixos após a plotagem dos dados dos imóveis
ax.set_xlim(-45, -40)
ax.set_ylim(-24, -20)

plt.title('Clusters de Imóveis do RJ por Preço e Área')
plt.show()




# 3.     Tarefa: Verificar a possibilidade de criar um modelo de predição dos preços dos imóveis
# no estado do RJ, baseando-se nos dados de preço e m²

# 3.1.   Criando Modelo de Regressão Linear para descobrir qt o Preço dos Imóveis é afetado pelo m² no Rio de Janeiro
# Definindo variáveis X e Y

# 3.1.1. Variável dependente - Área dos imóveis
X = dados_filt['area_m2'].values.reshape(-1,1)

# 3.1.2. Variáveis independente - Área dos imóveis em metros quadrados
Y = dados_filt['price_brl'].values

# 3.1.3. Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# 3.1.4. Criando e treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train.reshape(-1,1), Y_train)

# 3.1.5. Avaliando o modelo
score = modelo.score(X_test, Y_test)
previsoes = modelo.predict(X_test)

# 3.1.6. Testando a análise preditiva
y_predicao = modelo.predict(X_test.reshape(-1,1))

# 3.1.7. Simulando diferentes tamanhos de imóvel
areas_pred = np.array([52, 300, 700, 1000]).reshape(-1, 1)

# 3.1.8. Previsões dos preços dos imóveis simulados
preco_pred = modelo.predict(areas_pred).round()
print(preco_pred)

# 3.2.   Plotando os resultados
# 3.2.1. Regressao linear
plt.subplot(1,2,1)
plt.scatter(X_test, Y_test, color='gray')
plt.plot(X_test, previsoes, color='red', linewidth=2)
plt.xlabel('Área (m²)')
plt.ylabel('Preço (BRL)')
plt.title(f'Correlação entre preço e metro quadrado no Rio de Janeiro \n\
          Score: {score:.2f}\n\
          Correlação: {corr_preco_m2:.2f}')

# Tabela com os dados simulados 'preco_pred'
# vamos primeiramente juntar os dados simulados com os dados do conjunto de dados

# 3.2.2. Inserir dados da predição num dataframe (numa biblioteca) para utilizar na tabela do painel de visualização
df_preco_pred = pd.DataFrame({
    'M² do imóvel': areas_pred.flatten(),  # Achatando o array para torná-lo unidimensional
    'Preço do imóvel': preco_pred.flatten()  # Achatando o array para torná-lo unidimensional
})

# 3.2.3. Erro médio quadrático 
from sklearn.metrics import mean_squared_error # serve para mostrar o valor do erro qd cria a linha de regressão
rmse = np.sqrt(mean_squared_error(Y_test, y_predicao))

# 3.2.4. Criando a Tabela com os valores dos imóveis preditivos
plt.subplot(1,2,2)
table = plt.table(
    cellText=df_preco_pred.values.astype(int),
    colLabels=df_preco_pred.columns,
    loc='center',
    cellLoc='center'
)
table.set_fontsize(16)
table.scale(1, 1.5)
plt.title('Previsão de preço dos imóveis')
plt.title(f'Previsão de preço dos imóveis. RMSE: {round(rmse, 0)}')
plt.axis('off')

plt.tight_layout()
plt.show()