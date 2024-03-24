import pandas as pd
import numpy as np

#obter os dados
dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                    , sep=';', encoding='ISO-8859-1')

#excluir dados de 2024
dados = dados[dados['ano'] <= 2023]

#variável dependente
y_cvli = dados['cvli'].values

#variáveis independentes
x_hom_letalidade = dados[['hom_doloso','letalidade_violenta']].values

#importar a classe de treino e teste
from sklearn.model_selection import train_test_split

#dividir os dados de treino e teste
X_hom_letalidade_train, X_hom_letalidade_test, y_cvli_train, y_cvli_test = \
train_test_split(
    x_hom_letalidade,
    y_cvli,
    test_size=0.2,
    shuffle=False
)

#importar a classe de regressão linear
from sklearn.linear_model import LinearRegression

#Modelo linear
modelo = LinearRegression()

#Treinando o modelo

#    y = a1*    x1     + a2*      x2            + b
# cvli = a1*hom_doloso + a2*letalidade_violenta + b


modelo.fit(X_hom_letalidade_train.reshape(-1,2), y_cvli_train) # importante no reshape -1 é todas as linhas e o 2 são as duas colunas das variáveis independentes que estamos treinando

#Verificar a qualidade do treino: 0 a 1
#dados de teste
score = modelo.score(X_hom_letalidade_test.reshape(-1,2), y_cvli_test)
print('Coeficiente angular = ', modelo.coef_)
print('Coeficiente linear (intercepto): ', modelo.intercept_)
print('Score: ', score)


#Testar a análise preditiva
y_predicao = modelo.predict(X_hom_letalidade_test.reshape(-1,2))


#simular as qtds de homicídio e letalidade violenta
qtd_hom_letalidade_pred = np.array([
                                     [12,15], 
                                     [23,25], 
                                     [27,32]
                                     ])

#estimar o cvli
cvli_pred = modelo.predict(qtd_hom_letalidade_pred)
print(cvli_pred.round())


#Erro médio quadrático 
from sklearn.metrics import mean_squared_error # serve para mostrar o valor do erro qd cria a linha de regressão
rmse = np.sqrt(mean_squared_error(y_cvli_test, y_predicao))


# VISUALIZAÇÃO DE DADOS
# PRIMEIRA COISA É AVISAR PARA O PYTHON QUE OS DADOS SÃO TRIDIMENSIONAIS

import matplotlib.pyplot as plt 

fig, ax = plt.subplots(figsize=(15,10), subplot_kw={'projection': '3d'})

# utilizaremos primeiro somente os dados de homicídio (todas as linhas e indice zero)
hom_doloso = X_hom_letalidade_test[:,0]
# após utilizaremos os dados de letalidade violenda (todas as linhas e indice um)
letalidade_violenta = X_hom_letalidade_test[:,1]

ax.scatter(hom_doloso,letalidade_violenta,y_predicao,color='blue')
ax.plot_trisurf(hom_doloso,letalidade_violenta,y_predicao,color='red',alpha=0.5)

ax.set_xlabel('Hom. doloso')
ax.set_ylabel('Letalidade violenta')
ax.set_zlabel('CVLI predição')

plt.title('CVLI Preditivo')


plt.tight_layout()
plt.show()

