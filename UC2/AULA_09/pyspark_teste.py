from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col
import time

#iniciar a contagem do tempo de execução
start_time = time.time()

#Criar uma sessão spark
spark = SparkSession.builder \
        .master('local[*]') \
        .appName('BigData') \
        .getOrCreate()

#Endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

#carregar o arquivo csv
df_bolsa_familia = spark.read.option('encoding', 'ISO-8859-1') \
                    .option('header', 'true') \
                    .option('sep', ';') \
                    .csv(endereco + r'\202111_BolsaFamilia_Pagamentos.csv')

#exibir o dataframe
#df_bolsa_familia.show()

#substituir ',' por '.', na coluna 'VALOR PARCELA'
df_bolsa_familia = df_bolsa_familia.withColumn('VALOR PARCELA', \
                                    regexp_replace(col('VALOR PARCELA'), \
                                                   ',','.').cast('double'))

#realizar umsomatório de valor parcela por UF
df_bolsa_familia_uf = df_bolsa_familia.groupby('UF') \
                            .sum('VALOR PARCELA')

#exibir o resultado de df_bolsa_familia_uf
df_bolsa_familia_uf.show(n=27)

#exibir o tempo de execução
print(f'Tempo de execução: {round(time.time() - start_time,2)} segundos')

#parar sessão
spark.stop()