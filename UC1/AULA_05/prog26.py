# Verificar num posto se é mais vantajoso abastecer com etanol ou gasolina
# Precisamos informar quanto custa etanol e o custo da gasolina
# Dividir etanol pela gasolina e se etanol for <= 0.70 será mais vantajoso que a gasolina

def comb(e,g):
    result = e/g
    if result <= 0.70:
        print("O etanol é mais vantajoso.")
    else:
        print("A gasolina é mais vantajosa")

e = float(input("Informe o valor do etanol: "))
g = float(input("Informe o valor da gasolina: "))

comb(e,g)
