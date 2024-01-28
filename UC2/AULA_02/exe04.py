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
# Minha solução:

import pandas as pd

Maria = pd.Series([800,700,1000,900,1200,600,600])
Joao = pd.Series([900,500,1100,1000,900,500,700])
Manuel = pd.Series([700,600,900,1200,900,700,400])

Media_Maria = Maria.mean()
Min_Maria = Maria.min()
Max_Maria = Maria.max()
print(f'A media de vendas nos ultimos 7 dias de Maria foi {Media_Maria:.2f}, o menor valor foi {Min_Maria} e o maior valor foi {Max_Maria}')
print('\n')
Media_Joao = Joao.mean()
Min_Joao = Joao.min()
Max_Joao = Joao.max()
print(f'A media de vendas nos ultimos 7 dias de João foi {Media_Joao:.2f}, o menor valor foi {Min_Joao} e o maior valor foi {Max_Joao}')
print('\n')
Media_Manuel = Manuel.mean()
Min_Manuel = Manuel.min()
Max_Manuel = Manuel.max()
print(f'A media de vendas nos ultimos 7 dias de Manuel foi {Media_Manuel:.2f}, o menor valor foi {Min_Manuel} e o maior valor foi {Max_Manuel}')

# Solução do professor:


