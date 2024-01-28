# Exercicio para o while

# resp = "S"
# while resp == "S":
#     nome = input("Informe o seu nome: ")
#     idade = int(input("Informe sua idade: "))
#     resp = input("Deseja continuar (S/N)? ")

# Importante perceber que o Python é "case sensitive", ou seja, um 's' minúsculo ali dá Ruim.
# Para escapar desse erro podemos fazer o seguinte:

resp = "S"
while resp == "S" or resp == "s":  # utilizando o "or" para dar uma outra condição possível
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe sua idade: "))
    resp = input("Deseja continuar (S/N)? ")