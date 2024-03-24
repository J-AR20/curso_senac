import pandas as pd
import numpy as np

#obter os dados
dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' \
                    , sep=';', encoding='ISO-8859-1')

#excluir dados de 2024
dados = dados[dados['ano'] <= 2023]

print(dados.info())

# vamos ver se há alguma correlação entre todas as variáveis de ocorrencia policial
# testaremos todas as ocorrencias entre homicidio doloso (coluna 9) e morte de poiciais em serviço (coluna 60)

# vamos extrair apenas os dados que queremos 
dados_correlacao = dados.iloc[:,9:61] # antes da linha estamos pegando todas as linhas; depois pegamos as colunas entre 9 e 61

# correlação
correlacao = dados_correlacao.corr()

# filtrar correlacao acima de 0.85
correlacao = correlacao[correlacao >= 0.80]

#exportar para o excel
endereco = r'D:\BIG DATA - SENAC\UC3 - Machine Learning\AULA_04'
correlacao.to_excel(endereco + r'\correlacao.xlsx')

