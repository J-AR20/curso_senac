# Declaração dos Vetores e Variáveis
sexo=[]
idade=[]
resposta=[]
resp="S"
total=0
qtdsim=0
qtdnao=0
qtd18sim = 0

# Início da Estrutura para Armazenar os Dados nos Vetores
while resp == "S" or resp == "s":
    # Início do Tratamento de Erro - Variável Sexo
    while True:
        s = input("Informe o Sexo (M ou F) do Entrevistado: ")
        if s == "M" or s == "F":
            sexo.append(s)
            break
    # Fim do Tratamento de Erro - Variável Sexo
        
    idade.append(int(input("Informe a Idade do Entrevistado: ")))
    resposta.append(input("Informe se o Entrevistado Gostou ou Não do Produto (S ou N): "))
    resp = input("Deseja Continuar o Cadastro (S ou N)? ")
    total = total + 1 # Total de Pessoas
# Fim da Estrutura para Armazenar os Dados nos Vetores
    
# Início da Estrutura para Coletar os Dados nos Vetores   
for i in range(len(sexo)):
    if resposta[i]  == "S" or resposta[i]  == "s": 
        qtdsim = qtdsim + 1 # Total de Pessoas que Responderam Sim
    else: 
        qtdnao = qtdnao + 1 # Total de Pessoas que Responderam Não

    if idade[i] >= 18 and (resposta[i]  == "S" or resposta[i]  == "s"):
        qtd18sim = qtd18sim + 1 # Total de Pessoas > 18 que Responderam Sim
# Fim da Estrutura para Coletar os Dados nos Vetores 
        
# Apresentação dos Dados Solicitados
print(f"A quantidade de participantes foi: {total}")
print(f"A quantidade de participantes que responderam Sim foi: {qtdsim}")
print(f"A quantidade de participantes que responderam Não foi: {qtdnao}")
print(f"A quantidade de participantes maiores que 18 anos e que responderam Sim foi {qtd18sim}")