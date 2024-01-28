# Usando listas (método tradicional do Python)

notas = [6,7,5,9,7,8,10]
aprovados = []
reprovados = []

for i in notas:
  if (i >= 7):
    aprovados.append(i)
  else:
    reprovados.append(i)

print(f'Aprovados: {aprovados}')
print(f'Reprovados: {reprovados}')

# Usando listas (método Pandas)

import pandas as pd
notas_serie = pd.Series([6,7,5,9,7,8,10])

serie_notas_maiores_7 = notas_serie[notas_serie >= 7]
serie_notas_menores_7 = notas_serie[notas_serie < 7]

print(f'Lista dos alunos aprovados:')
print(serie_notas_maiores_7)
print(f'Lista dos alunos reprovados:')
print(serie_notas_menores_7)
