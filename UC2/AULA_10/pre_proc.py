import pandas as pd

#Endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

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
