'''Exercício 02: Previsão de lesões corporais
Você foi convidado/a a auxiliar no planejamento da segurança pública do Estado 
do Rio de Janeiro e foi solicitado a apresentar um painel, no qual fosse possível 
observar a relação entre ameaças e lesões corporais dolosas, além de ser 
possível realizar uma previsão acerca do impacto em lesões corporais, a partir 
de simulações em quantidade de ameaças.
Requisitos da análise:
• Utilizar os dados de: 
https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
• Excluir 2024 da análise
• Faça as previsões da forma que você entender ser melhor.'''

# 1) Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
#importar a classe de treino e teste
from sklearn.model_selection import train_test_split
#importar a classe de regressão linear
from sklearn.linear_model import LinearRegression
#importar bibliotecas para visualização
import matplotlib.pyplot as plt
import seaborn as sns


# 2) Importando a base
df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                 , sep=';', encoding='ISO-8859-1')



# 3) Formatando a base: selecionar as colunas de interesse
df_filtrado = df[['ano','ameaca','lesao_corp_dolosa']]

# Excluir 2024
df_ano = df_filtrado[df_filtrado['ano']<= 2023]
print(df_ano.head())



# 4) Observar a relação entre ameaças e lesões corporais dolosas
# Cálculo de correlação 
corr_ameaca_lesao = df_ano['ameaca'].corr(df_ano['lesao_corp_dolosa'])
print(corr_ameaca_lesao)


# 5) Previsão do impacto em lesões corporais, a partir de simulações em quantidade de ameaças

#variável independente
x_ameaca = df_ano['ameaca'].values
print(x_ameaca)
print(x_ameaca.max()) # max 370
print(x_ameaca.min()) # min 0

#variável dependente
y_lesao = df_ano['lesao_corp_dolosa'].values
print(y_lesao.max()) # max 370
print(y_lesao.min()) # min 0

# Dividir os dados de treino e teste
# Importante sempre seguir a mesma ordem na hora de enunciar as variáveis:
# X SEMPRE deve vir antes do Y
X_ameaca_train, X_ameaca_test, y_lesao_train, y_lesao_test = \
train_test_split(
    x_ameaca,
    y_lesao,
    test_size=0.2
    #shuffle=False
)

# Modelo linear
modelo = LinearRegression() # criamos uma variável que vai representar o modelo de regressão linear (meio que vazio)
modelo.fit(X_ameaca_train.reshape(-1,1), y_lesao_train) # agora nós preenchemos o nosso modelo com as variáveis que iremos trabalhar

# verificador - checa a qualidade do treino
# quanto mais próximo de 1, é um treino aceitável
score = modelo.score(X_ameaca_test, y_lesao_test) # Treino é feito com  dados de treino, o score() - a aferição, é feita com dados de teste

# Previsões para diferentes quantidades de ameaças
mais_ameacas = np.array([400, 500, 600]).reshape(-1, 1)
y_lesao_preditiva = modelo.predict(mais_ameacas).round().astype(int)
print(y_lesao_preditiva)

# Previsões para algumas amostras dos dados reais
amostras_reais = df_ano.sample(n=3)
ameacas_reais = amostras_reais['ameaca'].values
lesoes_reais = amostras_reais['lesao_corp_dolosa'].values




# 6) Visualizando correlação e tabela com resultados do modelo
plt.figure(figsize=(10, 12))

# Gráfico 1 - Ameaça vs Lesão Corporal Dolosa
plt.subplot(2, 1, 1)
sns.regplot(x='ameaca', y='lesao_corp_dolosa', data=df_filtrado, color='orange')
plt.title('Correlação entre ameaça e lesão corporal dolosa')
plt.xlabel('Qt. ameaça')
plt.ylabel('Qt. lesão corporal dolosa')
plt.figtext(0.5, 0.55, 'A correlação {:.4f} entre ameaça e lesão corporal dolosa indica uma relação positiva muito forte.'.format(corr_ameaca_lesao), ha='center')
plt.figtext(0.95, 0.01, 'Fonte: Instituto de Segurança Pública do estado do Rio de Janeiro', horizontalalignment='right')

# Tabela com resultados do modelo
plt.subplot(2, 1, 2)
headers = ["Qt. Ameaças", "Predição Lesões Corporais"]
table_data = np.column_stack((mais_ameacas.flatten(), y_lesao_preditiva))
table_data_real = np.column_stack((ameacas_reais, lesoes_reais))
table_data_combined = np.vstack((table_data_real, table_data))
cell_colors = [['lightgrey', 'lightgrey'], ['lightgrey', 'lightgrey'], ['lightgrey', 'lightgrey'], ['red', 'lightgrey'], ['red', 'lightgrey'], ['red', 'lightgrey']]
table = plt.table(cellText=table_data_combined, colLabels=headers, loc='center', cellLoc='center', cellColours=cell_colors)

# Adicionando título à tabela
table_title = plt.title("Modelo de predição de lesões corporais dolosas baseado no número de ameaças", y=1.1)

# Adicionando legenda para dados preditivos
plt.figtext(0.5, 0.47, "Dados com fundo vermelho são testes preditivos", fontsize=10, ha='center')

# Ajustando a posição da legenda da fonte
plt.figtext(0.5, 0.01, 'Fonte: Instituto de Segurança Pública do estado do Rio de Janeiro', horizontalalignment='center')

plt.show()