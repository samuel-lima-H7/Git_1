#CONTA DE BANCO

nome = input("Digite seu nome: ")
saldo = int(input("Digite seu saldo atual: "))
am = int(input("Digite o valor que queres depositar: "))



class Banco:
    def __init__(self, n, s):
        self.nome = n
        self.saldo = s
    def depositar(self, saldo1):
        self.saldo += saldo1
    def exibir(self):
        print(f"o nome do usuuário é {self.nome}")
        print(f"O saldo é igual a: {self.saldo}")



pessoa1 = Banco(nome, saldo)
pessoa1.depositar(am)
pessoa1.exibir()
