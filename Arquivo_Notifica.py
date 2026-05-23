#ENVIA CRONOGRAMA PARA O EMAIL

from _datetime import datetime
import csv


quant =  int(input("Digite o numero de tarefa que deseja fazer hoje: "))
dia =  input("Digite o dia da semana do qual a tarefa fará parte: ")
lista_tarefa =  list()

def info():
    lista_tarefa.append(dia)
    for c in range(quant):
        dados  = list()
        print("-="*20)
        hora = input("Digite o inicio do compromisso: ")
        compromisso = input("Digite o compromisso: ")
        print("-=" * 20)
        dados.append(hora)
        dados.append(compromisso)
        lista_tarefa.append(dados)

def armazena():
    with open("C:/Users/user/Desktop/Programação/teste programação.csv","w", newline="", encoding="utf-8-sig") as arquivo:
        planilha = csv.writer(arquivo, delimiter=";")
        planilha.writerow(["Dia da Semana","Hora", "Tarefa"])

        for a in lista_tarefa[1:]:
            planilha.writerow([lista_tarefa[0], a[0], a[1]])

def leitura():
    with open("C:/Users/user/Desktop/Programação/teste programação.csv", "r", newline="", encoding="utf-8-sig") as conteudo:
        info_arquivo = csv.reader(conteudo, delimiter=";")
        for coluna, valor in enumerate(info_arquivo):
            if coluna == 0:
                continue
            dia_atual = valor[0]
            print(dia_atual)


info()
armazena()
leitura()