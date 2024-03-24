import pandas as pd
import numpy as np

#endereco
endereco = r'C:\uc3_bigdata\dados'

#obter os dados
dados = pd.read_csv(endereco + r'\dados_producao_parafusos.csv')

#variável dependente
y_custo = dados['Custo de Produção (R$)'].values

#variável independente
x_qtde = dados['Quantidade Produzida (unidades)'].values

#importar a classe de treino e teste
from sklearn.model_selection import train_test_split

#dividir os dados de treino e teste
X_qtde_train, X_qtde_test, y_custo_train, y_custo_test = \
train_test_split(
    x_qtde,
    y_custo,
    test_size=0.2
    #shuffle=False
)

#importar a classe de regressão linear
from sklearn.linear_model import LinearRegression

#Modelo linear
modelo = LinearRegression()

#Treinando o modelo
#dados de treino
modelo.fit(X_qtde_train.reshape(-1,1), y_custo_train)

#Verificar a qualidade do treino
#dados de teste
score = modelo.score(X_qtde_test.reshape(-1,1), y_custo_test)

#Testar a análise preditiva
predicao = modelo.predict(X_qtde_test.reshape(-1,1))

#verificar o custo das qtdes 12000, 15000 e 20000
qtd_producao_pred = np.array([13000,17000,22000,25000])

#estimar o custo de produção
custo_producao_pred = modelo.predict(qtd_producao_pred.reshape(-1,1))

print(custo_producao_pred)
