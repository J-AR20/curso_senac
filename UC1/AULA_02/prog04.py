# Nessa aula vamos falar de Estruturas de Controle
# A tarefa é mostrar que se um aluno tem uma média inferior a 70 está reprovado, do contrário, aprovado

# A forma mais simples é essa aqui: 
# nome = input("Qual o nome do aluno: ")
# n1 = float(input("Informe a nota 1: "))
# n2 = float(input("Informe a nota 2: "))
# media = (n1 + n2) / 2
# if media >= 70:
#     print("A média do aluno", nome, "é", str(media), "e ele foi APROVADO")
# else:
#     print("A média do aluno", nome, "é", str(media), "e ele foi REPROVADO")

# A forma que eu fiz foi essa aqui:

# nome = input("Qual o nome do aluno: ")
# n1 = float(input("Informe a nota 1: "))
# n2 = float(input("Informe a nota 2: "))
# media = (n1 + n2) / 2
# indice = (n1 + n2) / 2
# if indice >= 70:
#     indice = "aprovado"
# else:
#     indice = "reprovado"
# print("A média do aluno", nome, "é", str(media), "e ele foi", indice)

# A forma do professor - ideal - foi essa aqui:
nome = input("Qual o nome do aluno: ")
n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
media = (n1 + n2) / 2
if media >= 70:
    sit = str.upper("aprovado!")
else:
    sit = str.upper("reprovado!")
print("A média do aluno", nome, "é", str(media), "e ele foi", sit)
