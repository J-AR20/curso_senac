# E se ao invés de escrever sempre uma soma à mão criar uma função soma para fazer isso:

# n1 = int(input("Informe um valor: "))
# n2 = int(input("Informe outro valor: "))
# soma = n1 + n2

# Isso se faz com a fç def()

def somar(x, y):
    result = x + y
    print(f"O resultado foi {result}.")

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
somar(n1, n2)
