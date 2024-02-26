from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col
import time
import pandas as pd

#iniciar a contagem do tempo de execução
start_time = time.time()

#criar uma seção spark
spark = SparkSession.builder \
    .master('local[*]') \
    .appName('BigData') \
    .getOrCreate()    
    
#Endereço dos dados
endereco = r'D:\BIG DATA - SENAC\UC2\AULA_09'

df_bolsa_familia = spark.read.option('econding', 'ISO-8859-1') \
    .option('header', 'true') \
    .option('sep', ';') \
    .csv(endereco + r'\202101_BolsaFamilia_Pagamentos.csv')

#Carregar o arquivo com o pandas
endereco_arquivo = r'D:\BIG DATA - SENAC\UC2\AULA_09'
df_bolsa_familia = pd.read_csv(endereco_arquivo + r'\202101_BolsaFamilia_Pagamentos.csv', sep=';', encoding='ISO-8859-1')
print(df_bolsa_familia.head(20))

#exibir o dataframe pelo spark
#df_bolsa_familia.show()

#substituir virgula por ponto da coluna 'valor parcela'
df_bolsa_familia = df_bolsa_familia.withColumn('VALOR PARCELA', \
                    regexp_replace(col('VALOR PARCELA'), \
                        ',','.').cast('double'))

#realizar uma sumarização de VALOR PARCELA por UF
df_bolsa_familia_uf = df_bolsa_familia.groupby('UF').sum('VALOR PARCELA')

df_bolsa_familia_uf.show(n=27)  # ou quando não se sabe o N df_bolsa_familia_uf.show(n=df_bolsa_familia.count())

#exibir o tempo de execucao
print(f'tempo de execução: {round(time.time() - start_time, 2)}')

#parar a sessão
spark.stop()