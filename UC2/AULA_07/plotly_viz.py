import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as ps

#endereço do arquivo de dados
endereco_arquivo = r'D:\BIG DATA - SENAC\UC2\AULA_06'

#leitura do arquivo
df_funcionario = pd.read_excel(endereco_arquivo + r'\funcionarios.xlsx')

#print(df_funcionario)

#calcular a variância
var_salario = df_funcionario['Salário'].var()

#calcular o desvio padrão
devp_salario = df_funcionario['Salário'].std()

#calcular a média 
media_salario = df_funcionario['Salário'].mean()

#Exibir as medidas
print('Variância: ', var_salario)
print('Desvio padrão: ', devp_salario)
print('Média: ', media_salario)

'''
Visualizando em um painel dinâmico - PLOTLY
'''


fig = ps.make_subplots(rows=1, 
                       cols=2,
                       subplot_titles=('Salário por funcionário','Distribuição de salário'))

#Adicionar o gráfico de barras
fig.add_trace(
    go.Bar(
        y=df_funcionario['Funcionário'],
        x=df_funcionario['Salário'],
        orientation='h'
    ),
    row=1, col=1
)

#Rótulo dos eixos
fig.update_xaxes(title_text='Salário', row=1, col=1)
fig.update_yaxes(title_text='Funcionário', row=1, col=1)

#adicionar o boxplot
fig.add_trace(
    go.Box(
        y=df_funcionario['Salário'],
        name='Salário'
    ),
    row=1, col=2
)

# Atualizar o layout
fig.update_layout(
    title_text = 'Análise de dados de salário',
    autosize = True
)

#Exibir a figura
fig.show()


