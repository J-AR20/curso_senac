soma = 0  # Aqui criamos um acumulador ou empilhador dos valores que estão sendo fornecidos

for cont in range(10):
    num = int(input("Informe o Valor: "))
    soma = soma + num
print("O resultado da soma é: " + str(soma))