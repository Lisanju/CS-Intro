#Ex 1#

str = input("Insira um texto: ")
print(str)

#Ex 2#

print(len(str))

#Ex 3#

nome = input("Insira um nome: ")
print(nome[:4])

#Ex 4#

nome = input("Insira um nome: ")

if (nome[0] == "a" or nome[0] == "A"):
  print(nome)

else:
  print("O nome não começa com 'a'")

#Ex 5#

str = input("Insira uma palavra: ")
str_nova = ""

for indice in range(len(str)):
    conv = ord(str[indice])
    conv = conv + 1
    str_nova = str_nova + chr(conv)
    
print("Resultado: ", str_nova)

#Ex 6#

str1 = input("Insira uma palavra: ")
str2 = input("Insira outra palavra: ")

if (str1 < str2):
    print("A palavra ", str1, " vem antes de ", str2, " na ordem alfabética")
    
else:
    print("A palavra ", str2, " vem antes de ", str1, " na ordem alfabética")

#Ex 7#

str1 = input("Digite uma palavra: ")
str2 = input("Digite outra palavra: ")
s = ""

if str1 in str2:
    print(f"A sequência {str1} está contida em {str2}")
    
else:
    print(f"A sequência {str1} não está contida em {str2}")

#Ex 8#

str = input("Digite uma palavra iniciada em letra maiúscula: ")

conv = ord(str[0]) + 32
str_conv = chr(conv) + str[1:len(str)]

print(str_conv)

#Ex 9#

str_min = input("Digite uma palavra em minúsculo: ")
str_mai = ""

for indice in range(len(str_min)):
    conv = ord(str_min[indice])
    conv = conv - 32
    str_mai = str_mai + chr(conv)
    
print(str_mai)

#Ex 10#

str1 = input("Digite uma palavra: ")
str2 = input("Digite outra palavra: ")

if (str1 < str2):
  print(f"{str1} vem antes de {str2}")

else:
  print(f"{str2} vem antes de {str1}")

#Ex 11#

str1 = input("Digite uma palavra: ")
str2 = input("Digite outra palavra: ")

if (str1 < str2):
  print(f"{str1} vem antes de {str2}")

else:
  print(f"{str2} vem antes de {str1}")

#Ex 12#

nome = input("Insira um nome: ")
sexo = input("Insira um sexo: ")
idade = int(input("Insira uma idade: "))

nome_conv = nome[0].upper() + nome[1:len(nome)]

if (sexo.lower() == "feminino" and idade < 25):
    print(f"{nome_conv}: Aceita.")
    
else:
    print(f"{nome_conv}: Não aceita.")

#Ex 13#

str = "01010011"
c = 0

for char in str:
    
    if (char == "1"):
        c = c + 1
        
print(f"A quantidade de 1's é igual a {c}")


#Ex 14#

str = input("Digite uma palavra: ")
x = input("Digite uma letra que faça parte da palavra escolhida: ")
y = input("Digite uma outra letra do alfabeto: ")
str_conv = ""

for indice in range(len(str)):
    
    if (str[indice] == x):
        str_conv = str_conv + y 
        
    else:
        str_conv = str_conv + str[indice]
    
print(str_conv)

#Ex 15#

str = input("Digite uma palavra: ")
print(str[::-1])

#Ex 16#

str = input("Insira uma palavra: ")
str_conv = ""

for indice in range(len(str)):

  if (str[indice] == "a" or str[indice] == "e" or str[indice] == "i" or str[indice] == "o" or str[indice] == "u"):
      str_conv = str_conv + ""
      
  else:
      str_conv = str_conv + str[indice]
      
print(str_conv)

#Ex 17#

str = input("Insira uma palavra: ")
letra_nova = input("Insira uma letra: ")
str_conv = ""
c = 0

for i in range(len(str)):
    
    if (str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u"):
        c = c + 1
        str_conv = str_conv + letra_nova
        
    else:
        str_conv = str_conv + str[i]

print(f"A palavra inserida possui {c} vogais")
print(str_conv)

#Ex 18#

str = input("Digite uma frase: ")
c = 0

for i in range(len(str)):
    
    if (str[i] == " "):
        c = c + 1
        
print(f"Há {c} espaços em branco na frase.")

#Ex 19#

str = input("Digite uma frase: ")
str_conv = ""

for i in range(len(str)):
    
    if (str[i] == " "):
        str_conv = str_conv + ""
        
    else:
        str_conv = str_conv + str[i]
        
print(str_conv)

#Ex 20#

idades = []
nomes = []
botao = True
maisNovo = float("inf")
nomeMaisNovo = ""
maisVelho = 0
nomeMaisVelho = ""

while(botao):
    idade = int(input("Digite uma idade: "))
    
    if (idade > 0):
        idades.append(idade)
        nome = input("Digite um primeiro nome: ")
        nomes.append(nome)
        
    else:
        botao = False
        break
    
for i in range(0,len(idades)):
    if (idades[i] > maisVelho):
        maisVelho = idades[i]
        nomeMaisVelho = nomes[i]
        
    elif (idades[i] < maisNovo):
        maisNovo = idades[i]
        nomeMaisNovo = nomes[i]
        
print(f"Mais velho\nNome: {nomeMaisVelho} - Idade: {maisVelho}\n\nMais novo\nNome: {nomeMaisNovo} - Idade: {maisNovo}")

#Ex 21#

carros = []
consumo = []
consumo1000km = []
N = 5
consumoMaisEconomico = float('inf')
carroMaisEconomico = ""

for n in range(0,N):
    addCarro = input("Digite o nome de um carro: ")
    addConsumo = int(input("Digite o consumo em quilômetros desse carro com 1 litro de combustível: "))
    carros.append(addCarro)
    consumo.append(addConsumo)
    
for i in range(0,N):
    consumo1000km.append(consumo[i]*1000)
    if (consumo[i] < consumoMaisEconomico):
        consumoMaisEconomico = consumo[i]
        carroMaisEconomico = carros[i]

print(f"Carro mais econômico: {carroMaisEconomico} - Consumo: {consumoMaisEconomico}\n\nCarros: {carros}\nConsumo em 1000km: {consumo1000km}")

#Ex 22#

nome = input("Digite o nome de uma mercadoria: ")
valor = float(input("Digite o valor dessa mercadoria: "))

desconto = valor*10/100

valorVista = valor - desconto

print(f"Mercadoria: {nome}\nValor total: {valor}\nValor do desconto: {desconto}\nValor à vista: {valorVista}")

#Ex 23#

S = input("Digite um texto: ")
botao = True

while(botao):
    I = int(input("Digite um número inteiro não-negativo"))
    J = int(input("Digite outro número inteiro não-negativo"))
    
    if (I <  0 and  J < 0):
        print("Os números digitados são negativos! Digite-os novamente!")
        
    elif (I < 0 and J > 0):
        print("O primeiro número digitado é negativo! Digite-o novamente!")
        
    elif (I > 0 and J < 0):
        print("O segundo número digitado é negativo! Digite-o novamente!")
        
    else:
        botao = False

print(S[I:J])

#Ex 24#

S = input("Digite um texto: ")
C = input("Digite um caractere: ")
I = int(input("Digite uma posição: "))
caracteres = []
posicao = []

for i in range(I,len(S)):
    if (S[i] == C):
        posicao.append(i)
        break

print(f"Posição: {posicao}")

#Ex 25#

string = input("Digite um texto: ")
nova_string = ""

for i in range(0,len(string)):
    nova_string = nova_string + chr(ord(string[i]) + 3)
    
print(nova_string)

#Ex 26#

string = input("Digite uma palavra: ")
stringComparada = ""

for i in range(0,len(string)):
    if (string[i] == string[len(string)-1-i]):
        stringComparada = stringComparada + string[len(string)-1-i]
        
if (stringComparada == string):
    print(string + " é um palíndromo.")
    
else:
    print(string + " não é um palíndromo.")

#Ex 27#

str1 = input("Digite um texto: ")
str2 = input("Digite outro texto: ")
N = int(input("Digite um número inteiro positivo: "))

for i in range(0,N):
    str1 = str1 + str2[i]
    
str1 = str1 + "\0"
print(str1)

#Ex 28#

A = input("Digite uma palavra ou um texto: ")
B = input("Digite outra palavra ou outro texto: ")

c = B.count(A)
print(c)

# ou #

A = input("Digite uma palavra ou um texto: ")
B = input("Digite outra palavra ou outro texto: ")
posicao = 0
ocorrencia = 0

while (posicao <= len(B) - len(A)):
    if (B[posicao:posicao + len(A)] == A):
        ocorrencia = ocorrencia + 1
        posicao = posicao + len(A)
        
    else:
        posicao = posicao + 1
        
print(ocorrencia)

#Ex 29#

opcoesRodando = True

while(opcoesRodando):
    print("[Menu de opções]\n(a) - Ler uma string S1 (tamanho máximo de 20 caracteres);\n(b) - Imprimir o tamanho da string S1;\n(c) - Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da comparação;\n(d) - Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação'\n(e) - Imprimir a string S1 de forma reversa;\n(f) - Contar quntas vezes um dado caractere aparece na string S1. Esse caractere deve ser informado pelo usuário;\n(g) - Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serão lidos pelo usuário;\n(h) - Verificar se uma string S2 é substring de S1. A string S2 deve ser informada pelo usuário;\n(i) - Retornar uma substring da string S1. Para isso o usuário deve informar a partir de qual posição deve ser criada a substring e qual é o tamanho da substring.\n")
    opcao = input("Selecione uma das opções acima.")
    botao = True

    if (opcao == "a"):
        while(botao):
            S1 = input("Insira um texto de até 20 caracteres: ")
            if (len(S1) > 20):
                print("Foram inseridos mais de 20 caracteres.")
        
            else:
                botao = False
            
    if (opcao == "b"):
        print(S1)
            
    if (opcao == "c"):
        S2 = input("Digite um novo texto: ")
        
        if (S1 < S2):
            print(S1 + " vem antes de " + S2)
            
        else:
            print(S2 + " vem antes de " + S1)
            
    if (opcao == "d"):
        S2 = input("Digite um novo texto: ")
        print(S1 + S2)
        
    if (opcao == "e"):
        S1Rev = S1[::-1]
        print(S1Rev)
        
    if (opcao == "f"):
        C = input("Digite um caractere: ")
        print(S1.count(C))
        
    if (opcao == "g"):
        S1Conv = S1
        C1 = input("Digite um caractere: ")
        C2 = input("Digite outro caractere: ")
        
        for i in range(0,len(S1Conv)):
            if (S1Conv[i] == C1):
                print(S1Conv.replace(S1Conv[i],C2))
                break
        
    if (opcao == "h"):
        S2 = input("Digite um texto: ")
        
        if (S2 in S1):
            print(S2 + " é substring de " + S1)
            
    if (opcao == "i"):
        subS = ""
        p = int(input("Digite uma posição: "))
        t = int(input("Digite um tamanho de substring: "))
        
        while (len(subS) <= t):
            subS = subS + S1[p:]
            
        print(subS)
