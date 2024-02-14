#Ex 1#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
listaLinhas = arquivo.readlines()

print(f"O arquivo possui {len(listaLinhas)} linhas")

#Ex 2#

nomeArquivo = str(input("Digite o nome do arquivo: ")) + ".txt"
arquivo = open(nomeArquivo,"r")
texto = arquivo.read()

qtVogais = 0

for char in texto:
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        qtVogais = qtVogais + 1

print(f"O arquivo possui {qtVogais} vogais")

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

#Ex 4#

