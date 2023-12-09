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

