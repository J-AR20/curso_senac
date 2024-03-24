import pandas as pd

# carga de dados
df_injuria = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/Base_Injuria_Preconceito.csv', sep=';', encoding='ISO-8859-1')
print(df_injuria.head())

# base onde estão as delegacias
df_dp = pd.read_csv(r'D:\BIG DATA - SENAC\UC2\AULA_014\DP.csv', sep=',', encoding='utf-8')
print(df_dp.head())

# renomeando a coluna 'Cisp' na base df_injuria para 'codDP' que é a coluna correspondente da base DP
df_injuria.rename(columns={'Cisp': 'codDP'}, inplace=True)
print(df_injuria.head())

# unindo as duas bases
df_injurias_por_dp = pd.merge(df_injuria, df_dp, on='codDP', how='inner')
print(df_injurias_por_dp.head())

# separando apenas a coluna que desejamos trabalhar
df_vitimas_por_dp = df_injurias_por_dp[['Vítimas','nome']]
print(df_vitimas_por_dp.head())

# sumarizando a base para chegar nos dados desejados:
df_top_10_dp = df_vitimas_por_dp.groupby('nome').sum('Vítimas') \
                    .sort_values('Vítimas', ascending=False)

print(df_top_10_dp.head(10))



