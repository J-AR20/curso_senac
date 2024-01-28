# Dando continuidade ao exercicio da aula passada

# Vnum = []
# Vpar = []
# Vimpar = []
# qtdpar = 0
# qtdimpar = 0

# for i in range(5):
#     Vnum.append(int(input("Informe o valor: ")))
# for i in range(len(Vnum)):
#     if Vnum[i]%2==0:
#         Vpar.append(Vnum[i])
#         qtdpar = qtdpar + 1
#     else:
#         Vimpar.append(Vnum[i])
#         qtdimpar+=1
# print(Vpar)
# print(Vimpar)
# print(f"A quantidade de pares é {qtdpar} e a quantidade de ímpares é {qtdimpar}")


# Outra forma com um pequena mudança


Vnum = []
Vpar = []
Vimpar = []

for i in range(5):
    Vnum.append(int(input("Informe o valor: ")))
for i in range(len(Vnum)):
    if Vnum[i]%2==0:
        Vpar.append(Vnum[i])
    else:
        Vimpar.append(Vnum[i])
print(Vpar)
print(Vimpar)
print(f"A quantidade de pares é {len(Vpar)} e a quantidade de ímpares é {len(Vimpar)}")


