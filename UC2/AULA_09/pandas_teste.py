import pandas as pd
import time

#iniciar a contagem do tempo de execução
start_time = time.time()

#Endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

#Carregar o arquivo
df_bolsa_familia = pd.read_csv(endereco + r'\202111_BolsaFamilia_Pagamentos.csv', \
                               sep=';',encoding='ISO-8859-1')

#substituir ',' por '.'
df_bolsa_familia['VALOR PARCELA'] = df_bolsa_familia['VALOR PARCELA'] \
                                        .str.replace(',','.') \
                                        .astype(float)

#Realizar o somatório de 'VALOR PARCELA' por UF
df_bolsa_familia_uf = df_bolsa_familia.groupby('UF')['VALOR PARCELA'].sum()

#exibir rquivo - 20 linhas
#print(df_bolsa_familia.head(20))

#exibir df_bolsa_familia_uf
print(df_bolsa_familia_uf)

#exibir o tempo de execução
print(f'Tempo de execução: {round(time.time() - start_time,2)} segundos')