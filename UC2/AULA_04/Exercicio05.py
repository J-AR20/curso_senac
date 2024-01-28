import pandas as pd
'''
•	'Centro',1000,2500,1700,1500,3000,2200,1300,1000
•	'Botafogo',1500,3200,2300,1000,2500,1700,1500,800
•	'Tijuca',1800,2500,2000,1100,2700,1800,1600,1200
•	'Ipanema',1500,3000,2100,900,2200,1500,1300,1000
•	'Copacabana',2000,2300,2000,1400,2100,1600,1500,1200 
'''
df_loja = pd.DataFrame (
    [
        ['Centro',1000,2500,1700,1500,3000,2200,1300,1000],
        ['Botafogo',1500,3200,2300,1000,2500,1700,1500,800],
        ['Tijuca',1800,2500,2000,1100,2700,1800,1600,1200],
        ['Ipanema',1500,3000,2100,900,2200,1500,1300,1000],
        ['Copacabana',2000,2300,2000,1400,2100,1600,1500,1200] 
    ]
)

#visualizando o df
#print(df_loja)

df_loja.columns = ['Loja', 'Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']

#visualizando nome de colunas
#df_loja

#Qual o total das vendas por loja?
df_loja['Total'] = df_loja.sum(axis=1, numeric_only=True)

#Visualizando o total
#print(df_loja)

#Qual a média das vendas por loja?

#CÁLCULO ERRADO!!!!!
#df_loja['Média_ERRADA'] = df_loja.mean(axis=1, numeric_only=True)

#CÁLCULO CORRETO!!!!!
df_loja['Média'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].mean(axis=1)

#Visualizando a média
#print(df_loja)

#Qual o maior valor que foi vendido, durante o dia de trabalho, por loja?
df_loja['Maior'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].max(axis=1)

#Visualizando o maior
#print(df_loja)

#Visualizando o maior valor com a utilização do método ILOC
#ILOC é um método de indexação baseado em posições [linhas, colunas]
df_loja['Maior_iLoc'] = df_loja.iloc[:,1:9].max(axis=1)

df_loja

#Qual o menor valor que foi vendido, durante o dia de trabalho, por loja?
df_loja['Menor'] = df_loja.iloc[:,1:9].min(axis=1)

#df_loja

#Filtro >= 14000
df_loja_filtrada = df_loja[df_loja['Total'] >= 14000]

df_loja_filtrada

#ordenação decrescente
print(df_loja_filtrada.sort_values(by='Total',ascending=False))

