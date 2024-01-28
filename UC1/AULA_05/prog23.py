# Vamos falar de tratamentos de erro:
# Usuário fornece 2 valores inteiros, calcule a divisão e apresenta o resultado

# n1 = int(input("Informe um valor: "))
# n2 = int(input("Informe outro valor: "))
# div = n1 / n2
# print(f"A divisão dos números é {div}")

# Funciona, no entanto, vai dar erro se nesse programa colocar um zero em qualquer um dos valores.
# Como, então, tratar dele?
# Pode-se dividir zero por algo, (0/n2), mas não se pode dividir algo por zero (n1/0)
# Logo, só precisaríamos, strictu sensu, tratar de erros no n2:


while True:
    try:
        n1 = int(input("Informe um valor: "))
        n2 = int(input("Informe outro valor: "))
        div = n1 / n2
    except ZeroDivisionError:
        print("O segundo valor não pode ser Zero.")
    except ValueError:
        print("Não se pode utilizar strings para fazer divisões.")
    else:
        print(f"A divisão dos números é {div:.2f}")
        break