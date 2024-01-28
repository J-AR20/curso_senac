# Estudo de caso
sex_ent = []
ida_ent = []
ava_ent = []
qtd_ava_s = 0
qtd_ava_n = 0

# Início da Estrutura para Armazenar os Dados nos Vetores
while ava_ent == "S" or ava_ent == "s":
    # Início do Tratamento de Erro - Variável Sexo
    while True:
        sexo = input("Qual o seu sexo (M/F)? ")
        if sexo == "M" or sexo == "F":
            sex_ent.append(sexo)
            break
    # Fim do Tratamento de Erro - Variável Sexo
        
    ida_ent.append(int(input("Informe a Idade do Entrevistado: ")))
    ava_ent.append(input("Informe se o Entrevistado Gostou ou Não do Produto (S ou N): "))
    total = total + 1 # Total de Pessoas
# Fim da Estrutura para Armazenar os Dados nos Vetores

# Início da Estrutura para Coletar os Dados nos Vetores   
for i in range(len(sexo)):
    if ava_ent[i]  == "S" or ava_ent[i]  == "s": 
        qtd_ava_s = qtd_ava_s + 1 # Total de Pessoas que Responderam Sim
    else: 
        qtd_ava_n = qtd_ava_n + 1 # Total de Pessoas que Responderam Não

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
