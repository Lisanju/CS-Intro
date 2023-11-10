#Ex 1#

c = 1
while(c<=5):
    mult = 3*c
    c = c+1
    print(mult)

print("Fim do programa")

#Ex 2#

c = 1
while(c<=100):
    print(c)
    c = c +1

print("Fim do programa while")

n = 100
c = 1
for c in range(1,n+1):
    print(c)

print("Fim do programa for")

#Ex 3#

c = 10
while(c>=0):
    print(c)
    c = c-1

print("FIM!")

#Ex 4#

inicial = 0
final = 100000
contagem = 1000
for n in range(inicial,final+1000,contagem):
    print(n)

print("Fim do programa")

#Ex 5#

c = 1
soma = 0
while(c<=10):
    n = int(input("Digite um valor: "))
    soma = soma+n
    c = c+1
    
print(soma)
print("Fim do programa")

#Ex 6#

c = 0
soma = 0
while(c<10):
    n = int(input("Digite um valor: "))
    soma = soma+n
    c = c+1

media = soma/10
print("A média da soma dos números fornecidos é: ",media)

#Ex 7#

c = 0
soma = 0
while(c<10):
    n = int(input("Digite um valor: "))
    if(n>0):
        soma = soma+n
        c = c+1
    else:
        print("Insira apenas valores positivos.")

media = soma/10
print("A média da soma dos números fornecidos é: ",media)

#Ex 8#

n = int(input("Digite N: "))
salva_maior = n
salva_menor = n

for i in range(1,10):
    n = int(input("Digite N: "))

    if(n>salva_maior):
        salva_maior = n

    elif(n<salva_menor):
        salva_menor = n

print(f"O menor número é {salva_menor} e o maior número é {salva_maior}")

#Ex 9#

n = int(input("Digite N: "))

for i in range(1,n+1,2):
    print(i)

print("Fim do programa")

#Ex 10#

soma = 0
for i in range(0,50+1,2):
    soma = soma+i

print("O resultado da soma dos 50 números pares é: ",soma)

#Ex 11#

