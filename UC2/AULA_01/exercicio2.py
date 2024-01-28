# Exercício 02: Verificar funcionário mais produtivo 

# O  Gerente  de  um  laboratório  de  informática  precisa  que  você  o  auxilie  a 
# identificar  todas  as  temperaturas  que  ficaram  acima  de  18º  nos  dados  dos 
# últimos 10 dias. 

# Ele te informou os seguintes dados relacionados aos registros da temperatura: 

17.15, 16.22, 18.57, 19.21, 21.73, 21.9, 16.99, 20.58, 18.7, 19.99, 21.49, 16.13, 
16.94, 15.55, 15.38, 19.56, 16.04, 16.92, 16.4, 21.8, 15.67, 20.83, 18.01, 15.9, 
19.24, 18.13, 16.49, 19.24, 16.47, 16.95 

# Como saída do programa ele gostaria de verificar somente aqueles que foram 
# maiores que 18º.

import pandas as pd

temp_alt = []
n_temp_alt = []
porcentagem_temp_alt = []

temperaturas = [17.15, 16.22, 18.57, 19.21, 21.73, 21.9, 16.99, 20.58, 18.7, 19.99, 21.49, 16.13, 
16.94, 15.55, 15.38, 19.56, 16.04, 16.92, 16.4, 21.8, 15.67, 20.83, 18.01, 15.9, 
19.24, 18.13, 16.49, 19.24, 16.47, 16.95]

for temperatura in temperaturas:
    if temperatura > 18:
        temp_alt.append(temperatura)

n_temp_alt = len(temp_alt)
porcentagem_temp_alt = (n_temp_alt / len(temperaturas)) * 100

output = f'''
O conjunto de temperaturas acima de 18º nos últimos dez dias foi:
{temp_alt}

Um total de {len(temp_alt)} registros ou {porcentagem_temp_alt:.2f}% da amostra.
'''
print(output)


# Solução do professor:
import pandas as pd

temperaturas = pd.Series([17.15, 16.22, 18.57, 19.21, 21.73, 21.9, 16.99, 20.58, 18.7, 19.99, 21.49, 16.13, 
16.94, 15.55, 15.38, 19.56, 16.04, 16.92, 16.4, 21.8, 15.67, 20.83, 18.01, 15.9, 
19.24, 18.13, 16.49, 19.24, 16.47, 16.95])

temperaturas_maiores_18 = temperaturas[temperaturas > 18]
temperaturas_menores_ou_iguais_18 = temperaturas[temperaturas <= 18]

print(temperaturas_maiores_18)
print(temperaturas_menores_ou_iguais_18)