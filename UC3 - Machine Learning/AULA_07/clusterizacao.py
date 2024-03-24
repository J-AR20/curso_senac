import pandas as pd
import matplotlib.pyplot as plt

#obter os dados
ocorrencias = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                    , sep=';', encoding='ISO-8859-1')

endereco = r'D:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_07'

populacao = pd.read_excel(endereco + r'\populacao_rj.xlsx')

#preparar dados
populacao['Cidade'] = populacao['Cidade'].str.replace(r' (RJ)','')

#ocorrência: CVLI, Munic
ocorrencias = ocorrencias[['munic','cvli']].groupby('munic') \
                .sum('cvli').reset_index()

#juntar geral num braço só
OcorrenciaPopulacao = ocorrencias.merge(populacao, \
                                        left_on='munic', \
                                        right_on='Cidade')

#print(OcorrenciaPopulacao.head())

'''
CLUSTERIZAÇÃO
'''
#variáveis quantitativas que serão
#utilizadas na clusterização
#mesmo nome da coluna correspondente ao dataframe
x = ['cvli','Densidade demográfica (Habitante por quilômetro quadrado)'\
     ,'Área da unidade territorial (Quilômetros quadrados)']

#delimitar o dataframe para a clusterização
OcorrenciaPopulacao = OcorrenciaPopulacao[['Cidade',x[0],x[1],x[2]]]

#importar bibliotecas
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#criar um variável para normalização
scaler = StandardScaler()

#normalizar os dados, das variáveis quantitativas
OcorrenciaPopulacao_normalizado = scaler.\
            fit_transform(OcorrenciaPopulacao[[x[0],x[1],x[2]]])

'''#######################
# IDENTIFICAR QTDE DE CLUSTERS
#######################
inercia = []

#iniciar o intervalo
valores_k = range(1,10)

#aplicar o método de cotovelo
for k in valores_k:
    #inicializar o modelo de kmeans
    kmeans = KMeans(n_clusters = k)

    #treinar o conjunto de daos
    kmeans.fit(OcorrenciaPopulacao_normalizado)

    #adicionar a inércia na lista
    inercia.append(kmeans.inertia_)

#plotar o gráfico
plt.plot(valores_k,inercia)
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inércia')
plt.title('Método de cotovelo: Identificação de número de clusters')

plt.show()
####################
# FIM  
###################'''

#definir a quantidade de clusters
#quantidade definida a partir do método de cotovelo
kmeans = KMeans(n_clusters=4)

#treinar o modelo para separar os 4 clusters
kmeans.fit(OcorrenciaPopulacao_normalizado)

#adicionar a coluna 'Cluster' no DF Original
OcorrenciaPopulacao['Cluster'] = kmeans.labels_

#criar um DF com a média de CVLI e Densidade por cluster
df_cluster_media = OcorrenciaPopulacao.groupby('Cluster')\
    .mean(x[0],x[1]).reset_index().sort_values(x[0],ascending=False)

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
print(df_cluster_media)

# pegar o padrão identificado e localizar em SP
# cidades que estejam nesse padrão
populacao_sp = pd.read_excel(endereco + r'\populacao_sp.xlsx')

populacao_sp = populacao_sp[(populacao_sp[x[1]] >= 4000) & \
                            (populacao_sp[x[1]] <= 6500) & \
                            (populacao_sp[x[2]] >= 90) &
                            (populacao_sp[x[2]] <= 1300)]

print(populacao_sp['Cidade'].unique())

#VISUALIZAR DADOS
plt.scatter(OcorrenciaPopulacao[x[0]], \
            OcorrenciaPopulacao[x[1]],
            c=OcorrenciaPopulacao['Cluster'],
            cmap='viridis')

plt.xlabel(x[0])
plt.ylabel(x[1])
plt.show()