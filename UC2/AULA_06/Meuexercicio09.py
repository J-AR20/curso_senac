# Exercício 09: Revisão salarial

# A gerente de RH da sua empresa precisa de um auxílio para realizar um estudo 
# acerca dos salários dos funcionários, buscando identificar a distribuição deles, 
# a fim de definir uma estratégia fundamentada em dados. 
# Sabendo de sua experiência, pediu sua ajuda para fornecer os insumos necessários, 
# para apoiar a sua tomada de decisão.

# Os dados estão na planilha ‘funcionarios.xlsx’, na coluna “Salário”.

import pandas as pd
import matplotlib.pyplot as plt
endereco = r'D:\BIG DATA - SENAC\UC2\AULA_06' # pen drive
# endereco = r'C:\Users\jonas.araujo\OneDrive - IFEC-RJ\Área de Trabalho\data-science\CURSO SENAC\UC2\AULA_06' # computador trabalho

df_funcionarios = pd.read_excel(endereco + r'\funcionarios.xlsx')

print(df_funcionarios)

#Recortando uma base apenas com salário para estudá-los separadamente
dados_salario = df_funcionarios[['Idade','Salário', 'Tempo de casa']]
print(dados_salario)

#Isso fornecerá informações como média, desvio padrão, mínimo, máximo, quartis, etc., 
# que ajudarão você a entender a dispersão dos salários na empresa.
estatisticas_salario = dados_salario['Salário'].describe()
print(estatisticas_salario)

# Criando um boxplot para a série 'Salário'
q1_salario = dados_salario['Salário'].quantile(0.25)
q3_salario = dados_salario['Salário'].quantile(0.75)
media_salario = dados_salario['Salário'].mean()
max_salario = dados_salario['Salário'].max()
plt.figure(figsize=(10, 6))
plt.text(1.1,q1_salario, 'Q1: ' + str(q1_salario), fontsize=10, color='blue')
plt.text(1.1,q3_salario, 'Q3: ' + str(q3_salario), fontsize=10, color='blue')
plt.text(1.23,max_salario, 'Média: ' + str(media_salario), fontsize=10)
plt.boxplot(dados_salario['Salário'])
plt.title('Boxplot do Salário')
plt.xlabel('Salário')
plt.show()


'''A variância sugere um conjunto de dados disperso.
A mediana, por exemplo, está relativamente longe do Q3 e muito distante do Q4
Há pouquíssimas pessoas que recebem acima de 10.000
'''


# Criando um boxplot para a série 'Tempo de casa'
q1_tcasa = dados_salario['Tempo de casa'].quantile(0.25)
q3_tcasa = dados_salario['Tempo de casa'].quantile(0.75)
media_tcasa = dados_salario['Tempo de casa'].mean()
max_tcasa = dados_salario['Tempo de casa'].max()
plt.figure(figsize=(10, 6))
plt.text(1.1,q1_tcasa, 'Q1: ' + str(q1_tcasa), fontsize=10, color='blue')
plt.text(1.1,q3_tcasa, 'Q3: ' + str(q3_tcasa), fontsize=10, color='blue')
plt.text(1.23,max_tcasa, 'Média: ' + str(media_tcasa), fontsize=10)
plt.boxplot(dados_salario['Tempo de casa'])
plt.title('Boxplot do Tempo de casa')
plt.xlabel('Tempo de casa (anos)')
plt.show()


# Criando um boxplot para a série 'Idade'
q1_idade = dados_salario['Idade'].quantile(0.25)
q3_idade = dados_salario['Idade'].quantile(0.75)
media_idades = dados_salario['Idade'].mean()
max_idade = dados_salario['Idade'].max()
plt.figure(figsize=(10, 6))
plt.text(1.1,q1_idade, 'Q1: ' + str(q1_idade), fontsize=10, color='blue')
plt.text(1.1,q3_idade, 'Q3: ' + str(q3_idade), fontsize=10, color='blue')
plt.text(1.23,max_idade, 'Média: ' + str(media_idades), fontsize=10)
plt.boxplot(dados_salario['Idade'])
plt.title('Boxplot da Idade')
plt.xlabel('Idade')
plt.show()
# Três idades estão são outliers / cabe retirá-las?
# Vamos retirar da amostra as idades outliers

# Calcule o intervalo interquartil (IQR)
IQR = q3_idade - q1_idade

# Defina os limites para identificar outliers
limite_inferior = q1_idade - 1.5 * IQR
limite_superior = q3_idade + 1.5 * IQR

# Filtrar o DataFrame para remover outliers de idade
df_sal_sem_outliers = dados_salario[(dados_salario['Idade'] >= limite_inferior) & (dados_salario['Idade'] <= limite_superior)]
print(df_sal_sem_outliers)

# Vamos agora refazer o boxplot da idade para ver se os outliers foram retirados:
q1_idade = df_sal_sem_outliers['Idade'].quantile(0.25)
q3_idade = df_sal_sem_outliers['Idade'].quantile(0.75)
media_idades = df_sal_sem_outliers['Idade'].mean()
max_idade = df_sal_sem_outliers['Idade'].max()
plt.figure(figsize=(10, 6))
plt.text(1.1,q1_idade, 'Q1: ' + str(q1_idade), fontsize=10, color='blue')
plt.text(1.1,q3_idade, 'Q3: ' + str(q3_idade), fontsize=10, color='blue')
plt.text(1.23,max_idade, 'Média: ' + str(media_idades), fontsize=10)
plt.boxplot(df_sal_sem_outliers['Idade'])
plt.title('Boxplot da Idade')
plt.xlabel('Idade')
plt.show()
# Deu certo. Agora irei usar df sem outliers para minhas análises



#Para entender o relacionamento entre 'Salário' e 'Idade', 
# você pode criar um gráfico de dispersão:
plt.scatter(df_sal_sem_outliers['Idade'], df_sal_sem_outliers['Salário'])
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Relação entre Idade e Salário')
plt.show()

#Isso permitirá visualizar como a idade dos funcionários se relaciona com seus salários. 
# Se houver uma tendência visível, isso pode indicar uma relação.

#Da mesma forma, para entender o relacionamento entre 'Salário' e 'Tempo de casa', 
# você pode criar um gráfico de dispersão:

plt.scatter(df_sal_sem_outliers['Tempo de casa'], df_sal_sem_outliers['Salário'])
plt.xlabel('Tempo de casa (anos)')
plt.ylabel('Salário')
plt.title('Relação entre Tempo de casa e Salário')
plt.show()

#Isso permitirá visualizar como o tempo de serviço dos funcionários se relaciona com seus salários.

#Para quantificar a relação entre as variáveis, você pode calcular a correlação 
# entre 'Salário' e 'Idade' e entre 'Salário' e 'Tempo de casa':
#A correlação varia de -1 a 1. Um valor próximo de 1 indica uma correlação positiva forte, 
# enquanto um valor próximo de -1 indica uma correlação negativa forte.

correlacao_idade_salario = df_sal_sem_outliers['Idade'].corr(df_sal_sem_outliers['Salário'])
print(f"Correlação entre Idade e Salário: {correlacao_idade_salario}")
#-0.1943 (resultado calculado com os outliers)
#-0.0880 (resultado calculado sem os outliers)

# Análise dos resultados segundo o chatGPT:
'''A correlação entre 'Idade' e 'Salário' é negativa em ambos os casos, o que sugere que à medida que 
a idade aumenta, o salário tende a diminuir ligeiramente. No entanto, o valor absoluto da correlação 
é relativamente baixo em ambas as situações. No primeiro caso (com outliers), a correlação é -0.1943, 
o que indica uma correlação fraca, mas ainda existe uma tendência negativa. No segundo caso (sem outliers), 
a correlação é ainda mais próxima de zero, -0.0880, o que sugere uma correlação ainda mais fraca. 
A remoção dos outliers parece ter diminuído a magnitude da correlação, mas a tendência geral permanece.'''

correlacao_tempo_casa_salario = df_sal_sem_outliers['Tempo de casa'].corr(df_sal_sem_outliers['Salário'])
print(f"Correlação entre Tempo de casa e Salário: {correlacao_tempo_casa_salario}")
#-0.3862 (resultado calculado com os outliers)
#-0.3811 (resultado calculado sem os outliers)


# Análise dos resultados segundo o chatGPT:
'''A correlação entre 'Tempo de casa' e 'Salário' também é negativa em ambos os casos. 
Neste caso, a correlação é um pouco mais forte do que a correlação entre 'Idade' e 'Salário',
mas ainda é considerada moderada ou fraca. A remoção dos outliers teve apenas um 
pequeno impacto na magnitude da correlação.

Em resumo, mesmo após a remoção dos outliers, as correlações entre 'Idade' e 'Salário' 
e entre 'Tempo de casa' e 'Salário' ainda são fracas ou moderadas. Isso indica que, 
do ponto de vista estatístico, não há uma relação muito forte entre essas variáveis 
independentemente de os outliers serem considerados ou não. Portanto, é possível concluir 
que os resultados não foram substancialmente afetados pela remoção dos outliers em termos de correlação.'''


