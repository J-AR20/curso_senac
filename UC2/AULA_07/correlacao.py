import pandas as pd

endereco = r'D:\BIG DATA - SENAC\UC2\AULA_05'

df_veiculos = pd.read_excel(endereco + r'\veiculos.xlsx')

print(df_veiculos)

df_ano = df_veiculos[['Ano', 'Roubo veículos', "Furto veículos", 'Recuperação veículos']].groupby('Ano').sum()

print(df_ano)

#Calculo da correlação
corr_roubo_recup = df_ano['Roubo veículos'].corr(df_ano['Recuperação veículos'])

#exibir a correlação
print('A correlação é', corr_roubo_recup)
# Correlação Forte, resultado deu 0.93 (quase 1), quanto mais o roubo aumenta, aumenta a recuperação

# seaborn (biblioteca usada para visualização de dados estatísticos)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

sns.regplot(x='Roubo veículos', y='Recuperação veículos', data=df_ano)

# Boxplot serve para analisar distribuição
# Se os dados estiverem consolidados (agrupados, sumarizados) não será possível 
# analisar a distribuição
# Nesse caso, eu não posso utilizar a df_ano, por isso utilizaremos o df_veiculos

sns.boxplot(x='Ano', y='Roubo veículos', data=df_veiculos)

plt.show()



