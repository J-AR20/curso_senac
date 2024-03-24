import pandas as pd

endereco = r'C:\Users\36131872023.1\Documents'

dados = pd.read_csv(endereco + r'\202311_NovoBolsaFamilia.csv', sep=';', encoding='ISO-8859-1')

dados = dados[['NOME MUNICÍPIO', 'VALOR PARCELA']]

#substituir , por .
dados['VALOR PARCELA'] = dados['VALOR PARCELA'].str \
                        .replace(',','.').astype(float)

#print(dados.info())

# filtro de cidade
# PLN - Processamento de Linguagem Natural
import spacy

#carregar o modelo de idioma
nlp = spacy.load('pt_core_news_lg')

#solitar município para o usuário
texto_usuario = input('Solicite a sua análise por Município: ')

#processar o texto do usuário com o modelo PLN (NLP)
doc = nlp(texto_usuario)

#identificar as entidades
munics_solicitados = []
for entidade in doc.ents:
    if entidade.label_ in ('LOC', 'GPE'):
        munics_solicitados.append(entidade.text.upper())

dados['NOME MUNICÍPIO'] = dados['NOME MUNICÍPIO'].str.upper()

if munics_solicitados:
    dados = dados[dados['NOME MUNICÍPIO'].isin(munics_solicitados)]
else:
    print('Desculpe! Não identifiquei o Município. Refaça sua solicitação.')
    exit()

ranking = dados.groupby('NOME MUNICÍPIO').sum('VALOR PARCELA') \
                .reset_index()

print(ranking)

import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))

plt.barh(ranking['NOME MUNICÍPIO'], ranking['VALOR PARCELA'])

plt.xlabel('Município')
plt.ylabel('Valor da parcela')

plt.show()