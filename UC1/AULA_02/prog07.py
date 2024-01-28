# Praticando
# 1 - Escreva um programa que, dados 2 número inteiros (n1 e n2), diga se eles são iguais ou diferentes.

n1 = int(input("Diga um número qualquer: "))
n2 = int(input("Diga outro número qualquer - pode ser ou não igual ao primeiro: "))
if n1 == n2:
    sit = (" valores iguais. ")
else:
    sit = (" valores diferentes. ")
print("Analisando os números podemos dizer que eles são" + sit + "Foram, respectivamente, " + str(n1) + " e " + str(n2) + ".")
if sit == " valores iguais. ":
    soma = n1 + n2
    print("A soma deles é " + str(soma) + ".")
else:
    multiplica = n1 * n2
    print("O produto deles é " + str(multiplica) + ".")

# Praticando
# Solução do professor!!! Mil vezes melhor que a minha


n1 = int(input("Diga um número qualquer: "))
n2 = int(input("Diga outro número qualquer - pode ser ou não igual ao primeiro: "))
if n1 == n2:
    print("São iguais, portanto a soma é:", (n1 + n2))
else:
    print("São diferentes, portanto o produto é:", (n1 * n2))