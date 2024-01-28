'''Exercício 05: Lanchonetes

A Gerente de uma rede de lanchonetes do Rio de Janeiro, entrou em contato com você, 
te pedindo para desenvolver um programa, onde ela pudesse obter respostas para as 
seguintes perguntas, com base nas vendas por hora, do seu dia de trabalho:

Qual o total das vendas por loja?
Qual a média das vendas por loja?
Qual o maior valor que foi vendido, durante o dia de trabalho, por loja?
Qual o menor valor que foi vendido, durante o dia de trabalho, por loja?
Ela te pediu também, para que no final, exibisse na tela as lojas ordenadas pelo total de vendas, 
de forma decrescente (do valor maior para o menor), para que pudesse observar o ranking das lojas 
pelo total de suas vendas, considerando somente aquelas que tiveram um total maior ou igual a 14.000.

Ela também de te passou os dados, para que você pudesse desenvolver esse trabalho:

Centro: 1000,2500,1700,1500,3000,2200,1300,1000
Botafogo: 1500,3200,2300,1000,2500,1700,1500,800
Tijuca: 1800,2500,2000,1100,2700,1800,1600,1200
Ipanema: 1500,3000,2100,900,2200,1500,1300,1000
Copacabana: 2000,2300,2000,1400,2100,1600,1500,1200'''

import pandas as pd

vendas = [
    ['Centro', 1000,2500,1700,1500,3000,2200,1300,1000],
    ['Botafogo',1500,3200,2300,1000,2500,1700,1500,800],
    ['Tijuca',1800,2500,2000,1100,2700,1800,1600,1200],
    ['Ipanema',1500,3000,2100,900,2200,1500,1300,1000],
    ['Copacabana',2000,2300,2000,1400,2100,1600,1500,1200]
]

df_vendas = pd.DataFrame(vendas)

# ------ Renomeando colunas ------
df_vendas.columns = ['Lojas', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8']

# ------ Criando colunas -------

# 1) Total Vendas
df_vendas['Total_v'] = df_vendas[['V1','V2','V3','V4','V5','V6','V7','V8']].sum(axis=1)
# Utilizamos [[]] dois colchetes e não 1 [] porque não estamos pegando todas as colunas
# mas um subconjunto dentro delas, uma vez que dentro de df_vendas não estamos pegando
# a coluna 'Lojas'.. No R é quase como estar "criando" um novo objeto.

# PS.: A soma da linha toda poderia ter sido feito assim:
# df_vendas['Total_v'] = df_vendas.sum(axis=1,numeric_only=True)

# 2) Total
df_vendas['Media'] = df_vendas[['V1','V2','V3','V4','V5','V6','V7','V8']].mean(axis=1)
# Nesse caso não rola de fazer o numeric_only=T pq ele ia utilizar o total para fazer a média

# 3) Maior valor vendido
df_vendas['Maior'] = df_vendas[['V1','V2','V3','V4','V5','V6','V7','V8']].max(axis=1)

# Vizualizando o maior valor COM A UTILIZACAO DO MÉTODO iLOC
# iLOC - MÉTODO DE INDEXAÇÃO BASEADO EM POSIÇÕES(LINHAS E COLUNAS)
df_vendas['Maior_iloc'] = df_vendas.iloc[:,1:9]

# 4) Maior valor vendido
df_vendas['Menor'] = df_vendas[['V1','V2','V3','V4','V5','V6','V7','V8']].min(axis=1)

# 5) Ordenar base pelo total de vendas
# df_vendas = df_vendas[['Total_v']].sort_values(axis=1)

df_maiores = []

filtro = df_vendas['Total_v'] >= 14000
df_maiores = df_vendas[filtro]

# Outra forma de ordenar sem precisar criar um objeto novo é:
print(df_vendas[df_vendas['Total_v']>=14000])


# Ordenando a base
df_ordenado = df_maiores.sort_values(by='Total_v', ascending=False)

print(df_ordenado)

df_ordenado

# print(df_vendas)

