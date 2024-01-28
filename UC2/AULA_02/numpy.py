import numpy as np
import pandas as pd

notas_serie = pd.Series([10,8,9,7,5,7])
notas_array = np.array([10,8,9,7,5,7])
print(notas_array.shape)

# notas_serie.mean()  # ambas as bibliotecas compartilham as mesmas fçs (em alguns casos)
# notas_array.mean()

notas = np.array(
    [
        ['João',7.5,8.0,8.5,9.0],
        ['Maria',6.0,6.5,7.0,7.5],
        ['José',8.0,7.5,8.5,9.5]
    ]    
)

# Inspecionando o array:
print(notas.shape) # dimensões do array
print(notas.dtype) # tipo de dados dentro do array
# <U32 (significa que o tipo de dado é alfanumérico)

notas[1,3] # Nota da aluna Maria no 3ºBimestre

# Média de João
media_joao = notas[0,1:].astype(float).mean() # 1: (os ':' significa que pega todo mundo dali em diante)
print(media_joao) 

media_joao = notas