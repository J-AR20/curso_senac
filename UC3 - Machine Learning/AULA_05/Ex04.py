import pandas as pd
import numpy as np

#obter os dados
dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv' \
                    , sep=';', encoding='ISO-8859-1')

valores_unicos = dados['upp'].unique()
print(valores_unicos) # UPP desejada 'Vila Kennedy'

# Selecionando os dados
dados_upp_vk = dados[dados['upp'] == 'Vila Kennedy']
print(dados_upp_vk.head())

# Selecionando apenas o crimes
crimes_vk = dados_upp_vk.iloc[:,4:23].join(dados_upp_vk.iloc[:,24:25]).join(dados_upp_vk.iloc[:,26:41])
# preciso checar e ver se isso deu ou não certo!!!!! 
print(crimes_vk.head())

# correlação multipla
correlacao = crimes_vk.corr()

# filtrar correlacao acima de 0.80
correlacao = correlacao[correlacao >= 0.80]

#exportar para o excel
endereco = r'D:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_05'
correlacao.to_excel(endereco + r'\correlacao_upp_vk.xlsx')




#variável dependente
y_roubo_transeunte = crimes_vk['roubo_transeunte'].values

#variáveis independentes
X_roubos_desagregados = crimes_vk[['roubo_veiculo','roubo_celular']].values

#importar a classe de treino e teste
from sklearn.model_selection import train_test_split

#dividir os dados de treino e teste
X_roubos_desagregados_train, X_roubos_desagregados_test, y_roubo_transeunte_train, y_roubo_transeunte_test = \
train_test_split(
    X_roubos_desagregados,
    y_roubo_transeunte,
    test_size=0.2,
    shuffle=False
)

#importar a classe de regressão linear
from sklearn.linear_model import LinearRegression

#Modelo linear
modelo = LinearRegression()

#Treinando o modelo

#    y             = a1*    x1        + a2*      x2            + b
# roubo_transeunte = a1*roubo_veiculo + a2*roubo_celular       + b


modelo.fit(X_roubos_desagregados_train.reshape(-1,2), y_roubo_transeunte_train) # importante no reshape -1 é todas as linhas e o 2 são as duas colunas das variáveis independentes que estamos treinando

#Verificar a qualidade do treino: 0 a 1
#dados de teste
score = modelo.score(X_roubos_desagregados_test.reshape(-1,2), y_roubo_transeunte_test)
print('Coeficiente angular = ', modelo.coef_)
print('Coeficiente linear (intercepto): ', modelo.intercept_)
print('Score: ', score)


#Testar a análise preditiva
y_predicao = modelo.predict(X_roubos_desagregados_test.reshape(-1,2))


#simular as qtds de roubo de veiculo e roubo de celular
qtd_roubo_veiculo_celular_pred = np.array([
                                     [100,356], 
                                     [156,400], 
                                     [200,350]
                                     ])

#estimar o cvli
roubo_transeuntes_pred = modelo.predict(qtd_roubo_veiculo_celular_pred)
print(roubo_transeuntes_pred.round())


# #Erro médio quadrático 
# from sklearn.metrics import mean_squared_error # serve para mostrar o valor do erro qd cria a linha de regressão
# rmse = np.sqrt(mean_squared_error(y_cvli_test, y_predicao))


# VISUALIZAÇÃO DE DADOS
# PRIMEIRA COISA É AVISAR PARA O PYTHON QUE OS DADOS SÃO TRIDIMENSIONAIS

import matplotlib.pyplot as plt 

fig, ax = plt.subplots(figsize=(15,10), subplot_kw={'projection': '3d'})

# utilizaremos primeiro somente os dados de roubo de celular (todas as linhas e indice zero)
roubo_celular = X_roubos_desagregados_test[:,0]
# após utilizaremos os dados de letalidade violenda (todas as linhas e indice um)
roubo_veiculo = X_roubos_desagregados_test[:,1]

ax.scatter(roubo_celular,roubo_veiculo,y_predicao,color='blue')
ax.plot_trisurf(roubo_celular,roubo_veiculo,y_predicao,color='red',alpha=0.5)

ax.set_xlabel('Roubo celular')
ax.set_ylabel('Roubo veículo')
ax.set_zlabel('Roubo a transeuntes predição')

plt.title('Roubo a transeuntes PREDITIVO')


plt.tight_layout()
plt.show()