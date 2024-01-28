# Duas funçoes não encapsuladas:

# def somar(n1,n2):
#     result1 = n1 + n2
#     print(f"A soma dos dois valores é {result1}")
# def subtracao(n1,n2):
#     result2 = n1 - n2
#     print(f"A subtracao do primeiro valor pelo segundo é {result2}")

# n1 = int(input("Informe o primeiro valor: "))
# n2 = int(input("Informe o segundo valor: "))
# somar(n1,n2)
# subtracao(n1,n2)


# Como funciona o encapsulamento de funções:

def calcular(x,y):
    def somar(num):
        return x + y
    def subtracao(num):
        return x - y
    result1 = somar(x+y)
    result2 = subtracao(x-y)
    print(f"A soma dos dois valores é {result1}")
    print(f"A subtracao do primeiro valor pelo segundo é {result2}")

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
calcular(n1,n2)

