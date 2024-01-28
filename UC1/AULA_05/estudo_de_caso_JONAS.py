# Estudo de caso
amostra = []
sex_ent = []
ida_ent = []
ava_ent = []
qtd_ava_s = 0
qtd_ava_n = 0

for entrevistado in range(3):
    sexo = input("Qual o seu sexo (M/F)? ")  # preciso de tratamento de erro para aceitar m/f minúsculo e recusar números ou outras letras...
    sex_ent.append(sexo)
    idade = int(input("Qual sua idade? ")) # preciso de tratamento de erro para números negativos, zero ou inserção de letras...
    ida_ent.append(idade)
    avaliacao = input("Gostou do produto (S/N)? ") # preciso de tratamento de erro para aceitar s/n minúsculo e recusar números ou outras letras...
    ava_ent.append(avaliacao)
    if avaliacao == "s" or avaliacao == "S":
        qtd_ava_s = qtd_ava_s + 1
    else:
        qtd_ava_n = qtd_ava_n + 1
for i in range(len(sex_ent)):
    tupla = (sex_ent[i], ida_ent[i], ava_ent[i])
    amostra.append(tupla)

# 4) Quantas pessoas maiores de 18 anos gostaram do produto
# 5) Quantas pessoas menores de 18 anos não gostaram do produto
maioridade = 0
menoridade = 0
maioridade = sum(1 for i in range(len(sex_ent)) if ida_ent[i] > 18 and ava_ent[i] == "S")
menoridade = sum(1 for i in range(len(sex_ent)) if ida_ent[i] < 18 and ava_ent[i] == "N")

# 6) Quantas pessoas maiores de 18 anos, do sexo feminino, não gostaram do produto
# 7) Quantas pessoas menores de 18 anos, do sexo masculino, gostaram do produto
maioridade_fem_ava_n = 0
menoridade_mas_ava_s = 0
maioridade_fem_ava_n = sum(1 for i in range(len(sex_ent)) if ida_ent[i] > 18 and sex_ent[i] == "F" and ava_ent[i] == "N")
menoridade_mas_ava_s = sum(1 for i in range(len(sex_ent)) if ida_ent[i] < 18 and sex_ent[i] == "M" and ava_ent[i] == "S")

print(f"O total de pessoas que participaram da pesquisa foi {len(sex_ent)}")
print(f"O número de pessoas que responderam 'SIM' foi {qtd_ava_s}")
print(f"O número de pessoas que responderam 'NÃO' foi {qtd_ava_n}")
print(f"O número de pessoas maiores de 18 anos que gostaram do produto foi {maioridade}")
print(f"O número de pessoas menores de 18 anos que não gostaram do produto foi {menoridade}")
print(f"Pessoas maiores de 18 anos, do sexo feminino, que não gostaram do produto: {maioridade_fem_ava_n}")
print(f"Pessoas menores de 18 anos, do sexo masculino, que gostaram do produto: {menoridade_mas_ava_s}")
