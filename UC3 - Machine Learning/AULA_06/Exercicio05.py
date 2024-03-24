import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, sum as spark_sum

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("Análise do Bolsa Família") \
    .getOrCreate()

# Endereço dos dados
endereco = r'C:\Users\36131872023.1\Documents'

# Carregar o arquivo no DataFrame do Spark
dados = spark.read.csv(endereco + r'\202311_NovoBolsaFamilia.csv', sep=';', encoding='ISO-8859-1', header=True)


# Manter somente as colunas UF, NOME MUNICÍPIO e VALOR PARCELA
dados = dados.select('UF', 'NOME MUNICÍPIO', 'VALOR PARCELA')

# Substituir , por . e converter VALOR PARCELA para double
dados = dados.withColumn('VALOR PARCELA', regexp_replace(col('VALOR PARCELA'), ',', '.').cast('double'))


# Importar PLN
import spacy


#carregar o modelo de idioma
nlp=spacy.load('pt_core_news_lg')

#solicitar município para o usuário
texto_usuario = input('Solicite a sua análise por Município: ')

#processar  texto do usuário com o modelo PLN
doc=nlp(texto_usuario)

#identificar as entidades
munics_solicitados = []
for entidade in doc.ents:
    if entidade.label_ in ('LOC', 'GPE'):
        munics_solicitados.append(entidade.text.upper())

dados['NOME MUNICÍPIO'] = dados['NOME MUNICÍPIO'].str.upper()

if munics_solicitados:
    dados = dados[dados['NOME MUNICÍPIO'].isin(munics_solicitados)]
else:
    print('Desculpe. Não identifiquei nenhum município. Refaça sua solicitação')
    exit()

