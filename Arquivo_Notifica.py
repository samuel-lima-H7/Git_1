#ENVIA CRONOGRAMA PARA O EMAIL

import csv
import os

quant =  int(input("Digite o numero de tarefa que deseja fazer hoje: "))
lista_tarefa =  list()

for c in range(quant):
    dados  = list()
    print("-="*20)
    hora = input("Digite o inicio do compromisso: ")
    compromisso = input("Digite o compromisso: ")
    print("-=" * 20)
    dados.append(hora)
    dados.append(compromisso)

    lista_tarefa.append(dados)

with open("C:/Users/user/Desktop/Programação/teste programação.csv","w", newline="", encoding="utf-8-sig") as arquivo:
    planilha = csv.writer(arquivo, delimiter=";")
    planilha.writerow(["hora", "tarefa"])

    for c in lista_tarefa:
        planilha.writerow([c[0], c[1]])


