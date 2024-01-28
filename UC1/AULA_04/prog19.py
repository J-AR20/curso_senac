Vnomes = []
Vidades = []
resultado = []
for i in range(3):
    Vnomes.append(input("Informe o nome: "))
    Vidades.append(int(input("Informe a idade: ")))
for i in range(len(Vidades)):
    tupla = (Vnomes[i], Vidades[i])
    resultado.append(tupla)
for r in resultado:
    print(r)