import pandas as pd
import numpy as np

#obter os dados
dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                    , sep=';', encoding='ISO-8859-1')

#Filtrar ano
dados = dados[dados['ano'] <= 2023]

'''
PLN
https://spacy.io/
'''
#biblioteca
import spacy

#carga do modelo do idioma
nlp = spacy.load('pt_core_news_lg')

#interação humano-computador (IHC)
texto_usuario = input('Solicite sua análise: ')

#criar uma variável do nlp atribuindo o texto_usuário
doc = nlp(texto_usuario)

# entidades
lst_municipios = []
for entidade in doc.ents:
    if entidade.label_ == 'LOC':
        # dados da entidade para maiúsculo
        lst_municipios.append(entidade.text.upper())

# alterar os dados de município para maiúsculo
dados['munic'] = dados['munic'].str.upper()

# filtrar municípios
if lst_municipios:
    dados = dados[dados['munic'].isin(lst_municipios)]
else:
    print('Nenhum município foi solicitado. \
          Refaça sua solicitação, dando mais contexto a análise. \
          Exemplo: Analisar dados para os municípios do Rio de Janeiro \
          e Cabo Frio')
    exit()

print(dados['munic'].unique())
'''
FIM PLN
'''

#variável dependente
y_cvli = dados['cvli'].values

#variável independente
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
#dados de treino
#y = a1x1 + a2x2 + b
#cvli = a1*hom_doloso + a2*letalidade_violenta + b
modelo.fit(X_hom_letalidade_train.reshape(-1,2), y_cvli_train)

#Verificar a qualidade do treino: 0 a 1
#dados de teste
score = modelo.score(X_hom_letalidade_test.reshape(-1,2), y_cvli_test)
print('Coeficente angular: ', modelo.coef_)
print('Coeficiente linear (Intercepto): ', modelo.intercept_)
print('Score: ', score)

#Testar a análise preditiva
y_predicao = modelo.predict(X_hom_letalidade_test.reshape(-1,2))

#simular as quantidades de homicídio doloso e letalidade violenta
qtd_hom_letalidade_pred = np.array([
                                    [12,15],
                                    [23,25],
                                    [27,32]
                                    ])

#estimar o cvli
cvli_pred = modelo.predict(qtd_hom_letalidade_pred)

print('CVLI Pred: ', cvli_pred)

'''#Inserir dados de predição em um dataframe
#Para utilizá-los na tabela do painel do visualização
df_lesao_pred = pd.DataFrame({'Qtde. ameaças':qtd_ameaca_pred, \
                              'Lesão corp. dolosa':lesao_pred})'''

#RMSE
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_cvli_test, y_predicao))

#VISUALIÇÃO DE DADOS
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15,10), subplot_kw={'projection': '3d'})

hom_doloso = X_hom_letalidade_test[:,0]
letalidade_violenta = X_hom_letalidade_test[:,1]

ax.scatter(hom_doloso,letalidade_violenta,y_predicao,color='blue')
ax.plot_trisurf(hom_doloso,letalidade_violenta,y_predicao, color='red', alpha=0.5)

ax.set_xlabel('Hom. doloso')
ax.set_ylabel('Letalidade violenta')
ax.set_zlabel('CVLI Pred')
plt.title('CVLI Preditivo')
plt.tight_layout()
plt.show()