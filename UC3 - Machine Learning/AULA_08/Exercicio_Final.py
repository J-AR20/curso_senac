# Importando bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#importar a classe de treino e teste
from sklearn.model_selection import train_test_split
#importar a classe de regressão linear
from sklearn.linear_model import LinearRegression

#endereço do conj. de dados
endereco = r'E:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_08'

#df com os dados de salário, 
dados = pd.read_csv(endereco + r'\Brasile-real-estate-dataset.csv', sep=';', encoding='Windows-1254')
print(dados.head())

# Ps.: Tentei com mais de um encoding e palavras com acentos continuaram vindo com problemas de acentuação

# Descobrindo quais dados de estado a base de dados possui
dados_state_names = dados['state'].unique()
print(dados_state_names)

# ['Pernambuco' 'Piauí' 'Rio Grande do Norte' 'Rio Grande do Sul'
#  'Rio de Janeiro' 'Rondônia' 'Santa Catarina' 'Sergipe' 'São Paulo'
#  'Tocantins']

# Filtrando apenas os dados do 'Rio de Janeiro'
df_rj = dados[dados['state'] == 'Rio de Janeiro']
print(df_rj)

# Dados necessários
# area_m2
# price_brl

# Aplicando mais um filtro para ficar apenas com os dados quantitativos a serem trabalhados
dados_filt = df_rj[['area_m2', 'price_brl']]
print(dados_filt.head())

# Limpeza/ajuste dos dados
# Ajustando os valores para o padrão brasileiro

# # Função para formatar os valores numéricos para o padrão brasileiro
# def formatar_para_br(valor):
#     return f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# # Aplicando a formatação para duas colunas
# for coluna in ['area_m2', 'price_brl']:
#     dados_filt[coluna] = dados_filt[coluna].apply(formatar_para_br)

# print(dados_filt.head())

# Operação para retirar os NA da análise
dados_filt = dados_filt.dropna()
# Verificando a presença de valores NA ou NaN em cada coluna
valores_na = dados_filt.isna()
print(valores_na)

# Contando quantos valores NA ou NaN existem em cada coluna
contagem_na = dados_filt.isna().sum()

print("DataFrame indicando presença de NA ou NaN:")
print(valores_na)
print("\nContagem de NA ou NaN por coluna:")
print(contagem_na)

# Verificando a correlação entre as variáveis
corr_preco_m2 = dados_filt['area_m2'].corr(dados_filt['price_brl'])
print(corr_preco_m2)



# Criando Modelo de Regressão Linear para descobrir qt o Preço dos Imóveis é afetado pelo m² no Rio de Janeiro

# Variável dependente - Preço dos imóveis
x = dados_filt['price_brl'].values

# Variáveis independente - Área dos imóveis em metros quadrados
y = dados_filt['area_m2'].values

# Dividir os dados de treino e teste
# Obs.: Qt menor o conjunto de dados maior o teste, por isso utilizaremos 30% e não 20%
x_train, x_test, y_train, y_test = \
train_test_split(
    x,
    y,
    test_size=0.4,
    shuffle=False
)

# Modelo linear
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(x_train.reshape(-1,1), y_train)

# Verificar a qualidade do treino: 0 a 1
# dados de teste
score = modelo.score(x_test.reshape(-1,1), y_test)
print('Coeficiente angular = ', modelo.coef_)
print('Coeficiente linear (intercepto): ', modelo.intercept_)
print('Score: ', score)

# Testando a análise preditiva
y_predicao = modelo.predict(x_test.reshape(-1,1))

# Simulando diferentes tamanhos de imóvel
areas_pred = np.array([50, 600, 1000, 800]).reshape(-1, 1)

# Previsões dos preços dos imóveis simulados
preco_pred = modelo.predict(areas_pred)
print(preco_pred)

#regressao linear
plt.subplot(1,2,1)
# sns.regplot(x=X_ameaca_test,y=y_lesao_test, color='red') # linha automática criada pelo seaborn
sns.regplot(x='price_brl', y='area_m2', data=dados_filt, color='black') # linha criada pelo cálculo do modelo de regressão criado 
plt.xlabel('Preço dos imóveis')
plt.ylabel('M² dos imóveis')
plt.title(f'Correlação entre preço e metro quadrado no Rio de Janeiro \n\
          Score: {score:.2f}\n\
          Correlação: {corr_preco_m2:.2f}')
#plt.show()


# tabela com os dados simulados 'preco_pred'
# vamos primeiramente juntar os dados simulados com os dados do conjunto de dados
# inserir dados da predição num dataframe (numa biblioteca) para utilizar na tabela do painel de visualização

df_preco_pred = pd.DataFrame({
    'M² do imóvel': areas_pred.flatten(),  # Achatando o array para torná-lo unidimensional
    'Preço do imóvel': preco_pred.flatten()  # Achatando o array para torná-lo unidimensional
})

#Erro médio quadrático 
from sklearn.metrics import mean_squared_error # serve para mostrar o valor do erro qd cria a linha de regressão
rmse = np.sqrt(mean_squared_error(y_test, y_predicao))

# Tabela
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
