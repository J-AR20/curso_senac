# Uma das principais estruturas de dados - Dataframe
# Bidimensional / Tabular / Linhas x Colunas / Matriz
# Eixo das linhas axis=1
# Eixo das colunas axis=0

import pandas as pd

notas = [
    ['João',7.5,8.0,8.5,9.0],
    ['Maria',6.0,6.5,8.5,8.0],
    ['João',8.0,6.0,8.5,9]
]

df_notas = pd.DataFrame(notas)
# renomeando as colunas
df_notas.columns = ['Nome', 'nota1', 'nota2', 'nota3', 'nota4']

# criando colunas
df_notas['Media'] = df_notas[['nota1', 'nota2', 'nota3', 'nota4']].mean(axis=1)
df_notas['Maior'] = df_notas[['nota1', 'nota2', 'nota3', 'nota4']].max(axis=1)
df_notas['Menor'] = df_notas[['nota1', 'nota2', 'nota3', 'nota4']].min(axis=1)

print(df_notas.describe())

print(df_notas)