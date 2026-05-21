#ENVIA CRONOGRAMA PARA O EMAIL
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

for i in range(len(lista_tarefa)):
    print("-=" * 20)
    print(f"horario: {lista_tarefa[i][0]}")
    print(f"tarefa: {lista_tarefa[i][1]}")
    print("-=" * 20)
