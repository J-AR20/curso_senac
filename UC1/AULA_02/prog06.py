# Vamos aprender a utilizar a biblioteca Date Time

from datetime import date
# ano = date.today()
# print(ano)

# # Para extrair apenas o ano:
# ano = date.today().year
# print(ano)

# # Para extrair apenas o mês:
# mes = date.today().month
# print(mes)

# # Para extrair apenas o dia:
# dia = date.today().day
# print(dia)

# Jeito raiz (manual) de pegar a data no padrão brasileiro
# data = date.today()
# print(str(data.day)+"/"+str(data.month)+"/"+str(data.year))

# Outra forma:
# print(str(date.today().day)+"/"+str(date.today().month)+"/"+str(date.today().year))

# O correto:
data = date.today()
print(data.strftime("%d/%m/%Y"))


