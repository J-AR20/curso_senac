# Exercicio: Um usuario fornece 10 números e no final devo dizer qual o recebe o maior numero fornecido

recebe = 0
for x in range(10):
    x = int(input("Me diga um número: "))
    if x > recebe:
        recebe = x  
print(f"O maior número digitado é: {recebe:.2f}")

# a grande questão aqui é que não estamos atualizando o valor de recebe nunca
# estamos apenas armazenando quando dizemos: 'recebe = x'
# o for (o loop) estará guardando dentro dele todos os números




# Explicação do ChatGPT:
# recebe = 0: Aqui você está inicializando a variável recebe com o valor zero. 
# Essa variável será usada para armazenar o maior número fornecido pelo usuário.

# for x in range(10):: Este é um loop for que executa 10 vezes. 
# A cada iteração, o loop solicita ao usuário que forneça um número.

# x = int(input("Me diga um número: ")): Dentro do loop, você está usando a variável x para armazenar 
# o número fornecido pelo usuário. O input é utilizado para obter a entrada do usuário, 
# e int é usado para converter essa entrada em um número inteiro.

# if x > recebe:: Aqui, você está comparando o número fornecido (x) 
# com o valor atual armazenado em recebe. Se x for maior que o valor atual em recebe, 
# então recebe é atualizado para o valor de x.

# print(f"O resultado da soma é: {recebe:.2f}"): 
# No final do loop, o programa imprime o maior número fornecido pelo usuário. 
# A formatação :.2f é usada para garantir que o número seja exibido com duas casas decimais, 
# embora nesse caso, como são números inteiros, isso não terá efeito prático.