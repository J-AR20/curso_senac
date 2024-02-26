from pyspark.sql import SparkSession

# sessão spark
spark = SparkSession.builder \
        .master('local[*]') \
        .appName('BigData') \
        .config('spark.driver.memory', '2g') \
        .config('spark.executor.memory', '2g') \
        .getOrCreate()

# endereço do parquet
endereco = r'C:\uc2_bigdata\dados'

#carregar o arquivo
df = spark.read.parquet(endereco + r'\202311_NovoBolsaFamilia.parquet')

#converter em pandas
df_valor_parcela_pd = df.select('REGIAO','VALOR PARCELA').toPandas()

#TIMMING (Ponto de Corte)
q_menor = df_valor_parcela_pd['VALOR PARCELA'].quantile(0.05)
q_maior = df_valor_parcela_pd['VALOR PARCELA'].quantile(0.95)

#corte
df_valor_parcela_pd_trimmed = df_valor_parcela_pd[ \
                            (df_valor_parcela_pd['VALOR PARCELA'] > q_menor) \
                            & (df_valor_parcela_pd['VALOR PARCELA'] < q_maior)]

#Visualizar gráficos
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#criação dos subplots
fig = make_subplots(
                    rows=1,
                    cols=2,
                    subplot_titles=['Boxplot', 'Tabela'],
                    specs=[[{'type':'box'},{'type':'table'}]]
)

#adicionar um boxplot
fig.add_trace(
    go.Box(
        y = df_valor_parcela_pd_trimmed['VALOR PARCELA'],
        x = df_valor_parcela_pd_trimmed['REGIAO'],
        name = 'Valor Parcela'
    ),
    row=1,col=1
)

#CRIAR UM FUNÇÃO DE FORMATAÇÃO
def formatacao(valor):
    return f'{valor:,.2f}'.replace('.','#').replace(',','.') \
    .replace('#',',')        

#DESENVOLVER AS MÉTRICAS ESTATÍSTICAS
df_total_regiao = df_valor_parcela_pd_trimmed.groupby('REGIAO')['VALOR PARCELA'].agg(
                        Total = 'sum',
                        Media = 'mean',
                        Variancia = 'var',
                        Desvio = 'std'
                    ).reset_index()

#calcular o total
total_geral = df_valor_parcela_pd_trimmed['VALOR PARCELA'].sum()

#calcular a participação
participacao = df_total_regiao['Total'] / total_geral

#formatar valores
df_total_regiao['Total'] = df_total_regiao['Total'].apply(formatacao)
df_total_regiao['Participacao'] = participacao.apply(formatacao)
df_total_regiao['Media'] = df_total_regiao['Media'].apply(formatacao)
df_total_regiao['Variancia'] = df_total_regiao['Variancia'].apply(formatacao)
df_total_regiao['Desvio'] = df_total_regiao['Desvio'].apply(formatacao)

#Tabela
#header das colunas (CABEÇALHO)
header_colunas = list(df_total_regiao.columns)

#células de dados
lst_celulas = []
for col in df_total_regiao.columns:
    lst_celulas.append(df_total_regiao[col])

#forma2: células de dados
#celulas = [df_total_regiao[col] for col in df_total_regiao.columns]

#Tabela
fig.add_trace (
    go.Table(
        header=dict(
            values=header_colunas,
            fill_color = 'lightblue'
        ),
        cells=dict(
            values=lst_celulas,
            fill_color = 'lightgrey'
        )
    ),
    row=1, col=2
)

#ajustar a tela
fig.update_layout(
    title = 'Análise do Bolsa Família por Região',
    autosize = True
)

#exibir o gráfico
fig.show()
#fig.write_html()

#fechar a sessão do spark
spark.stop()
