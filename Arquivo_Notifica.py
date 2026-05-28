#ENVIA CRONOGRAMA PARA O EMAIL

from _datetime import datetime
import locale
import csv

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
data = datetime.now()
hoje = data.strftime("%A")
data_atual = hoje[0:hoje.find("-")]
dados = list()
lista_tarefa =  list()

def info(parametro):
    lista_tarefa.append(parametro)
    for c in range(quant):
        dados1  = list()
        print("-="*20)
        hora = input("Digite o inicio do compromisso: ")
        compromisso = input("Digite o compromisso: ")
        print("-=" * 20)
        dados1.append(hora)
        dados1.append(compromisso)
        lista_tarefa.append(dados)
def armazena():
    with open("C:/Users/user/Desktop/Programação/teste programação.csv","a", newline="", encoding="utf-8-sig") as arquivo:
        planilha = csv.writer(arquivo, delimiter=";")
        for a in lista_tarefa[1:]:
            planilha.writerow([lista_tarefa[0], a[0], a[1]])
def leitura():
    tarefas_hora = list()
    with open("C:/Users/user/Desktop/Programação/teste programação.csv", "r", newline="", encoding="utf-8-sig") as conteudo:
        info_arquivo = csv.reader(conteudo, delimiter=";")
        for linha, valor in enumerate(info_arquivo):
            tarefas_hora = list()
            if linha == 0:
                continue
            dia_inserido = str(valor[0].lower().strip())
            if dia_inserido == data_atual:
                tarefas_hora.append(valor[1])
                tarefas_hora.append(valor[2])
                dados.append(tarefas_hora)

entrada_de_dados = str(input("deseja inserir alguma informação no arquivo")).lower().split( )
if entrada_de_dados[0] == "s":
    quant =  int(input("Digite o numero de tarefa que deseja fazer hoje: "))
    dia =  input("Digite o dia da semana do qual a tarefa fará parte: ")
    info(dia)
    armazena()

leitura()
print(dados)

for i in range(len(dados)):
    print(f"Hoje é {hoje}, e às {dados[i][0]} você tem as seguintes tarefas: {dados[i][1]}.")
