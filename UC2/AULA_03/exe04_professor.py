"""Exercicio 04 - O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, 
o maior valor vendido e o menor valor vendido de seus 3 vendedores/as. 

Pediu para que fosse algo automatizado, pois como ele está em fase de expansão, nos próximos meses 
mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.

Ele te passou a venda dos últimos 7 dias, dos/as vendedores/as atuais:

->Maria: 800,700,1000,900,1200,600,600
->João: 900,500,1100,1000,900,500,700
->Manuel: 700,600,900,1200,900,700,400

Como resultado, ele gostaria de visualizar o Nome do/a vendedor/a, 
a média de venda, o maior valor vendido e o menor valor vendido dos últimos 7 dias.
"""

# Deveríamos fazer um array somente com os nomes e outro com os números.
# A ideia era que o código fosse automatizado para entrar novos vendedores

import numpy as np

vendas = np.array(
    [
        [800,700,1000,900,1200,600,600],
        [900,500,1100,1000,900,500,700],
        [700,600,900,1200,900,700,400]
    ]
)

print(vendas)

vendedores = ['Maria', 'João', 'Manuel']

for i in range(len(vendedores)):
    nome = vendedores[i]
    media = vendas[i].mean()
    menor = vendas[i].min()
    maior = vendas[i].max()
    
    print(f'{nome} ->', f'Média: {round(media,2)}',
                        f'Menor valor: {round(menor)}',
                        f'Maior valor: {round(maior)}')     