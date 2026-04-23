#CONTA DE BANCO

nome = input("Digite seu nome: ")
saldo = input("Digite seu saldo atual: ")

class Banco:
    def __init__(self, n, s):
        self.nome = n
        self.saldo = s


pessoa1 = Banco(nome, saldo)
print( pessoa1.nome)
print(pessoa1.saldo)