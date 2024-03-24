import pandas as pd

df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                 , sep=';', encoding='ISO-8859-1')

#selecionar as colunas de interesse
df_filtrado = df[['ano','ameaca','lesao_corp_dolosa', \
             'roubo_em_coletivo', 'roubo_celular']]

#excluir 2024
df_ano = df_filtrado[df_filtrado['ano']<= 2023]
#df_ano = df_filtrado[df_filtrado['ano']< 2024]

#cálculo da correlação 1
corr_ameaca_lesao = df_ano['ameaca'].corr(df_ano['lesao_corp_dolosa'])

#cálculo da correlação 2
corr_roubo_coletivo_celular = df_ano['roubo_em_coletivo'] \
                        .corr(df_ano['roubo_celular'])

'''print(corr_ameaca_lesao)
print(corr_roubo_coletivo_celular)'''

##############
#Visualizando#
##############
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(
        f'Ameaça x Lesão corporal dolosa: {corr_ameaca_lesao:.2f}',
        f'Roubo em coletivo x Roubo de celular: \
            {corr_roubo_coletivo_celular:.2f}',
    )
)

# Gráfico 1: Ameaça e Lesão Corporal Dolosa
fig.add_trace(
    go.Scatter(
        x=df_ano['ameaca'],
        y=df_ano['lesao_corp_dolosa'],
        mode='markers'
    ), row = 1, col =1
)

# Gráfico 2: roubo em coletivo e roubo de celular
fig.add_trace(
    go.Scatter(
        x=df_ano['roubo_em_coletivo'],
        y=df_ano['roubo_celular'],
        mode='markers'
    ), row = 1, col =2
)

#atualizar o layout
fig.update_layout(
    title_text = 'Correlações',
    autosize = True
)

#exibir painel
fig.show()