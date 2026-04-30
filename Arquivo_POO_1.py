#CALUCULO DE JUROS COMPOSTOS

nome = input("Digite o nome de usuário: ")
valor = int(input("Digite o saldo inicial do usuário: "))
taxa = int(input("Digite a taxa de juros: "))
meses = int(input("Digite o numero de meses: "))


class Sistema:
    def __init__(self, n, v, t, m):
        self.valor = v
        self.nome = n
        self.meses = m
        self.taxa = t
        self.bruto = 0
        self.liquido = 0

    def valor_bruto(self):
        bruto = self.valor*((1+self.taxa/100)**self.meses)
        self.bruto = bruto

    def valor_liquido(self):
        lucro = self.bruto -  self.valor
        imposto = lucro * 0.15
        self.liquido = self.bruto - imposto

    def exibir(self):
        print(f"Usuário: {self.nome}")
        print(f"Montante bruto do valor inicial é de: {self.bruto}")
        print(f"Valor Liquido final: {self.liquido}")

pessoa1 = Sistema(nome, valor, taxa, meses)
pessoa1.valor_bruto()
pessoa1.valor_liquido()
pessoa1.exibir()

