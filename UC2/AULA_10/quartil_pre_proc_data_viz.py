from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col
import time

#iniciar a contagem do tempo de execução
start_time = time.time()

#Criar uma sessão spark
spark = SparkSession.builder \
        .master('local[*]') \
        .appName('BigData') \
        .config('spark.driver.memory','2g') \
        .config('spark.executor.memory', '2g') \
        .getOrCreate()

#Endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

#carregar o arquivo csv
df_bolsa_familia = spark.read.option('encoding', 'ISO-8859-1') \
                    .option('header', 'true') \
                    .option('sep', ';') \
                    .parquet(endereco + r'\202311_NovoBolsaFamilia.parquet')

#exibir o dataframe
#df_bolsa_familia.show()

#Calcular quartil
valores_quartis = df_bolsa_familia.stat.approxQuantile('VALOR PARCELA' \
                                    , [0.25, 0.5, 0.75], 0.01)

#exibir valores de quartil
print('Q1: ',valores_quartis[0])
print('Q2 (MEDIANA): ',valores_quartis[1])
print('Q3: ',valores_quartis[2])

#Visualizar o valor parcela no boxplot
#converter para pandas
df_bolsa_familia_valor_parcela_pd = df_bolsa_familia \
                                        .select('VALOR PARCELA').toPandas()

#seaborn
import seaborn as sns
sns.boxplot(data=df_bolsa_familia_valor_parcela_pd,y='VALOR PARCELA') 

import matplotlib.pyplot as plt
plt.show()

#encerrar sessão
spark.stop()

#exibir o tempo de execução
print(f'Tempo de execução: {round(time.time() - start_time,2)} segundos')
