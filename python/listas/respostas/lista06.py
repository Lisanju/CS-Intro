#Ex 1#

def dobrar(numeroInt):
    dobro = numeroInt * 2
    return dobro

print(dobrar(2))

#Ex 2#

def retornaMaior(n1,n2):
    if (n1 > n2):
        return n1
    else:
        return n2

print(retornaMaior(5,2))

#Ex 3#

def dataPorExtenso(dia,mes,ano):
    if (mes == 1):
        print(f'Data: {dia} de janeiro de {ano}.')

    elif (mes == 2):
        print(f'Data: {dia} de fevereiro de {ano}.')

    elif (mes == 3):
        print(f'Data: {dia} de março de {ano}.')

    elif (mes == 4):
        print(f'Data: {dia} de abril de {ano}.')

    elif (mes == 5):
        print(f'Data: {dia} de maio de {ano}.')

    elif (mes == 6):
        print(f'Data: {dia} de junho de {ano}.')

    elif (mes == 7):
        print(f'Data: {dia} de julho de {ano}.')

    elif (mes == 8):
        print(f'Data: {dia} de agosto de {ano}.')

    elif (mes == 9):
        print(f'Data: {dia} de setembro de {ano}.')

    elif (mes == 10):
        print(f'Data: {dia} de outubro de {ano}.')

    elif (mes == 11):
        print(f'Data: {dia} de novembro de {ano}.')

    elif (mes == 12):
        print(f'Data: {dia} de dezembro de {ano}.')

    else:
        print("Data inválida.")

dataPorExtenso(7,1,2003)

#Ex 4#

def desenhaLinha(numeroDeSinais):
    i = 0
    string = ""
    
    while (i < numeroDeSinais):
        i = i + 1
        string = string + "="

    print(string)

desenhaLinha(77)

#Ex 5#

def somaEntre(n1,n2):
    soma = 0

    if (n1 > n2):
        while (n2 < n1 - 1):
            n2 = n2 + 1
            soma = soma + n2 

    else:
        while (n2 - 1 > n1):
            n1 = n1 + 1
            soma = soma + n1

    return soma

print(somaEntre(12,20))

#Ex 6#

def exponenciacao(x,z):
    i = 1
    exp = x

    while (i < z):
        exp = exp * x
        i = i + 1

    return exp

print(exponenciacao(2,3))

#Ex 7#

def verificarQuadradoPerfeito(numero):
    if numero < 0:
        return False

    rq = 0
    while (rq * rq < numero):
        rq = rq + 1

    if (rq * rq == numero):
        print(f"{numero} é um quadrado perfeito.")
    else:
        print(f"{numero} não é um quadrado perfeito.")

verificarQuadradoPerfeito(16)

#Ex 8#

def volumeEsfera(raio):
    volume = (4/3) * 3.14 * (raio ** 3)
    return volume

print(volumeEsfera(4))

#Ex 9#

def convSegundos(hora,minuto,segundo):
    hora = hora * 60
    minuto = minuto + hora
    minuto = minuto * 60
    segundo = segundo + minuto
    return segundo

print(convSegundos(2,25,50))

#Ex 10#

def CpraF(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

print(CpraF(30))

#Ex 11#

def calcHipotenusa(a,b):
    hipotenusa = (a**2 + b**2)**1/2
    return hipotenusa

print(calcHipotenusa(4,6))

#Ex 12#

def volCilindro(altura,raio):
    volume = 3.141592 * raio**2 * altura
    return volume

print(volCilindro(4,2))

#Ex 13#

def fatorial(n):
    c = 0
    fatorial = 1
    i = n
    
    while (c < n):
        fatorial = fatorial * i
        i = i - 1
        c = c + 1

    return fatorial

print(fatorial(5))

#Ex 14#

def calcMedia(n1,n2,n3,letra):
    if (letra == "a"):
        mediaA = (n1 + n2 + n3)/3
        return mediaA

    elif (letra == "p"):
        mediaP = (n1*5 + n2*3 + n3*2)/10
        return mediaP

    else:
        return False

print(calcMedia(4,5,6,"p"))

#Ex 15#

def somaAlgarismos(numero):
    if (numero <= 0):
        return "Número inválido."

    else:
        soma = 0
        
        while (numero > 0):
            digito = numero % 10
            soma = soma + digito
            numero = numero // 10
            
        return soma

print(somaAlgarismos(251))

#Ex 16#

def operacoes(n1,n2,simbolo):
    if (simbolo == "+"):
        return n1+n2

    elif (simbolo == "-"):
        return n1-n2

    elif (simbolo == "/"):
        return n1/n2

    elif (simbolo == "*"):
        return n1*n2

    else:
        return False

print(operacoes(2,3,"-"))

#Ex 17#

def calcConsumo(distanciaKm,quantidadeL):
    consumo = distanciaKm/quantidadeL

    if (consumo < 8):
        return "Venda o carro!"

    elif (consumo > 12):
        return "Super econômico!"

    else:
        return "Econômico!"

print(calcConsumo(10,4))

#Ex 18#

a = int(input("Digite um valor a: "))
b = int(input("Digite um valor b: "))
c = int(input("Digite um valor c: "))

def vFormaTriangulo(a,b,c):
    if (a + b > c and b + c > a and a + c > b):
        return True

    else:
        return False

def mTipoTriangulo(a,b,c):
    if (vFormaTriangulo(a,b,c)):
        if (a == b and a == c):
            return "Equilátero"

        elif (a == b or a == c or b == c):
            return "Isósceles"

        else:
            return "Escaleno"

    else:
        False

print(mTipoTriangulo(a,b,c))

#Ex 19#

def retornaSubstring(string,substring):
    return string.find(substring)

print(retornaSubstring("Eu gosto da Nana pra caramba porque a Nana é fofa","gato"))

#Ex 20#

def vAnagrama(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if (len(s1) != len(s2)):
        return False

    contador1 = {}
    contador2 = {}

    for letra in s1:
        contador1[letra] = contador1.get(letra, 0) + 1

    for letra in s2:
        contador2[letra] = contador2.get(letra, 0) + 1

    return contador1 == contador2

print(vAnagrama("listen","sileny"))

#Ex 21#

def intercalar(s1,s2):
    sI = ""

    for char1, char2 in zip(s1,s2):
        sI = sI + char1 + char2

    return sI

print(intercalar("aaaaaaaaa","bbbbbb"))

#Ex 22#

def maiorFatorPrimo(numero):
    return True

#Ex 23#

#Ex 24#

def gerarLinha(numero):
    if (numero <= 0):
        return "Número inválido."

    for i in range(1, numero + 1):
        print("!" * i)

gerarLinha(5)

#Ex 25#

def tLateral(n):
    if (n <= 0):
        print("Número inválido.")

    else:
        c = 0
        for i in range(1,2*n):
            if (i < n):
                print("*" * i)

            else:
                print("*" * (n - c))
                c = c + 1

tLateral(55)

#Ex 26#

def gerarTriangulo(n):
    if (n <= 0):
        print("Número inválido.")

    else:
        cE = n - 1
        cD = 0

        for i in range(1,n+1):
            print((" " * cE) + ("*" * i) + ("*" * cD))
            cE = cE - 1
            cD = cD + 1

gerarTriangulo(6)

#Ex 27#

def serie(n):
    if (n <= 0):
        print("Número inválido.")

    else:
        soma = 0
        for i in range(1, n+1):
            soma = soma + (i**2 + 1)/(i +3)

        print("Resultado da série: ", soma)

serie(2)

#Ex 28#

def somatorio(n):
    if (n <= 0):
        print("Número inválido.")

    else:
        soma = 0

        for i in range(1,n+1):
            soma = soma + i

        print(soma)

somatorio(3)

#Ex 33#

import math

def neperiano(n):
    if (n < 0):
        print("Número inválido.")

    else:
        soma = 0
        for i in range(0,n+1):
            soma = soma + (1/math.factorial(i))

        print(soma)

neperiano(5)

#Ex 41#

def qPar(lista):
    listaPar = []
    for num in lista:
        if (num % 2 == 0):
            listaPar.append(num)

    return listaPar

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(qPar(lista))

#Ex 42#

def retornaMaior(lista):
    maior = -9999999999

    for num in lista:
        if (num > maior):
            maior = num

    return maior

lista = [-30,-2,0,1,4,14,20,23,35]
print(retornaMaior(lista))

#Ex 43#

def retornaMedia(lista):
    soma = 0
    q = 0

    for num in lista:
        soma = soma + num
        q = q + 1

    return soma/q

print(retornaMedia([1,2,3,4,5]))

#Ex 44#

def aleatorio(lista):
    for i in range(0,20+1):
        if (i not in lista):
            lista.append(i)

    return lista

print(aleatorio([0,1,4,5,6,7,10,23]))

#Ex 45#

def separarLista(listaTrinta):
    listaPar = []
    listaImpar = []

    for num in listaTrinta:
        if (num % 2 == 0):
            listaPar.append(num)

        else:
            listaImpar.append(num)

    return f"Lista par: {listaPar} \nLista ímpar: {listaImpar}"
    
print(separarLista([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))

#Ex 46#

def desvioPadrao(v):
    n = len(v)
    desvioPadrao = 1/(n-1)
    somatorio = 0
    somaMedia = 0

    for i in v:
        somaMedia = somaMedia + i

    media = somaMedia / n
    
    for i in v:
        somatorio = somatorio + (i - media)**2

    desvioPadrao = desvioPadrao * somatorio

    return f"O desvio padrão é {desvioPadrao}"

print(desvioPadrao([1,2,3,4,5,6,7,8,9,10]))

#Ex 47#

lista = [1,2,3,4,5,6,7,8,9,10]

def imprimir(v):
    print(v)
    return v

def reverter(v):
    vRevertido = []
    vRevertido.append(v[::-1])
    print(vRevertido)
    return vRevertido

def mediaAritmetica(v):
    media = 0
    soma = 0

    for i in v:
        soma = soma + i

    media = soma / len(v)
    print(media)
    return media

opcao = int(input("Digite uma das opções a seguir:\n1 - Impressão normal da lista.\n2 - Impressão reversa.\n3 - Função que retorna a média aritmética dos elementos da lista.\n\n-> "))

if (opcao == 1):
    imprimir(lista)

elif (opcao == 2):
    reverter(lista)

elif (opcao == 3):
    mediaAritmetica(lista)

else:
    print("Opção inválida.")

#Ex 48#

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

def maiorQue10(matriz):
    c = 0

    for linha in matriz:
        for elemento in linha:
            if (elemento > 10):
                c = c + 1

    print(f"Na matriz há {c} elementos maiores que 10")
    return c

maiorQue10(a)

#Ex 49#

b = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

def somaAD(matriz):
    soma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i < j):
                soma = soma + matriz[i][j]

    print(f"A soma dos elementos da matriz acima da diagonal principal é {soma}.")
    return soma

somaAD(b)
