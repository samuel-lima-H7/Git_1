#CÓDIGO DE FUNCIONAMENTO DE CAIXA ELETRONICO

entrada = int(input("Digite o valor no caixa: R$: "))
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
num = list()
divi = 0
sobra = ""

while True:
    for c in range(len(cedulas)):
        if sum(num) == entrada:
            break
        print(f"Entrada {c}: {entrada}")
        if entrada >= cedulas[c]:
            divi = entrada // cedulas[c]
            print(f"Divisão {c}: {divi}")

        num.append(divi*cedulas[c])
        print(f"Lista {c}: {num}")
        entrada -= divi * cedulas[c]


    break

print(num)
print(sum(num))


