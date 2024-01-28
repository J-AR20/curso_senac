# 2) Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a média das idades e o nome da pessoa mais velha.

maior_idade = 0
soma_idade = 0

for x in range(1,11):
	nome = str(input("Qual o seu nome: "))
	idade = int(input("Qual sua idade: "))
	soma_idade = idade + soma_idade
	if idade > maior_idade:
		maior_idade = idade
		maior_nome = nome
media_idade = soma_idade / 3
print(f"A media das idades foi {media_idade:.2f}")
print(f"O nome da pessoa mais velha é {maior_nome.upper()}")


# Solução professor:
maioridade = 0
somaidade = 0
for cont in range(10):
    nome = input("Informe o Nome da Pessoa: ")
    idade = int(input("Informe a Idade da Pessoa: "))
    somaidade = somaidade + idade
    if idade > maioridade:
        maioridade = idade
        maiornome = nome
mediaidade = somaidade / cont+1
print(f"Sr(a) {maiornome.upper()} você é a pessoa mais velha")
print(f"A Média das Idades é:{mediaidade:.2f}")