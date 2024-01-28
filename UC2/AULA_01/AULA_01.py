

notas = [6,7,5,9,7,8,10]
print(notas)


# Forma como transformamos um vetor unidimensional num conjunto de dados bidimensional, uma série lida no Pandas:
# Apelidaremos a biblioteca pandas como 'pd' para ser mais fácil de mencioná-la no código. Isso é uma conveção seguida no mundo todo.

import pandas as pd  
notas_serie = pd.Series(notas)
print(f'Aqui vemos a saída de uma lista, unidimensional: {notas}') 
print(f'Aqui vemos a saída de uma série: {notas_serie}')

# A saída do pandas, que apresenta um índice dos dados é muito importante porque ele nos ajuda a individualizar um determinado dado


