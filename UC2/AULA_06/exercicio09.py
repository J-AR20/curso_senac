import pandas as pd
import matplotlib.pyplot as plt

#endereço do arquivo de dados
endereco_arquivo = r'C:\uc2_bigdata\Dados'

#leitura do arquivo
df_funcionario = pd.read_excel(endereco_arquivo + r'\funcionarios.xlsx')

#print(df_funcionario)

#calcular a variância
var_salario = df_funcionario['Salário'].var()

#calcular o desvio padrão
devp_salario = df_funcionario['Salário'].std()

#calcular a média 
media_salario = df_funcionario['Salário'].mean()

#Exibir as medidas
print('Variância: ', var_salario)
print('Desvio padrão: ', devp_salario)
print('Média: ', media_salario)

#configurar o layout da página
plt.figure(figsize=(12,6))

#gráfico de barras
plt.subplot(1, 2, 1)
plt.barh(df_funcionario['Funcionário'], df_funcionario['Salário'])
plt.title('Salário por funcionário')
plt.xlabel('Salário')
plt.ylabel('Funcionário')

#boxplot
plt.subplot(1,2,2)
df_funcionario.boxplot(column=['Salário'])

#exibir os gráfico
plt.show()