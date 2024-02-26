from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, format_number

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
                    .csv(endereco + r'\202311_NovoBolsaFamilia.csv')

#exibir o dataframe
#df_bolsa_familia.show()

#substituir ',' por '.', na coluna 'VALOR PARCELA'
df_bolsa_familia = df_bolsa_familia.withColumn('VALOR PARCELA', \
                                    regexp_replace(col('VALOR PARCELA'), \
                                                   ',','.').cast('double'))

#realizar o somatório do valor parcela, agrupando pela UF
df_bolsa_familia_munic = df_bolsa_familia.groupby(['NOME MUNICÍPIO']) \
                            .sum('VALOR PARCELA') \
                            .orderBy('sum(VALOR PARCELA)', ascending=False)
#Formatar número decimal
df_bolsa_familia_munic = df_bolsa_familia_munic \
                            .withColumn('sum(VALOR PARCELA)' \
                            ,format_number(col('sum(VALOR PARCELA)'),2)) \
                            .withColumnRenamed('sum(VALOR PARCELA)','VALOR TOTAL')

#exibir o dataframe ranqueado por munic
#15 primeiras cidades
df_bolsa_familia_munic.show(n=15)

#encerrar sessão
spark.stop()
