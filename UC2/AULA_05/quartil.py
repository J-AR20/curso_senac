import pandas as pd
import matplotlib.pyplot as plt

'''A Gerente de Recursos Humanos da sua empresa te passou a seguinte tabela 
de dados:

Funcionário Idade Salário Tempo de casa Passagens
João 22 10000 1 2
Maria 26 4000 3 4
Joana 22 4000 1 2
Manuel 22 15000 1 2
Manuela 35 5000 10 2
José 35 2000 8 2
Josefina 22 4000 1 4
Odilea 30 2000 5 2
Helio 40 8000 15 2
Anselmo 24 12000 2 4

E, a partir dessa tabela, ela disse que precisa criar um processo automatizado, 
onde seja possível observar, através de dados estatísticos e visualização, a 
concentração das idades, dividida por quartis.'''


df_funcionarios = pd.DataFrame (
    [
        ["João", 22, 10000, 1, 2],
        ["Maria", 26, 4000, 3, 4],
        ["Joana", 22, 4000, 1, 2],
        ["Manuel", 22, 15000, 10, 2],
        ["Manuela", 35, 5000, 8, 2],
        ["José", 35, 2000, 8, 2],
        ["Josefina", 22, 4000, 1, 4], 
        ["Odilea", 30, 2000, 5, 2], 
        ["Helio", 40, 8000, 15, 2],
        ["Anselmo", 24, 12000, 2, 4]          
    ]
)

df_funcionarios.columns = ["Funcionário", "Idade", "Salário", "Tempo de casa", "Passagens"]


q1_salarios = df_funcionarios['Idade'].quantile(0.25)
q2_salarios = df_funcionarios['Idade'].quantile(0.50)
q3_salarios = df_funcionarios['Idade'].quantile(0.75)
media_idades = df_funcionarios['Idade'].mean()

# Vizualizando os dados
print(f'O primeiro quartil das idades é: {q1_salarios}')
print(f'O segundo quartil das idades é: {q2_salarios}')
print(f'O terceiro quartil das idades é: {q1_salarios}')
print(f'A média das idades é: {media_idades}')

df_funcionarios.boxplot(column=['Idade'])
plt.show()