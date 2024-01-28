# 2- Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos
# números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente

vetor = []
for n in range (4):
    elemento = int(input("Me dê um número: "))
    vetor.append(elemento)

for x in vetor:
    if x % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")


# Solução do professor:       
# Vnum = [2,3,7,9,1,5,10,15,4,8] 
Vnum = []
qtdpar = 0
qtdimpar = 0
for i in range(5):
    Vnum.append(int(input("Informe o valor: ")))
for i in range(len(Vnum)):
    if Vnum[i] % 2 == 0:
        qtdpar = qtdpar + 1
    else:
        qtdimpar +=1
print(f"A quantidade de pares é {qtdpar} e a quantidade de ímpares é {qtdimpar}")