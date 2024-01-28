# Exercicio: 2- Faça um programa que receba do usuário o nome e a idade de 10 pessoas. 
# Ao final mostre a média das idades e o nome da pessoa mais velha

# Dica: ao invés de mostrar o nome da pessoa mais velha mostre a idade para ver se deu certo.

# Solução chatGPT
# nomes = []
# idades = []

# # Recebendo nome e idade de 10 pessoas
# for i in range(1, 11):
#     nome = input(f"Informe o nome da {i}ª pessoa: ")
#     idade = int(input(f"Informe a idade de {nome}: "))
    
#     nomes.append(nome)
#     idades.append(idade)

# # Calculando a média das idades
# media_idades = sum(idades) / len(idades)

# # Encontrando a pessoa mais velha
# indice_mais_velha = idades.index(max(idades))
# pessoa_mais_velha = nomes[indice_mais_velha]

# # Exibindo os resultados
# print(f"\nMédia das idades: {media_idades:.2f} anos")
# print(f"Pessoa mais velha: {pessoa_mais_velha} com {max(idades)} anos")


# 1) Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.

maior = []
contador = 0

for x in range(1,6):
	numero = int(input("Digite um numero: "))
	maior.append(numero)
	if numero > contador:
		contador = numero
print(f"A soma de todos os n é {maior[0]+maior[1]+maior[2]+maior[3]+maior[4]}")
print(f"O maior número digitado foi {contador}")


# Outra forma de resolver a soma seria: 
	
soma_n = 0
cont = 0

for y in range(1,6):
	num = int(input("Digite um numero: "))
	soma_n = soma_n + num
	if num > cont:
		cont = num
print(f"A soma de todos os n é {soma_n}")
print(f"O maior número digitado foi {cont}")