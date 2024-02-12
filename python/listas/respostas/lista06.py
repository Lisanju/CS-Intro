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

