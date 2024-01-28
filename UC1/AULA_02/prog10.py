# Um hotel cobra R$250,00 a diária para um casal e mais uma taxa de serviços. A taxa é:
# - R$15,00 por diária, se o número de diárias for maior que 15;
# - R$20,00 por diária, se o número de diárias for igual a 15;
# - R$30,00 por diária, se o número de diárias for menor que 15.
# Construa um programa que mostre o nome e o total da conta de um cliente.

nome_cliente = str(input("Diga o nome do cliente: "))
n_diarias = int(input("Quantas diárias vai ficar hospedado: "))
valor_diarias = n_diarias * 250

if n_diarias > 15:
    total1 = int((n_diarias * 15) + valor_diarias)
    print("O cliente " + nome_cliente + " deverá pagar em sua estadia R$ " + str(total1))
elif n_diarias == 15:
    total2 = int((n_diarias * 20) + valor_diarias)
    print("O cliente " + nome_cliente + " deverá pagar em sua estadia R$ " + str(total2))
else:
    total3 = int((n_diarias * 30) + valor_diarias)
    print("O cliente " + nome_cliente + " deverá pagar em sua estadia R$ " + str(total3))

