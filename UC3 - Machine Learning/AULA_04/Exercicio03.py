import pandas as pd
import numpy as np

#obter os dados
dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv' \
                    , sep=';', encoding='ISO-8859-1')


# explorando os dados
print(dados.info())

valores_unicos = dados['upp'].unique()
print(valores_unicos) # UPP desejada 'Vila Kennedy'

# Selecionando os dados
dados_upp_vk = dados[dados['upp'] == 'Vila Kennedy']
print(dados_upp_vk.head())

# Selecionando apenas o crimes
crimes_vk = dados_upp_vk.iloc[:,4:23].join(dados_upp_vk.iloc[:,24:25]).join(dados_upp_vk.iloc[:,26:41])
# preciso checar e ver se isso deu ou não certo!!!!! 
print(crimes_vk.head())

# correlação
correlacao = crimes_vk.corr()

# filtrar correlacao acima de 0.85
correlacao = correlacao[correlacao >= 0.80]

#exportar para o excel
endereco = r'D:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_04'
correlacao.to_excel(endereco + r'\correlacao_upp.xlsx')