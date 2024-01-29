import pandas as pd
import matplotlib.pyplot as plt

endereco = r'D:\BIG DATA - SENAC\UC2\AULA_05'
# r'' se chama 'raw string' que diz para o python o que são aquelas barras.. daí não precisamos corrigir na mão!!!!! 

df_veiculos = pd.read_excel(endereco + r'\veiculos.xlsx')
# df_veiculos2 = pd.read_excel(endereco + r'\veiculos_novo.xlsx')
# a razão para concatenar o endereço assim é que vc pode chamar varios arquivos de uma mesma pasta sem muito esforço

# delimitar o DF pelas colunas (por suas séries) responsáveis por responder o nosso problema
df_regiao = df_veiculos[['Regiao', 'Roubo veículos', 'Furto veículos', 'Recuperação veículos']]
# excluímos o Ano porque não nos interessava

# primeira coisa que precisamos fazer, já que nossa análise é por região, é agrupar os dados por região
# precisamos utilizar o groupby (para agrupar) e o sum() para somar os dados agrupados
df_regiao = df_veiculos[['Regiao', 'Roubo veículos', 'Furto veículos', 'Recuperação veículos']].groupby('Regiao').sum()

# criar uma coluna de roubo+furtos
df_regiao['Total R+F'] = df_regiao['Roubo veículos'] + df_regiao['Furto veículos']

# determinar taxa de recuperação -> taxa_recuperacao = recuperacao / roubo
df_regiao['Tx. recuperacao'] = df_regiao['Recuperação veículos'] / df_regiao['Roubo veículos']

# desenvolva um gráfico de barras.... (ver os parametros exigidos no enunciado do exercicio) 
# primeira coisa a ser feita é ordenar os dados

df_regiao.sort_values(by='Tx. recuperacao', ascending=False)

df_regiao['Tx. recuperacao'].plot.bar(title='Tx de recuperação por Região', figsize=(10,5))
plt.xlabel('Região')
plt.ylabel('Tx. de recuperação')

plt.show()


