import pandas as pd
import matplotlib.pyplot as plt

funcionarios = [
    ['João',22,10000,1,2],
    ['Maria',26,4000,3,4],
    ['Joana',22,4000,1,2],
    ['Manuel',22,15000,1,2],
    ['Manuela',35,5000,10,2],
    ['José',35,2000,8,2],
    ['Josefina',22,4000,1,4],
    ['Odilea',30,2000,5,2],
    ['Helio',40,8000,15,2],
    ['Anselmo',24,12000,2,4]
]

#Lista nome das colunas
colunas = ['Funcionario','Idade','Salário','Tempo de casa','Passagens']

#criação do DF
df_funcionarios = pd.DataFrame(funcionarios,columns=colunas)

#Calculando os quartis

q1_salario = df_funcionarios['Salário'].quantile(0.25)
q2_salario = df_funcionarios['Salário'].quantile(0.50)
q3_salario = df_funcionarios['Salário'].quantile(0.75)

print('Quartis')
print('Q1 (25%):',q1_salario)
print('Q2 (50%):',q2_salario)
print('Q3 (75%):',q3_salario)
print('Média:', df_funcionarios['Salário'].mean())

#visualizando dados
df_funcionarios.boxplot(column=['Salário'])
plt.show()