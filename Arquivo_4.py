#SISTEMA DE ANALISE DE DADOS PRA DEFINIR STATUS DE FUNCIOANAMENTO EM EMPRESA

quant = int(input("Digite a quantidade de veiculos que deseja cadastrar: "))
veiculos = list()
Dados_veiculo = list()

for c in range(quant):
    Veiculo = input("Digite o veiculo de registro: ")
    KM_rodados = float(input("Digite o numero de quilometros que o veiculo percorreu: "))
    Comb_usado = float(input("Digite a quantidade em litros de combustível usado: "))
    Temp_gasto = float(input("Digite o tempo em horas de viagem que o veiculo percorreu: "))
    Dados_veiculo.append(Veiculo)
    Dados_veiculo.append(KM_rodados)
    Dados_veiculo.append(Comb_usado)
    Dados_veiculo.append(Temp_gasto)
    veiculos.append(Dados_veiculo)
    Dados_veiculo.clear()

