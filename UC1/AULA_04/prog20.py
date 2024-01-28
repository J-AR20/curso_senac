# 1 - Faça um programa que receba do usuário um vetor com 10 posições. 
# Em seguida deverá ser impresso o maior e o menor elemento do vetor.
vetor = []

for n in range (5):
    elemento = int(input("Me dê um número: "))
    vetor.append(elemento)
vetor.sort()
print(f"O maior elemento digitado foi {vetor[4]} enquanto o menor foi {vetor[0]}")


# Solução do professor:
Vnum = []
for i in range(5):
    Vnum.append(int(input("Informe o valor: ")))

maior = Vnum[0]
menor = Vnum[0]
for i in Vnum:
    if Vnum[i] >= maior:
        maior = Vnum[i]
    if Vnum[i] <= menor:
        menor = Vnum[i]
print(f"O maior valor é {maior} e o menor valor é {menor}")