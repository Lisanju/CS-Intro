#Ex 1#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
listaLinhas = arquivo.readlines()

print(f"O arquivo possui {len(listaLinhas)} linhas")

arquivo.close()

#Ex 2#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
texto = arquivo.read()

qtVogais = 0

for char in texto:
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        qtVogais = qtVogais + 1

print(f"O arquivo possui {qtVogais} vogais")

arquivo.close()

#Ex 3#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
texto = arquivo.read()

vogais = ["a","e","i","o","u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

qtVogais = 0
qtConsoantes = 0

for char in texto:
    for v in vogais:
        if (char == v):
            qtVogais = qtVogais + 1

    for c in consoantes:
        if (char == c):
            qtConsoantes = qtConsoantes + 1

print(f"O arquivo possui {qtVogais} vogais e {qtConsoantes} consoantes")

arquivo.close()

#Ex 4#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
texto = arquivo.read()

inputChar = str(input("Digite um caracter: "))
qtInputChar = 0

for char in texto:
    if (char == inputChar):
        qtInputChar = qtInputChar + 1

print(f"A quantidade de [{inputChar}] no texto é {qtInputChar}")

arquivo.close()

#Ex 5#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
texto = arquivo.read()

listaChar = []
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for char in texto:
    listaChar.append(char)

print("== Quantidade de vezes em que cada caractere aparece no texto ==\n")

for letra in alfabeto:
    print(f"{letra}: {listaChar.count(letra)}")

arquivo.close()

#Ex 6#



#Ex 7#

nomeAO = str(input("Digite o nome de um arquivo já existente: ")) + ".txt"
AO = open(nomeAO,"r")
textoAO = AO.read()
AO.close()

nomeAN = str(input("Digite o nome de um novo arquivo para criar: ")) + ".txt"
AN = open(nomeAN,"w")
AN.write(textoAO.upper())
AN.close()

#Ex 8#

nomeAR1 = str(input("1 - Digite o nome de um arquivo já existente: ")) + ".txt"
AR1 = open(nomeAR1,"r")
textoAR1 = AR1.read()
AR1.close()

nomeAR2 = str(input("2 - Digite o nome de outro arquivo já existente: ")) + ".txt"
AR2 = open(nomeAR2,"r")
textoAR2 = AR2.read()
AR2.close()

nomeAC = str(input("3 - Digite o nome de um novo arquivo para criar: ")) + ".txt"
AC = open(nomeAC,"w")
textoAC = AC.write(textoAR1 + textoAR2)
AC.close()

#Ex 9#

