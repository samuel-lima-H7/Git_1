#CALUCULO DE JUROS COMPOSTOS

#Definição das variáveis
nome = input("Digite o nome de usuário: ")
valor = int(input("Digite o saldo inicial do usuário: "))
taxa = int(input("Digite a taxa de juros: "))
meses = int(input("Digite o numero de meses: "))

#Classe para o calculo dos juros
class Sistema:
    #Definição das instâncias
    def __init__(self, n, v, t, m):
        self.valor = v
        self.nome = n
        self.meses = m
        self.taxa = t
        self.bruto = 0
        self.liquido = 0

    #Calculo do valor bruto
    def valor_bruto(self):
        bruto = self.valor*((1+self.taxa/100)**self.meses) #Calculo de juros compostos(fórmula)
        self.bruto = bruto

    #Calculo do valor liquido
    def valor_liquido(self):
        lucro = self.bruto -  self.valor    #Calculo do lucro(subtraindo o valor atual pelo inicial)
        imposto = lucro * 0.15              #Calculo de imposto(aplicando 15 por cento ao lucro gerado)
        self.liquido = self.bruto - imposto #Calculo do lucro liquido(subtraindo o valor bruto pelo que será descontado automaticamento)

    #Exibição dos valores
    def exibir(self):
        print(f"Usuário: {self.nome}")
        print(f"Montante bruto do valor inicial é de: {self.bruto:.2f}")
        print(f"Valor Liquido final: {self.liquido:.2f}")

#Criação dos objetos
pessoa1 = Sistema(nome, valor, taxa, meses)
pessoa1.valor_bruto()
pessoa1.valor_liquido()
pessoa1.exibir()

