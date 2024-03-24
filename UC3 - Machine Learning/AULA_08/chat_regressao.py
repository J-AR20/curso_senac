import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregando os dados
dados_rj = pd.read_csv('caminho_para_o_seu_arquivo.csv', sep=';', encoding='Windows-1254')
dados_rj = dados_rj[dados_rj['state'] == 'Rio de Janeiro'].dropna(subset=['area_m2', 'price_brl'])

# Normalizar os dados de interesse
scaler = StandardScaler()
colunas_analise = ['area_m2', 'price_brl']
dados_normalizados = scaler.fit_transform(dados_rj[colunas_analise])

# Aplicar K-Means com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
dados_rj['cluster'] = kmeans.fit_predict(dados_normalizados)

# Agrupar os dados por cluster e calcular a média para cada um
df_cluster_media = dados_rj.groupby('cluster').mean().reset_index().sort_values(by='area_m2', ascending=False)

# Preparar os dados para a plotagem
preco_brl = dados_rj['price_brl']
area_m2 = dados_rj['area_m2']
cluster = dados_rj['cluster']

# Plotagem
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw={'projection': '3d'})
scatter = ax.scatter(preco_brl, area_m2, c=cluster, cmap='viridis', label=cluster.unique())

ax.set_xlabel('Preço (BRL)')
ax.set_ylabel('Área (m²)')
ax.set_title('Clusters de Imóveis do RJ por Preço e Área')
plt.legend(*scatter.legend_elements(), title="Clusters")

plt.tight_layout()
plt.show()

# Exibir a média dos valores por cluster
print(df_cluster_media[['cluster', 'area_m2', 'price_brl']])
