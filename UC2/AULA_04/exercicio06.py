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

df_rh = pd.DataFrame (
    [
        ["João", 22, 10000, 1, 2],
        ["Maria", 26, 4000, 3, 4],
        ["Joana", 22, 4000, 1, 2],
        ["Manuel", 22, 15000, 1, 2],
        ["José", 35, 2000, 8, 2],
        ["Josefina", 22, 4000, 1, 4], 
        ["Odilea", 30, 2000, 5, 2], 
        ["Helio", 40, 8000, 15, 2],
        ["Anselmo", 24, 12000, 2, 4]          
    ]
)

df_rh.columns = ["Funcionário", "Idade", "Salário", "Tempo de casa", "Passagens"]

# 1. De acordo com as passagens dos funcionários qual a quantidade mais frequente?

#df_rh.iloc['Moda'] = # df_rh.iloc[:,5:5].mode(axis=0)


print(df_rh.loc["Passagens"])
#df_rh

# 2. Qual a média salarial?

# 3. Qual a idade central dos meus funcionários?

# 4. Qual o maior e menor tempo de casa, bem como a diferença entre eles?

# 5. Qual a média de tempo de casa?

# 6. Qual o funcionário mais novo e mais velho, bem como a diferença de idade entre eles?

# 7. Qual a média de idade?

# 8. Qual o total de funcionários?

# 9. Qual o nome do funcionário com maior salário?

# 10.Qual o nome do funcionário com maior tempo de casa?
