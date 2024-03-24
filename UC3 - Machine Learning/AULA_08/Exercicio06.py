#Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#endereço do conj. de dados
endereco = r'D:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_08'

#df com os dados de salário, 
salario = pd.read_excel(endereco + r'\dados_salarios.xlsx')
salario.info()

#definir as variáveis
x = ['Salário', 'Tempo de Casa (meses)', 'Idade']

# Para fazer clusterização precisamos normalizar os dados, trazendo-os para uma mesma escala 
# entre 0-1, o que reduz os desvios.  (Interessante porque a normalização pode ser utilizada para trabalhar com os dados que tenho de despesas_casa)

# Normalizar os dados
scaler = StandardScaler() # variável de normalização, ela que irá normalizar os dados

# Criar um conjunto de dados normalizado
salarioNormalizado = scaler.fit_transform(salario[[x[0], x[1], x[2]]]) # Aqui cada 'x' é uma das variáveis que iremos trabalhar
# Importante que os nomes das variáveis poderiam ter sido chamados no código acima ao invés do x[0], x[1].... 



print(salarioNormalizado)
#print(dados_rh.head())

'''
MÉTODO DE COTOVELO: IDENTIFICAR A QUANTIDADE DE CLUSTERS
O método serve para apontar qual a quantidade ideal de clusters os dados suportam
É para realizar somente 1 vez ou quando houver necessidade
'''

# # Criando a lista da inércia
# inercia = []

# # Criando o intervalo de valores k (cluster)
# valores_k = range(1,10)

# # Aplicar o Método de Cotovelo
# for k in valores_k:
#     #inicializar o modelo KMeans com o 'k' cluster
#     Kmeans = KMeans(n_clusters=k)

#     # Ajustar o modelo
#     Kmeans.fit(salarioNormalizado)

#     # Adicionar a inércia na lista
#     inercia.append(Kmeans.inertia_)

# # Plotar o gráfico

# plt.plot(valores_k,inercia)
# plt.xlabel('Qtd de clusters (k)')
# plt.ylabel('Inércia')
# plt.title('Método de Cotovelo')

# plt.show()


'''
MÉTODO DE COTOVELO: IDENTIFICAR A QUANTIDADE DE CLUSTERS
O método serve para apontar qual a quantidade ideal de clusters os dados suportam
É para realizar somente 1 vez ou quando houver necessidade
'''

#k clusters
#k = 3 (segundo avaliação do método)

# Definindo o número de clusters que iremos trabalhar
Kmeans = KMeans(n_clusters=3)

#Treinar o modelo
Kmeans.fit(salarioNormalizado)

# Adicionar os clusters ao df original (salario)
salario['cluster'] =Kmeans.labels_ # com isso adicionamos os rótulos dos clusters às séries de dados do df original

# Consolidar os dados do cluster
df_salario_cluster_media = salario.groupby('cluster')\
                                  .mean()\
                                  .reset_index()\
                                  .sort_values(x[0], ascending=False)

print(df_salario_cluster_media)



# Plotar em um gráfico
fig, ax = plt.subplots(figsize=(15,10),\
                       subplot_kw={'projection':'3d'})

tempo_casa = salario[x[1]]
idade = salario[x[2]]
vlr_salario = salario[x[0]]
cluster = salario['cluster']

ax.scatter(tempo_casa, idade, vlr_salario, c=cluster,cmap='viridis')

ax.set_xlabel('Tempo de casa (meses)')
ax.set_ylabel('Idade')
ax.set_zlabel('Salário')
plt.title('Clusters de Salário')

# Adicionar uma barra de cores
cbar = plt.colorbar(ax.scatter(tempo_casa, idade, vlr_salario, c=cluster,cmap='viridis'))
cbar.set_ticks(cluster.unique())

plt.tight_layout()
plt.show()


