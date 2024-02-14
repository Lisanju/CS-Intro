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


