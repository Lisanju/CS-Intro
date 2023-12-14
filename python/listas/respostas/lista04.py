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

vetor = []
N = 5

for n in range(0,N):
    numero = int(input("Digite um número: "))
    vetor.append(numero)
    
menor = vetor[0]
maior = vetor[0]
    
for valor in vetor:
    if (valor > maior):
        maior = valor
        
    elif (valor < menor):
        menor = valor

print(f"O menor valor do vetor é {menor}.")
print(f"O maior valor do vetor é {maior}.")

#Ex 13#

vetor = []
N = 5

for n in range(0,N):
    numero = int(input("Digite um número: "))
    vetor.append(numero)
    
menor = vetor[0]
posmenor = 0
maior = vetor[0]
posmaior = 0
    
for i in range(0,len(vetor)):
    if (vetor[i] > maior):
        maior = vetor[i]
        posmaior = i
        
    elif (vetor[i] < menor):
        menor = vetor[i]
        posmenor = i

print(f"A posição do menor valor do vetor é {posmenor}.")
print(f"A posição do maior valor do vetor é {posmaior}.")

#Ex 14#

vetor = []
N = 10

for n in range(0,N):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)
    
for i in range(0,N):
    for e in range(i+1,N):
        if (vetor[i] == vetor[e]):
            print(vetor[i])

#Ex 15#

vetor = []
vetorSemRepeticao = []
N = 20

for n in range(0,N):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)
    
for v in vetor:
    if v not in vetorSemRepeticao:
        vetorSemRepeticao.append(v)
    
print(f"Vetor sem elementos repetidos: {vetorSemRepeticao}")

#Ex 16#

vetor = []
N = 5

for n in range(0,N):
    valor = int(input("Digite um número real: "))
    vetor.append(valor)
    
print("Selecione um dos códigos abaixo:\n- 0\n- 1\n- 2")
codigo = int(input(""))
vetor.append(f"código {codigo}")

if (codigo == 0):
    print("Programa finalizado")
    
elif (codigo == 1):
    print(vetor)
    
elif (codigo == 2):
    print(vetor[::-1])
    
else:
    print("Código inválido")

#Ex 17#

vetor = []
N = 10

for n in range(0,N):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)
    
for i in range(0,N):
    if (vetor[i] < 0):
        vetor[i] = 0
        
print(vetor)

#Ex 18#

vetor = []
vetorMultiplos = []
N = 10

for n in range(0,N):
    valor = int(input("Digite um número: "))
    vetor.append(valor)
    
x = int(input("Selecione um valor x: "))

for valor in vetor:
    multiplo = x * valor
    vetorMultiplos.append(multiplo)
    
print(vetorMultiplos)

#Ex 19#

vetor = []

for i in range(0,50):
    valor = (i+5*i)%(i+1)
    vetor.append(valor)
    
print(vetor)

# ou #

vetor = [((i+5*i)%(i+1)) for i in range(0,50)]
print(vetor)

#Ex 20#

vetor1 = []
vetor2 = []
N = 10

for n in range(0,N):
    valor = int(input("Digite um valor no intervalo [0-50]: "))
    if (valor >= 0 and valor <= 50):
        vetor1.append(valor)
        
    else:
        print("O número inserido não faz parte do intervalo [0-50].")
        pass
        
print(f"Vetor 1: {vetor1}.")

for valor in vetor1:
    if (valor % 2 == 0):
        vetor2.append(valor)
        
print(f"Vetor 2: {vetor2}.")

#Ex 21#

A = []
B = []
C = []

for n in range(0,10):
    valor = int(input("Insira um número para o vetor A: "))
    A.append(valor)

for n in range(0,10):
    valor = int(input("Insira um número para o vetor B: "))
    B.append(valor)

for i in range(0,10):
    mult = A[i] * B[i]
    C.append(mult)
        
print(f"Vetor C: {C}.")

#Ex 22#

vetorA = []
vetorB = []
vetorC = []
cA = 0
cB=0

for n in range(0,10):
    valor = int(input("Digite um número para o vetor A: "))
    vetorA.append(valor)
    
for n in range(0,10):
    valor = int(input("Digite um número para o vetor B: "))
    vetorB.append(valor)
    
for i in range(0,20):
    if (i % 2 == 0):
        vetorC.append(vetorA[cA])
        cA = cA + 1
        
    else:
        vetorC.append(vetorB[cB])
        cB = cB + 1
    
print(vetorC)

#Ex 23#

vetor1 = []
vetor2 = []
pescalar = 0

for n in range(0,5):
    valor = int(input("Insira um valor para o vetor 1: "))
    vetor1.append(valor)
    
for n in range(0,5):
    valor = int(input("Insira um valor para o vetor 2: "))
    vetor2.append(valor)
    
for i in range(0,5):
    pescalar = pescalar + (vetor1[i] * vetor2[i])
    
print(f"Vetor 1: {vetor1}\nVetor 2: {vetor2}\nProduto escalar: {pescalar}")

#Ex 24#

numeros = []
alturas = []
N = 10
maiorAltura = 0
numeroMaiorAltura = 0
menorAltura = 10
numeroMenorAltura = 0

for n in range(0,N):
    numero = int(input(f"Insira o número do aluno {n}: "))
    numeros.append(numero)
    altura = float(input(f"Insira a altura do aluno {n}: "))
    alturas.append(altura)
    
for i in range(0,N):
    if (alturas[i] > maiorAltura):
        maiorAltura = alturas[i]
        numeroMaiorAltura = numeros[i]

    elif (alturas[i] < menorAltura):
        menorAltura = alturas[i]
        numeroMenorAltura = numeros[i]
        
print(f"Aluno mais alto:\nNúmero - {numeroMaiorAltura}\nAltura - {maiorAltura}\n\nAluno mais baixo:\nNúmero - {numeroMenorAltura}\nAltura - {menorAltura}")

#Ex 25#

vetor = []

for n in range(1,101):
    if (n % 7 != 0 and n % 10 != 7):
        vetor.append(n)
        
print(vetor)

#Ex 26#

import math

v = []
n = 10
soma = 0
quadradoDaDiferenca = []
somatorio = 0

for numero in range(0,n):
    add = int(input("Insira um número: "))
    v.append(add)
    
for valor in v:
    soma = soma + valor
    
m = soma/n

for valor in v:
    quadradoDaDiferenca.append((valor - m)**2)
    
for valor in quadradoDaDiferenca:
    somatorio = somatorio + valor

desvioPadrao = math.sqrt(somatorio/n-1)
print(desvioPadrao)

#Ex 27#

vetor = []
N = 10
vetorPrimos = []
c = 3

for n in range(0,N):
    numero = int(input("Insira um número: "))
    vetor.append(numero)
    
for i in range(0,N):
    if (vetor[i] < 2):
        continue                ## 0 e 1 não são primos e números negativos são desconsiderados
    
    elif (vetor[i] == 2):
        vetorPrimos.append(f"Número {vetor[i]} - Posição {i}")      ## 2 é o único número par primo
        
    elif (vetor[i] % 2 == 0):
        continue                ## Se é par, então não é primo
    
    elif (vetor[i] != c and vetor[i] % c == 0):
        continue                ## Se o resto da divisão de um número ímpar com outro ímpar é 0, então não é primo
    
    else:
        vetorPrimos.append(f"Número {vetor[i]} - Posição {i}")
        
print(vetorPrimos)

#Ex 28#

v = []
N = 10
v1 = []
v2 = []

for n in range(0,N):
    valor = int(input("Digite um número inteiro: "))
    v.append(valor)
    
for i in range(0,N):
    if (v[i] % 2 == 0):
        v2.append(v[i])
            
    elif (v[i] == 0):
        continue
    
    else:
        v1.append(v[i])
        
print(v1)
print(v2)

#Ex 29#

vetor = []
N = 6
cImpar = 0
somaPares = 0
pares = []
impares = []

for n in range(0,N):
    numero = int(input(f"{n} - Digite um número inteiro: "))
    vetor.append(numero)
    
for valor in vetor:
    if (valor % 2 == 0):
        pares.append(valor)
        somaPares = somaPares + valor
        
    else:
        impares.append(valor)
        cImpar = cImpar + 1
        
print(f"Números pares digitados: {pares}.")
print(f"Soma dos números pares digitados: {somaPares}.")
print(f"Números ímpares digitados: {impares}.")
print(f"Quantidade de números ímpares digitados: {cImpar}.")

#Ex 30#

vetorA = []
vetorB = []
vetorIntersecao = []
N = 10

for n in range(0,N*2):
    if (n < N):
        numero = int(input("Digite um número para o vetor A: "))
        vetorA.append(numero)
        
    elif (n >= N):
        numero = int(input("Digite um número para o vetor B: "))
        vetorB.append(numero)
        
for valor in vetorA:
    if (valor in vetorB and valor not in vetorIntersecao):
        vetorIntersecao.append(valor)

print(vetorIntersecao)

#Ex 31#

vetorA = []
vetorB = []
vetorUniao = []
N = 10

for n in range(0,N*2):
    if (n < N):
        numero = int(input("Digite um número para o vetor A: "))
        vetorA.append(numero)
        
    else:
        numero = int(input("Digite um número para o vetorB: "))
        vetorB.append(numero)
        
for i in range(0,N):
    if (vetorA[i] not in vetorUniao):
        vetorUniao.append(vetorA[i])
        
for i in range(0,N):
    if (vetorB[i] not in vetorUniao):
        vetorUniao.append(vetorB[i])
    
print(vetorUniao)

#Ex 32#

