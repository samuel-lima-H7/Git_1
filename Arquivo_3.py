#CÓDIGO DE FUNCIONAMENTO DE CAIXA ELETRONICO

entrada = int(input("Digite o valor no caixa: R$: "))
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
divi = 0
sobra = ""

while True:
    for c in range(len(cedulas)):
        entrada = ( entrada - divi * cedulas[c])
        if entrada < cedulas[c]:
            divi = entrada // cedulas[c]





