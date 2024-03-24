from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, sum as spark_sum
import spacy

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("Análise do Bolsa Família") \
    .getOrCreate()

# Carregar o modelo do idioma
nlp = spacy.load('pt_core_news_lg')

# Endereço dos dados
endereco = r'C:\Users\36131872023.1\Documents'

# Carregar o arquivo no DataFrame do Spark
df_bolsa_familia = spark.read.csv(endereco + r'\202311_NovoBolsaFamilia.csv', sep=';', encoding='ISO-8859-1', header=True)

# Manter somente as colunas UF, NOME MUNICÍPIO e VALOR PARCELA
df_bolsa_familia = df_bolsa_familia.select('UF', 'NOME MUNICÍPIO', 'VALOR PARCELA')

# Substituir , por . e converter VALOR PARCELA para double
df_bolsa_familia = df_bolsa_familia.withColumn('VALOR PARCELA', regexp_replace(col('VALOR PARCELA'), ',', '.').cast('double'))

# Interagir com o usuário
texto_usuario = input('Solicite sua análise: ')

# Criar uma variável do nlp atribuindo o texto_usuário
doc = nlp(texto_usuario)

# Extrair municípios
lst_municipios = [entidade.text.upper() for entidade in doc.ents if entidade.label_ == 'LOC']

# Filtrar DataFrame para os municípios específicos
df_bolsa_familia_munic = df_bolsa_familia.filter(col('NOME MUNICÍPIO').isin(lst_municipios))

if df_bolsa_familia_munic.count() == 0:
    print('Nenhum município foi solicitado. Refaça sua solicitação, dando mais contexto à análise. \
          Exemplo: Analisar dados para os municípios do Rio de Janeiro e Cabo Frio')
    spark.stop()
    exit()

# Realizar a soma do valor parcela, agrupando pela UF
df_bolsa_familia_munic.groupBy('NOME MUNICÍPIO').agg(spark_sum('VALOR PARCELA').alias('TOTAL')).show()

# Parar SparkSession
spark.stop()
