# Definindo variáveis
total_pessoas = int(input("Digite o número total de pessoas entrevistadas: "))
sexo = []  # Lista para armazenar o sexo dos entrevistados
idade = []  # Lista para armazenar a idade dos entrevistados
resposta_produto = []  # Lista para armazenar as respostas sobre o produto

# Preenchendo as listas com as informações dos entrevistados
for i in range(total_pessoas):
    sexo_entrevistado = input(f"Digite o sexo da pessoa {i + 1} (M/F): ")
    idade_entrevistado = int(input(f"Digite a idade da pessoa {i + 1}: "))
    resposta_entrevistado = input(f"Digite a resposta sobre o produto da pessoa {i + 1} (S/N): ")

    sexo.append(sexo_entrevistado)
    idade.append(idade_entrevistado)
    resposta_produto.append(resposta_entrevistado)

# 1) O total de pessoas que participaram da pesquisa
total_participantes = len(sexo)

# 2) O número de pessoas que responderam "Sim" ou "S"
num_responderam_sim = resposta_produto.count('S')

# 3) O número de pessoas que responderam "Não" ou "N"
num_responderam_nao = resposta_produto.count('N')

# 4) Quantas pessoas maiores de 18 anos gostaram do produto
maiores_18_gostaram = sum(1 for i in range(total_participantes) if idade[i] > 18 and resposta_produto[i] == 'S')

# 5) Quantas pessoas menores de 18 anos não gostaram do produto
menores_18_nao_gostaram = sum(1 for i in range(total_participantes) if idade[i] < 18 and resposta_produto[i] == 'N')

# 6) Quantas pessoas maiores de 18 anos, do sexo feminino, não gostaram do produto
maiores_18_feminino_nao_gostaram = sum(1 for i in range(total_participantes) if idade[i] > 18 and sexo[i] == 'F' and resposta_produto[i] == 'N')

# 7) Quantas pessoas menores de 18 anos, do sexo masculino, gostaram do produto
menores_18_masculino_gostaram = sum(1 for i in range(total_participantes) if idade[i] < 18 and sexo[i] == 'M' and resposta_produto[i] == 'S')

# Exibindo os resultados
print(f"Total de pessoas entrevistadas: {total_participantes}")
print(f"Número de pessoas que gostaram do produto: {num_responderam_sim}")
print(f"Número de pessoas que não gostaram do produto: {num_responderam_nao}")
print(f"Pessoas maiores de 18 anos que gostaram do produto: {maiores_18_gostaram}")
print(f"Pessoas menores de 18 anos que não gostaram do produto: {menores_18_nao_gostaram}")


