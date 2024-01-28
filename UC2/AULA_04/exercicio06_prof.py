'''A Gerente de Recursos Humanos da sua empresa te passou a seguinte tabela 
de dados:

"Funcionário" "Idade" "Salário" "Tempo de casa" "Passagens"
"João" 22 10000 1 2
"Maria" 26 4000 3 4
"Joana" 22 4000 1 2
"Manuel" 22 15000 1 2
"Manuela" 35 5000 10 2
"José" 35 2000 8 2
"Josefina" 22 4000 1 4
"Odilea" 30 2000 5 2
"Helio" 40 8000 15 2
"Anselmo" 24 12000 2 4

E, a partir dessa tabela, ela disse que precisa criar um processo automatizado, 
onde seja possível responder (somente responder, nada mais) às seguintes 
perguntas:

Esse processo precisa ser automatizado, pois 1 vez por semana, ela precisará 
apresentar essas informações na reunião com a diretoria.'''

# Criar o DataFrame
import pandas as pd

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

df_funcionarios

# 1. De acordo com as passagens dos funcionários qual a quantidade mais frequente?
moda_passagens = df_funcionarios['Passagens'].mode().values[0]
print('A quantidade de passagens mais frequente é: ', moda_passagens)

# 2. Qual a média salarial?
media_salario = df_funcionarios['Salário'].mean()
print(f'A média dos salários é: {media_salario:.2f}')


# 3. Qual a idade central dos meus funcionários?
idade_central = df_funcionarios['Idade'].median()
print(f'A idade central é: {idade_central}')


# 4. Qual o maior e menor tempo de casa, bem como a diferença entre eles?
max_tempo = df_funcionarios['Tempo de casa'].max()
min_tempo = df_funcionarios['Tempo de casa'].min()
amplitude = max_tempo - min_tempo
print(f'O maior tempo de casa: {max_tempo}')
print(f'O menor tempo de casa: {min_tempo}')
print(f'A diferença entre o maior e o menos tempo de casa (a amplitude) é: {amplitude}')


# 5. Qual a média de tempo de casa?
media_tempo_de_casa = df_funcionarios['Tempo de casa'].mean()
print(f'A média do tempo de casa é: {media_tempo_de_casa:.2f}')


# 6. Qual o funcionário mais novo e mais velho, bem como a diferença de idade entre eles?
func_novo = df_funcionarios['Idade'].min()
func_velho = df_funcionarios['Idade'].max()
amplitude_idade = func_velho - func_novo
print(f'O funcionário mais novo tem: {func_novo}')
print(f'O funcionário mais velho tem: {func_velho}')
print(f'A diferença de idade entre o mais velho e o mais velho (a amplitude) é: {amplitude_idade}')

# 7. Qual a média de idade?
media_idade = df_funcionarios['Idade'].mean()
print(f'A média de idade é: {media_idade:.2f}')

# 8. Qual o total de funcionários?
total_func = df_funcionarios['Funcionário'].count()
print(f'O total de funcionários é: {total_func}')


# 9. Qual o nome do funcionário com maior salário?
maior_salario = df_funcionarios['Salário'].max()
func_maior_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Funcionário'].values[0]
print(f'O nome do funcionário com o maior salário é: {func_maior_salario}')


# 10.Qual o nome do funcionário com maior tempo de casa?
maior_tempo = df_funcionarios['Tempo de casa'].max()
func_maior_tempo = df_funcionarios[df_funcionarios['Tempo de casa'] == maior_tempo]['Funcionário'].values[0]
print(f'O nome do funcionário com o maior tempo de casa é: {func_maior_tempo}')









