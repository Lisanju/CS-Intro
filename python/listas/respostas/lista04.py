#Vetores#

#Ex 1#

N = 6
a = []

for i in range(1,N+1):
    x = input("Atribua os valores: ")
    a.append(x)
    
var = a[0] + a[1] + a[5]
print(f"A soma entre os valores das posições a[0], a[1] e a[5] é: {var}")

a[4] = 100

print(f"{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n{a[4]}\n{a[5]}")

#Ex 2#

N = 6
valores = []

for i in range(0,N):
  add = int(input("Digite um valor: "))
  valores.append(add)

print(valores)

#Ex 3#

N = 10
reais = []
reais_quadrado = []

for i in range(0,N):
    x = float(input("Digite um número real: "))
    reais.append(x)
    
for i in reais:
    reais_quadrado.append(i**2)
    
print(reais)
print(reais_quadrado)

#Ex 4#

N = 6
vetor = []

for i in range(0,N):
    x = int(input("Insira um valor: "))
    vetor.append(x)
    
x = vetor[2]
y = vetor[5]

print(x+y)

#Ex 5#

N = 10
c = 0
vetor = []
vetor_par = []

for i in range(0,N):
    x = int(input("Insira um valor: "))
    vetor.append(x)
    
for elemento in vetor:
    if (elemento % 2 == 0):
        vetor_par.append(elemento)
        c = c + 1
    
print(vetor_par)
print(f"O vetor possui {c} números pares.")

#Ex 6#

N = 10
vetor = [int(input("Insira um valor: ")) for i in range(0,N)]

maior = vetor[0]
menor = vetor[0]

for e in vetor:
    if (e > maior):
        maior = e
        
    elif (e < menor):
        menor = e

print(f"Maior: {maior}\nMenor: {menor}")

#Ex 7#

vetor = [int(input("Insira um valor: ")) for i in range(0,10)]

maior = vetor[0]

for i in range(len(vetor)):
    if (vetor[i] > maior):
        maior = vetor[i]
        pos = i

print(f"Vetor: {vetor}\nMaior: {maior}\nPosição: {pos}")

#Ex 8#

vetor = [int(input("Insira um valor: ")) for i in range(0,6)]
print(vetor[::-1])

#Ex 9#

vetor = []

for i in range(0,6):
    while True:
        x = int(input(f"Insira o {i +1} número par: "))
    
        if (x % 2 == 0):
            vetor.append(x)
            break
            
        else:
            print("O número inserido não é par.")
        
print(vetor[::-1])

#Ex 10#

N = 15
vetor = []

for i in range(0,N):
    nota = float(input("Nota: "))
    vetor.append(nota)
    
media = 0

for n in vetor:
    media = media + n
    media = media / N
    
print(f"Média geral: {media}")

#Ex 11#

vetor = []
vetorNegativo = []
vetorPositivo = []
N = 10
soma = 0

for n in range(0,N):
    numero = float(input("Digite um número real: "))
    vetor.append(numero)
    
for valor in vetor:
    if (valor<0):
        vetorNegativo.append(valor)
        
    else:
        vetorPositivo.append(valor)
        
for valor in vetorPositivo:
    soma = soma + valor
        
print(f"A quantidade de números negativos é {len(vetorNegativo)}.")
print(f"A soma dos números positivos é {soma}.")

#Ex 12#

