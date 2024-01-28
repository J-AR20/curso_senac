# A revendedora de carros Pica-Pau Ltda. paga aos seus funcionários vendedores um salário fixo de R$2500,00, 
# mais uma comissão fixa de R$500,00 por carro vendido e mais 5% do valor das vendas. 
# Faça um programa que determine o salário total de um vendedor.

faturamento = int(input("Informe o faturamento da revendedora no ano: "))
n_carro_vendido = int(input("Me diga quantos carros o vendedor x vendeu no mês: "))
comissao_carro_vendido = n_carro_vendido * 500
bonus = faturamento * 0.05
salario_inicial = 2500
salario_final = salario_inicial + comissao_carro_vendido + bonus
print("O salário fixo do vendedor de R$2500 acrescido da comissão de R$500 por carro vendido, mais 5% sobre o valor das vendas chega ao montante: R$" + str(salario_final))
