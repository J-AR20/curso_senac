
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

#df_loja

#Qual o menor valor que foi vendido, durante o dia de trabalho, por loja?
df_loja['Menor'] = df_loja.iloc[:,1:9].min(axis=1)

#df_loja


#COLUNAS

#TOTAL 
#LOC - É um método para ser utilizado com o Rótulo 
#também é possível utilizar [linha,coluna]
df_loja.loc['Total'] = df_loja.sum(axis=0,numeric_only=True)

#df_loja

#MÉDIA
#CÁLCULO ERRADO
#df_loja.loc['Média_ERRADA'] = df_loja.mean(axis=0,numeric_only=True)

#CÁLCULO CERTO.
df_loja.loc['Média'] = df_loja.iloc[0:5,1:10].mean(axis=0)

#df_loja

#MAIOR
#CÁLCULO.
df_loja.loc['Maior'] = df_loja.iloc[0:5,1:].max(axis=0)

df_loja

#MENOR
#CÁLCULO.
df_loja.loc['Menor'] = df_loja.iloc[0:5,1:].min(axis=0)

#df_loja

#AMPLITUDE TOTAL
#Medida de dispersão ou variabilidade
#Afere a variabilidade do seu conjunto, qdo
#comparado com a média
df_loja.loc['Amplitude total'] = df_loja.loc['Maior'] - df_loja.loc['Menor']



#AMPLITUDE 2
df_loja.loc['Amplitude 2'] = df_loja.loc['Maior','Hora 1':'Total'] - df_loja.loc['Menor','Hora 1':'Total']

#SUBSTITUIR NaN por ''
df_loja = df_loja.fillna('--')
df_loja