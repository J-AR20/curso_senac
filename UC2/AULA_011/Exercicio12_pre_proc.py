import pandas as pd
#Endereço dos dados
endereco = r'C:\uc2_bigdata\dados'

df = pd.read_csv(endereco + r'\202311_NovoBolsaFamilia.csv', \
                 sep=';', encoding = 'ISO-8859-1')

# dataframe regiao
df_regiao = pd.DataFrame({
    'UF': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'REGIAO': ['Norte', 'Nordeste', 'Norte', 'Norte', 'Nordeste', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Centro-Oeste', 'Nordeste', 'Centro-Oeste', 'Centro-Oeste', 'Sudeste', 'Norte', 'Nordeste', 'Sul', 'Nordeste', 'Nordeste', 'Sudeste', 'Nordeste', 'Sul', 'Norte', 'Norte', 'Sul', 'Sudeste', 'Nordeste', 'Norte']
})

#filtrando colunas df bolsa familia
df = df[['UF','VALOR PARCELA']]

#substituir , por .
df['VALOR PARCELA'] = df['VALOR PARCELA'] \
                        .str.replace(',','.').astype(float)

#relacionar os dfs (JOIN)
df_regiao_uf = df.merge(df_regiao, on='UF')

#exportar para parquet
df_regiao_uf.to_parquet(endereco + r'\202311_NovoBolsaFamilia.parquet')