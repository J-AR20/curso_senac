# Faça um programa que pergunte a uma pessoa a sua idade, o seu peso e quanto dormiu nas últimas 24h
# Deverá dizer se ela pode ou não doar sangue a partir das seguintes condições:
# - Ter entre 16 e 69 anos;
# - Pesar mais de 50 kg;
# - Estar descansado (ter dormido pelo menos 6 horas nas ultimas 24 horas)

# Solução possível...
# O problema dessa solução é que ele é muito grande por conta das redundâncias
# O programa roda perfeitamente, mas é grande e confuso.
# A solução, portanto, foi a que eu fiz, colocar todas as condições em apenas uma linha.

idade = int(input("Qual a sua idade: "))
peso = float(input("Quanto você pesa: "))
sono = int(input("Quanto dormiu nas últimas 24h: "))
if idade >= 16 and idade <= 69:
    if peso > 50:
        if sono >= 6:
            print("Apto a doar")
        else:
            print("Não está apto para doar")
    else:
        print("Não está apto para doar")
else:
    print("Não está apto para doar")


# Solução ideal do professor:

idade = int(input("Qual a sua idade: "))
peso = float(input("Quanto você pesa: "))
sono = int(input("Quanto dormiu nas últimas 24h: "))
if (idade >= 16 and idade <= 69) and peso > 50 and sono >= 6: # não precisa dos parenteses na 1ª condição. É para faciliar a visualização.
#  '16 <= idade <= 69' é outra forma de notar um valor entre uma determinada faixa
    print("Você está apto")
else:
    print("Você não está apto")
