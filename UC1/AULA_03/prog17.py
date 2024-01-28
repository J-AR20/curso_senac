# 3) Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e ao final mostre a média da turma e a situação de cada aluno de acordo com as seguintes condições:

# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO

# soma_n_turma = 0
# media_aluno = []

# for nota in range(1,4):
# 	nome = input("Informe o Nome do Estudante: ")
# 	p1 = float(input("Informe a primeira nota: "))
# 	p2 = float(input("Informe a segunda nota: "))
# 	media_aluno = (p1 + p2) / 2
# 	soma_n_turma = soma_n_turma + media_aluno
# 	if media_aluno >= 70:
# 	    sit = "ATENDIDO"
# 	elif media_aluno >= 30 and media_aluno < 70:
# 	    sit = "PARCIALMENTE ATENDIDO"
# 	else:
# 	    sit = "NÃO ATENDIDO"
#     print(f"Sr(a) {nome.upper()}, você foi {sit}, pois sua média foi {media_aluno:.2f}")
# media_turma = soma_n_turma / (nota+1)
# print(f"A media da turma foi {media_turma:.2f}")


# Resolução professor:	
	
somamedia = 0
for cont in range(5):
	nome = input("Informe o Nome do Estudante: ")
	n1 = float(input("Informe a Primeira Nota: "))
	n2 = float(input("Informe a Segunda Nota: "))
	media = (n1+n2)/2
	somamedia = somamedia + media
	if media >= 70:
		sit = "ATENDIDO"
	elif media >= 30 and media < 70:
		sit = "PARCIALMENTE ATENDIDO"
	else:
		sit = "NÃO ATENDIDO"
	print(f"Sr(a) {nome}, você foi {sit}, pois sua média foi {media:.2f}")
mediaturma = somamedia / (cont+1)
print(f"A média da turma foi {mediaturma:.2f}")
