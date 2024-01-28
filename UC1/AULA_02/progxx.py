# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas
# 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
# - Ter entre 16 e 69 anos.
# - Pesar mais de 50 kg.
# - Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

idade = int(input("Qual a sua idade: "))
peso = float(input("Quanto você pesa: "))
sono = float(input("Quanto dormiu nas últimas 24h: "))
if idade < 16 or idade > 69 or peso <= 50 or sono < 6:
    print("Você não está apto a doar sangue.")
else:
    print("Você está apto doar sangue.")