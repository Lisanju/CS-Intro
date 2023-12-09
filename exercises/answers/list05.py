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

str_mai = input("Digite uma palavra em maiúsculo: ")
str_min = ""

for indice in range(len(str_mai)):
    conv = ord(str_mai[indice])
    conv = conv + 32
    str_min = str_min + chr(conv)
    
print(str_min)

#Ex 8#

