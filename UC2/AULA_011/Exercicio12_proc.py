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
                    cols=1,
                    subplot_titles=['Boxplot']
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

#ajustar a tela
fig.update_layout(
    title = 'Análise do Bolsa Família por Região',
    autosize = True
)

#exibir o gráfico
fig.show()
fig.write_html()

#fechar a sessão do spark
spark.stop()
