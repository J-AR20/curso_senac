'''Exercício 11: Identificando correlações 

O  Ministro  de  desenvolvimento  Social  pediu  sua  ajudar  para  verificar  o 
ranqueamentos das 20 cidades que mais receberam o auxílio do Bolsa Família 
em dezembro de 2023. 

Informou a você que os dados podem ser obtidos através do link a seguir: 
https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia 
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

#Criar uma sessão spark
spark = SparkSession.builder \
        .master('local[*]') \
        .appName('BigData') \
        .getOrCreate()

#Endereço dos dados
endereco = r'C:\Users\36131872023.1\Downloads'

#carregar o arquivo csv
df_bolsa_familia = spark.read.option('encoding', 'ISO-8859-1') \
                    .option('header', 'true') \
                    .option('sep', ';') \
                    .csv(endereco + r'\202311_NovoBolsaFamilia.csv')

# df_bolsa_familia.show()

#substituir virgula por ponto da coluna 'valor parcela'
df = df_bolsa_familia.withColumn('VALOR PARCELA', \
                    regexp_replace(col('VALOR PARCELA'), \
                        ',','.').cast('double'))

# realizar o somatório do valor parcela, agrupando pelo nome do município
df_por_cidade = df.groupby('NOME MUNICÍPIO').sum('VALOR PARCELA')

df_por_cidade.orderBy(col("VALOR PARCELA").asc(),col("NOME MUNICÍPIO").desc())

df_por_cidade.show(n=20)

# NÃO CONSEGUI RESOLVER.... 
