'''Exercício 10: Identificando correlações 

A gerente de RH da sua empresa precisa de um auxílio para realizar um estudo 
acerca das relações entre idade e salário, buscando identificar: 

1. Existe alguma relação entre a idade e o salário? Será que os mais novos 
ganham menos que os mais velhos? 
2. Como é a distribuição dos salários segundo a idade? 

Ela  também  informou  que  gostaria  de  visualizar  um  “painel  simples”,  com 
visualizações que pudessem auxiliar na tomada de decisão. 

Os dados estão na planilha ‘funcionarios.xlsx’'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.subplots as ps

#endereço do arquivo de dados
endereco_arquivo = r'D:\BIG DATA - SENAC\UC2\AULA_06'

#leitura do arquivo
df_funcionario = pd.read_excel(endereco_arquivo + r'\funcionarios.xlsx')

#print(df_funcionario)


#correlação entre idade e salário
corr_idade_salario = df_funcionario['Idade'].corr(df_funcionario['Salário'])

#exibir o resultado da correlação
print(corr_idade_salario)
# valor = -0.1943
# o resultado negativo indica uma correlação inversamente proporcional, ou seja, enquanto um aumenta
# o outro diminui. no entanto, como o valor está bem próximo do zero indica que essa tendência de correlação
# é fraca. neste sentido, só com esses valores ainda não podemos afirmar muita coisa

# Vamos visualizar graficamente o teste realizado
plt.figure(figsize=(12,6))

# construção de um gráfico de regressão linear que indica a correlação
sns.regplot(x='Idade',y='Salário',data=df_funcionario)

plt.show()

'''
PLOTLY
'''

fig = ps.make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(f'Correlação idade-salário: {corr_idade_salario}',
                    'Distribuição entre idade e salário')

)

# dispersão
fig.add_trace(
    go.Scatter(
        x=df_funcionario['Idade'],
        y=df_funcionario['Salário'],
        mode='markers' # mostra os pontos que representam os dados - além da linha de dispersão
    ),
    row=1,col=1
)

#boxplot
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