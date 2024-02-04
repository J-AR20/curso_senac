'''Produzir:
1) Correlação entre Roubo e Furto;
2) Ver a distribuição dos crimes;
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.subplots as ps

#endereço do arquivo de dados
endereco_arquivo = r'E:\BIG DATA - SENAC\UC2\AULA_06'

#leitura do arquivo
df_veiculos = pd.read_excel(endereco_arquivo + r'\veiculos.xlsx')

print(df_veiculos)

# correlação entre idade e sakário
corr_roubo_furto = df_veiculos['Roubo veículos'].corr(df_veiculos['Furto veículos'])

# exibir a correlação
print('Correlação entre roubo e furto: ', corr_roubo_furto)

'''Existe uma forte correlação entre os crimes roubo e furto. O resultado de teste de regressão linear
a pontou a existência de uma forte correlação positiva entre as duas modalidades criminais, apontando que
ao passo que uma delas aumenta a outra também aumenta'''

# visualizar o gráfico de correlação
plt.figure(figsize=(12,6))

sns.regplot(x='Roubo veículos', y='Furto veículos', data=df_veiculos)

plt.show()




#gráfico de barras
#definição do local do gráfico
plt.subplot(2, 2, 1) # uma linha, duas colunas e gráfico na posicao 1 (primeiro quadrante)
df_veiculos['Roubo veículos'].plot.bar(title='Roubo de veículos por ano')
plt.xlabel('Ano')
plt.ylabel('Total roubos')

#definição do local do gráfico
plt.subplot(2, 2, 2) # uma linha, duas colunas e gráfico na posicao 1 (primeiro quadrante)
df_veiculos['Furto veículos'].plot.bar(title='Furto de veículos por ano')
plt.xlabel('Ano')
plt.ylabel('Total furtos')

#gráfico boxplot
#definição do local do gráfico
plt.subplot(2, 2, 3) # uma linha, duas colunas e gráfico na posicao 2 (segundo quadrante)
df_veiculos.boxplot(column=['Roubo veículos'])

#gráfico boxplot
#definição do local do gráfico
plt.subplot(2, 2, 4) # uma linha, duas colunas e gráfico na posicao 2 (segundo quadrante)
df_veiculos.boxplot(column=['Furto veículos'])
plt.show()






'''
PLOTLY
'''
fig = ps.make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(f'Correlação roubo e furto: {corr_roubo_furto}',
                    'Distribuição entre roubo e furto')
)

# dispersão
fig.add_trace(
    go.Scatter(
        x=df_veiculos['Roubo veículos'],
        y=df_veiculos['Furto veículos'],
        mode='markers'
    ),
    row=1,col=1
)

# boxplot
fig.add_trace(
    go.Box(
        x=df_veiculos['Roubo veículos'],
        y=df_veiculos['Furto veículos']
    ),
    row=1,col=2
)

fig.update_layout(
    title = 'Análise de dados: roubo e furto',
    autosize=True
)

fig.show()