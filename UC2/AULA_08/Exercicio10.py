import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.subplots as ps

#endereço do arquivo de dados
endereco_arquivo = r'C:\uc2_bigdata\Dados'

#leitura do arquivo
df_funcionario = pd.read_excel(endereco_arquivo + r'\funcionarios.xlsx')

#print(df_funcionario)

# correlação entre idade e sakário
corr_idade_salario = df_funcionario['Idade'].corr(df_funcionario['Salário'])

# exibir a correlação
print('Correlação entre idade e salário: ', corr_idade_salario)

# visualizar o gráfico de correlação
plt.figure(figsize=(12,6))

sns.regplot(x='Salário', y='Idade', data=df_funcionario)

#plt.show()

'''
PLOTLY
'''
fig = ps.make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(f'Correlação idade e salário: {corr_idade_salario}',
                    'Distribuição entre idade e salário')
)

# dispersão
fig.add_trace(
    go.Scatter(
        x=df_funcionario['Idade'],
        y=df_funcionario['Salário'],
        mode='markers'
    ),
    row=1,col=1
)

# boxplot
fig.add_trace(
    go.Box(
        x=df_funcionario['Idade'],
        y=df_funcionario['Salário']
    ),
    row=1,col=2
)

fig.update_layout(
    title = 'Análise de dados: idade e salário',
    autosize=True
)

fig.show()



