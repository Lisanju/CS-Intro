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

