#CALUCULO DE JUROS COMPOSTOS

nome = input("Digite o nome de usuário: ")
valor = int(input("Digite o saldo inicial do usuário: "))
taxa = int(input("Digite a taxa de juros: "))
meses = int(input("Digite o numero de meses: "))

val_bruto= 0
val_liquido = 0

class Sistema:
    def _init_(self, n, v, t, m, b, l):
        self.valor = v
        self.nome = n
        self.meses = m
        self.taxa = t
        self.bruto = b
        self.liquido = l

    def juros_compostos(self):
        bruto = self.valor*((1+self.taxa)**self.meses)
        self.bruto = bruto


pessoa1 = Sistema(nome, valor, taxa, meses, val_bruto, val_liquido)

