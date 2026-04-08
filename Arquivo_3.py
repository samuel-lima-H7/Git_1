#CÓDIGO DE FUNCIONAMENTO DE CAIXA ELETRONICO


cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

entradaorigem = int(input("Digite o valor no caixa: R$: "))
entrada = entradaorigem

num = list()
divi = 0

total = {"Quantidade": list(), "Cédula": list()}

for c in range(len(cedulas)):
    if entrada >= cedulas[c]:
        divi = entrada // cedulas[c]
        num.append(divi*cedulas[c])

        total["Quantidade"].append(divi)
        total["Cédula"].append(cedulas[c])

        entrada -= divi * cedulas[c]
    if sum(num) == entradaorigem:
        break

print(f"Para completar o valor de {entradaorigem} é necessário ter: ")
for i in range(len(num)):
    print(f"{total["Quantidade"][i]} cedulas de {total["Cédula"][i]} reais")


