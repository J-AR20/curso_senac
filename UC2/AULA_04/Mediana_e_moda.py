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
        ['Centro',1000,2500,1500,1500,3000,2200,1300,1000],
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

#média
df_loja['Média'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].mean(axis=1)

#Adicionando a coluna de mediana
df_loja['Mediana'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].median(axis=1)

#Adiconando a coluna de moda
#Modal (1 moda): Só funcionará se houver 1 moda

df_loja['Moda'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].mode(axis=1)

#Bimodal ou multimodal
df_loja['Moda'] = df_loja[['Hora 1', 'Hora 2', 'Hora 3',
                    'Hora 4', 'Hora 5', 'Hora 6', 'Hora 7',
                   'Hora 8']].mode(axis=1).fillna('').values.tolist()

#visualizando nome de colunas
df_loja