from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, format_number
import pandas as pd
import spacy

#carga do modelo do idioma
nlp = spacy.load('pt_core_news_lg')

#Endereço dos dados
endereco = r'C:\Users\36131872023.1\Documents'

#Carregar o arquivo
df_bolsa_familia = pd.read_csv(endereco + r'\202311_NovoBolsaFamilia.csv', \
                               sep=';',encoding='ISO-8859-1')

#Manter somente as colunas UF, NOME MUNICÍPIO e VALOR PARCELA
df_bolsa_familia = df_bolsa_familia[['UF','NOME MUNICÍPIO','VALOR PARCELA']]

#substituir , por .
df_bolsa_familia['VALOR PARCELA'] = df_bolsa_familia['VALOR PARCELA'] \
                                    .str.replace(',','.').astype(float)

#converter para parquet
df_bolsa_familia.to_parquet(endereco + r'\202311_NovoBolsaFamilia.parquet')

'''
PLN
https://spacy.io/
'''

#interação humano-computador (IHC)
texto_usuario = input('Solicite sua análise: ')

#criar uma variável do nlp atribuindo o texto_usuário
doc = nlp(texto_usuario)

# entidades
lst_municipios = []
for entidade in doc.ents:
    if entidade.label_ == 'LOC':
        # dados da entidade para maiúsculo
        lst_municipios.append(entidade.text.upper())

# alterar os dados de município para maiúsculo
df_bolsa_familia['NOME MUNICÍPIO'] = df_bolsa_familia['NOME MUNICÍPIO'].str.upper()

# filtrar municípios
if lst_municipios:
    df_bolsa_familia_munic = df_bolsa_familia[df_bolsa_familia['NOME MUNICÍPIO'].isin(lst_municipios)]
else:
    print('Nenhum município foi solicitado. \
          Refaça sua solicitação, dando mais contexto a análise. \
          Exemplo: Analisar dados para os municípios do Rio de Janeiro \
          e Cabo Frio')
    exit()

# print(df_bolsa_familia_munic['NOME MUNICÍPIO'].unique())

#realizar o somatório do valor parcela, agrupando pela UF
    
df_bolsa_familia = df_bolsa_familia.withColumn('VALOR PARCELA', \
                                    regexp_replace(col('VALOR PARCELA'), \
                                                   ',','.').cast('double'))

lista_munic = df_bolsa_familia_munic['NOME MUNICÍPIO'].unique() \
                            .sum('VALOR PARCELA') \
                            .orderBy('sum(VALOR PARCELA)', ascending=False)

print(lista_munic)