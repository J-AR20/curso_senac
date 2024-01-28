import pandas as pd

nota1 = pd.Series([6,7,5,9,7,6,8,10])
nota2 = pd.Series([7,5,8,6,9,6,7,8])

media = (nota1+nota2)/2

aprovado = []
reprovado = []

for i in media:
    if i >= 7:
        aprovado = aprovado.append[i]
    else:
        reprovado = reprovado.append[i]

print(aprovado) 
print(reprovado)