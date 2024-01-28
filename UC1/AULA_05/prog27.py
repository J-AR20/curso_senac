
def comb(e,g):
    result = e/g
    if result <= 0.70:
        print("O etanol é mais vantajoso.")
    else:
        print("A gasolina é mais vantajosa.")
while True:
    try:
        e = float(input("Informe um valor: "))
        g = float(input("Informe outro valor: "))
    except ValueError:
        print("Verifique o valor fornecido")
    else:
        try:
            comb(e,g)
        except ZeroDivisionError:
            print("verifique o valor da gasolina.")
        else:
            break