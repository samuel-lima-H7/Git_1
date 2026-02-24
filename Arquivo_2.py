#CODIGO QUE TRADUZ PARA UMA LINGUA INVENTADA

#RECEBE UMA STR
palavra = input(str("Digite um palavra: "))

#VARIÁVEIS QUE SERÃO USADAS
palavra_str = ""
palavra_traduzida = []

#SISTEMAS DE SUBSTITUIÇÃO DE LETRAS
alfabeto = {"A": "S",
"B": "N",
"C": "V",
"D": "F",
"E": "R",
"F": "G",
"G": "H",
"H": "J",
"I": "O",
"J": "K",
"K": "L",
"L": "K",
"M": "N",
"N": "M",
"O": "P",
"P": "O",
"Q": "W",
"R": "T",
"S": "D",
"T": "Y",
"U": "I",
"V": "B",
"W": "E",
"X": "C",
"Y": "U",
"Z": "X",
"Ç": "C"
}

#LAÇO QUE REPETE O PROCESSO DE SUBSTITUIÇÃO PARA CARA LETRA
for c in range(len(palavra)):
    #ARMAZENAMENTO DA LETRA ATUAL
    letra_atual = str(palavra[c].upper())
    #VERIFICAÇÃO DE PRESENÇA DE CARACTERE
    if letra_atual in alfabeto:
        #ARMAZENAMENTO DA PALAVRA TRADUZIDA
        palavra_traduzida.append(alfabeto[letra_atual])

#PASSANDO PARA STR
palavra_str = "".join(palavra_traduzida)

#PRINT DA PALAVRA
print(palavra_str)