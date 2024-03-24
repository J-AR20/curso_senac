# Importando bibliotecas
import pandas as pd

df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')
print(df.head())

# Selecionar as colunas de interesse
df_filtrado = df[['ano', 'ameaca', 'lesao_corp_dolosa', 'roubo_celular', 'roubo_em_coletivo']]

# Excluindo 2024
df_ano = df_filtrado[df_filtrado['ano']<= 2023]
print(df_ano.head())

# Cálculo da correlação
corr_ameaca_lesao = df_ano['ameaca'].corr(df_ano['lesao_corp_dolosa'])

corr_roubo_coletino_celular = df_ano['roubo_em_coletivo'].corr(df_ano['roubo_celular'])

# Visualizar

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(
    f'Ameaça x Lesão Corporal Dolosa: {corr_ameaca_lesao:.2f}',
    f'Roubo em coletivo x Roubo de celular: {corr_roubo_coletino_celular:.2f}',
    )
)

# Gráfico 1: Ameaça e lesão corporal dolosa
fig.add_trace(
    go.Scatter(
        x=df_ano['ameaca'],
        y=df_ano['lesao_corp_dolosa'],
        mode='markers'
    ), row=1, col=1
)

# Gráfico 2: Roubo em coletivo e Roubo de celular
fig.add_trace(
    go.Scatter(
        x=df_ano['roubo_em_coletivo'],
        y=df_ano['roubo_celular'],
        mode='markers'
    ), row=1, col=2
)

# Atualizar o layout - layout do painel por completo
fig.update_layout(
    title_text='Correlações',
    autosize= True
)

# Exibir painel
fig.show()