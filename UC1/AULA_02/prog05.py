# Vamos falar de Tratamentos de Erro
# Montar um programa onde o usuário fornece o ano de nascimento
# Essa pessoa, qual sua idade? Ela é maior ou menor de idade?

from datetime import date
ano = int(input("Me diga o ano que você nasceu: "))
idade = 2023 - ano  # Essa solução é precária. Um jeito de utilizar a data atual da máquina será útil.
if idade >= 18:
    sit = "maior de idade."
else:
    sit = "menor de idade."
print("A pessoa possui", idade, "anos e é", sit)

# Para resolver a incosistência do programa vamos usar a biblioteca datetime do python

from datetime import date
nasc = int(input("Me diga o ano que você nasceu: "))
ano = date.today().year # Essa solução é a que resolve o problema de atualização manual do ano base de calculo da idade.
idade = ano - nasc  
if idade >= 18:
    sit = "maior de idade."
else:
    sit = "menor de idade."
print("A pessoa possui"+ idade+ "anos e é"+ sit)

# Vamos aumentar o número e condições - verificar se a pessoa tem acima de 65 (idoso)

from datetime import date
nasc = int(input("Me diga o ano que você nasceu: "))
ano = date.today().year
idade = ano - nasc  
if idade < 18:
    sit = "jovem."
elif idade >= 18 and idade < 65:
    sit = "adulta."
else:
    sit = "idosa."

print("A pessoa possui "+ str(idade)+ " anos e é "+ sit)





