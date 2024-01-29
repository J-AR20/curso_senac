import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
#caminho_arquivo = 'D:/CURSOS/BIG DATA - SENAC/UC2/AULA_05/veiculos.xlsx' # computador de casa
#caminho_arquivo = 'C:/Users/jonas.araujo/OneDrive - IFEC-RJ/Área de Trabalho/data-science/CURSO SENAC/UC2/AULA_05/veiculos.xlsx' # computador do trabalho
caminho_arquivo = 'D:/BIG DATA - SENAC/UC2/AULA_05/veiculos.xlsx'

# Carregar o arquivo Excel em um DataFrame
dados = pd.read_excel(caminho_arquivo)


# 1) INTEGRAÇÃO E PREPARAÇÃO DOS DADOS
print("Visão geral dos dados:")
print(dados.head())  # Mostra as primeiras linhas do DataFrame

# Quais são as categorias que temos:
reg = dados["Regiao"].unique()
print(reg) # "Baixada Fluminense", "Capital", "Grande Niterói", "Interior"

years = dados["Ano"].unique()
print(years) # Últimos 20 anos, de 2003 a 2023

# Modificar os nomes das colunas para ser mais facil trabalhar
# Nomes anteriores = ['Ano', 'Regiao', 'Roubo veículos', 'Furto veículos', 'Recuperação veículos']
novas_colunas = ['ano', 'regiao', 'roubo', 'furto', 'recuperacao']
dados.columns = novas_colunas

print(dados.head())

dados
# O dataframe possui 84 linhas e 5 colunas

# Criando o parâmetro taxa de recuperação que não está presente no conjunto de dados:
dados['tx_recuperacao'] = dados['recuperacao'] / dados['roubo']
dados



# 2) ANÁLISE DE DADOS:

# 2.1) Realize o agrupamento dos dados por região (nesse momento não há a necessidade de se considerar os anos),
# calculando o total de  ocorrências de roubo e furto de veículos

soma_furtos = dados['furto'].sum(axis=0)
soma_roubos = dados['roubo'].sum(axis=0)
print(f'A quantidade de furtos foi {soma_furtos} enquanto a de roubos foi {soma_roubos}')

crimes_por_regiao = dados.groupby('regiao')[['furto', 'roubo', 'tx_recuperacao']].sum()
# Exibindo o resultado
print(crimes_por_regiao)

# 2.2) Crie uma coluna adicional a tabela inicial de dados, que represente esse total, 
# somando roubos e furtos por região
dados['t_roubo&furto'] = dados['roubo'] + dados['furto']
dados

# 2.3) Determine a taxa de recuperação de veículos em cada região, conforme regra negócio
tx_por_regiao = dados.groupby('regiao')[['tx_recuperacao']].sum()
# Exibindo o resultado
print(tx_por_regiao)



# 3) VISUALUZAÇÃO DOS RESULTADOS:

# 3.1) Desenvolva um gráfico de barras exibindo as taxas de recuperação 
# de veículos por região, ordenadas da maior para a menor. O gráfico deve 
# ser acompanhado de título e rótulos para cada eixo

# Ordenando os dados do maior para o menor
resultado_ordenado = tx_por_regiao.sort_values(by='tx_recuperacao', ascending=False)

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(resultado_ordenado.index, resultado_ordenado['tx_recuperacao'], color='skyblue')

# Adicionando título e rótulos aos eixos
plt.title('Taxa de recuperação por região')
plt.xlabel('Região do estado do RJ')
plt.ylabel('Taxa de recuperação')

# Mostrando o gráfico
plt.show()

# retirar linhas horizontais (grid)
plt.grid(False)

