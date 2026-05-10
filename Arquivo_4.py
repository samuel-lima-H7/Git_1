#SISTEMA DE ANALISE DE DADOS PRA DEFINIR STATUS DE FUNCIONAMENTO EM EMPRESA

quant = int(input("Digite a quantidade de veiculos que deseja cadastrar: "))
veiculos = list()



for c in range(quant):
    dados_veiculo = list()
    print("-="*20)
    veiculo = input("Digite o veiculo de registro: ")
    km_rodados = float(input("Digite o numero de quilometros que o veiculo percorreu: "))
    comb_usado = float(input("Digite a quantidade em litros de combustível usado: "))
    temp_gasto = float(input("Digite o tempo em horas de viagem que o veiculo percorreu: "))
    print("-=" * 20)
    dados_veiculo.append(veiculo)
    dados_veiculo.append(km_rodados)
    dados_veiculo.append(comb_usado)
    dados_veiculo.append(temp_gasto)
    veiculos.append(dados_veiculo)

def analise_repeticao():
    repetido = 0
    for r in range(len(veiculos)):
        nome_atual = veiculos[r][0]
        veiculos.pop(r)
        for v in range(len(veiculos)):
            if nome_atual == veiculos[v][0]:
                repetido += 1
                print(nome_atual)
    print(repetido)


def analise_manutencao(val,b):
    if val[b][1] >= 5000.00:
        return "Manutenção Necessária"
    else:
         return "Manutenção Ok"

def analise_eficiencia(val, b):
    km_por_litro = val[b][1] / val[b][2]
    if km_por_litro >= 3.5:
        return "Veiculo Eficiente"
    else:
        return "Veiculo NÃO Eficiente"

'''for a in range(len(veiculos)):
    print("-="*20)
    print(f"O Veiculo {veiculos[a][0]:^20}")
    print(analise_eficiencia(veiculos, a))
    print(analise_manutencao(veiculos, a))
'''

analise_repeticao()












