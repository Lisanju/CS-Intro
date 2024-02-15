# 1 - Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o número de vezes que aquela palavra aparece no arquivo. #

nomeA = str(input("Digite o nome do arquivo de texto sem a extensão dele (.txt): ")) + ".txt"
arquivo = open(nomeA,"r")
textoA = arquivo.read()
palavra = str(input("Digite uma palavra para buscar no arquivo: "))
ocorrencias = textoA.count(palavra)

print(f"No arquivo a palavra {palavra} ocorre {ocorrencias} vezes.")

arquivo.close()

# 2 - Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por "*". #

nomeAO = str(input("Digite o nome de um arquivo texto existente (não é necessário escrever sua extensão): ")) + ".txt"
nomeAN = str(input("Digite o nome de um novo arquivo texto (não é necessário escrever sua extensão): ")) + ".txt"

AO = open(nomeAO,"r")
AN = open(nomeAN,"w")

textoAO = AO.read()

for char in textoAO:
    if (char == "a" or char == "i" or char == "u" or char == "e" or char == "o"):
        AN.write("*")

    else:
        AN.write(char)

AO.close()
AN.close()

AN = open(nomeAN,"r")
textoAN = AN.read()

print(textoAN)

# 3 - Escreva um programa que leia um número inteiro positivo n e em seguida imprina n linhas do chamado Triangulo de Floyd.
# Para n = 6, temos:
#    1
#    2 3
#    4 5 6
#    7 8 9 10
#    11 12 13 14 15     
#    16 17 18 19 20 21

def trianguloFloyd(n):

    valor = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(valor,end=" ")
            valor = valor + 1
        print()

trianguloFloyd(6)

# 4 - Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... #

def fibonacciR(n):
    if (n == 1 or n == 2):
        return n - 1

    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

print(fibonacciR(5))

# 5 - Faça um programa que calcule e escreva o valor de S: 
#      S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50

def sequencia(n):
    a = 1
    b = 1

    if (n == 1):
        print("1/1")
        return a/b

    else:
        for i in range(2,n+1):
            a = a + 2
            b = b + 1

        print(f"{a}/{b}")
        return a/b

print(sequencia(50))
