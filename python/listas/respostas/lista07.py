#Ex 1#

def somatorioR(n):
    if (n == 1):
        return 1

    else:
        return n + somatorioR(n-1)

print(somatorioR(10))

#Ex 2#

def fatorialR(n):
    if (n == 0):
        return 1

    else:
        return n * fatorialR(n-1)

print(fatorialR(4))

def fatorialIt(n):
    fat = 1

    for i in range(1,n+1):
        fat = fat * i

    return fat

print(fatorialIt(4))

#Ex 3#

def somaCuboR(n):
    if (n == 1):
        return 1

    else:
        return n**3 + (n-1)**3

print(somaCuboR(3))

#Ex 4#

def expoR(k,n):
    if (k == 1 or n == 0):
        return 1

    else:
        return k * expoR(k,n-1)

print(expoR(2,3))

#Ex 5#

def fibonacciR(n):
    if (n == 1 or n == 2):
        return n-1

    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

print(fibonacciR(5))

def fibonacciIt(n):
    if (n == 1 or n == 2):
        return n-1

    else:
        a = 0
        b = 1
        cont = 2

        while (cont < n):
            c = a + b
            a = b
            b = c
            cont = cont + 1

        return c

print(fibonacciIt(5))

#Ex 6#

def cresR(n):
    if (n == 0):
        print(0)
        return n

    else:
        resultado = cresR(n-1)
        print(n)
        return resultado

print(cresR(4))

#Ex 7#

def decresR(n):
    if (n == 0):
        return n

    else:
        print(n)
        return decresR(n-1)

print(decresR(4))

#Ex 8#

def parCresR(n):
    if (n < 0 or n % 2 != 0):
        return

    else:
        parCresR(n-2)
        print(n)

parCresR(10)

def imparCresR(n):
    if (n < 0 or n % 2 == 0):
        return

    else:
        imparCresR(n-2)
        print(n)

imparCresR(11)

#Ex 9#

def parCresR(n):
    if (n < 0 or n % 2 != 0):
        return

    else:
        print(n)
        parCresR(n-2)

parCresR(10)

def imparCresR(n):
    if (n < 0 or n % 2 == 0):
        return

    else:
        print(n)
        imparCresR(n-2)

imparCresR(11)

#Ex 10#

def exibirR(lista,i=0):
    if (i < len(lista)):
        print(lista[i], end = " ")
        exibirR(lista,i+1)

exibirR([1,2,3,4,5])

#Ex 11#

def menorElemento(lista):
    if (len(lista) == 1):
        return lista[0]

    else:
        copia = menorElemento(lista[1:])

        if (lista[0] < copia):
            return lista[0]

        else:
            return copia

print(menorElemento([4,3,6,2,7]))

#Ex 12#

def serieR(n):
    if (n <= 0):
        return 1

    else:
        nAnterior = serieR(n-1)
        serie = (1 + nAnterior**2) / nAnterior
        return serie

print(serieR(3))

#Ex 13#

def fatDuplo(n):
    if (n % 2 == 0):
        return "Número inválido"

    elif (n <= 0):
        return 1

    else:
        fatorial = n * fatDuplo(n-2)
        return fatorial

print(fatDuplo(5))

#Ex 14#

def fatorialQuadruploR(n):
    def fatorialR(n):
        if (n <= 1):
            return 1

        else:
            return n * fatorialR(n-1)
    
    if (n <= 1):
        return 1

    else:
        return fatorialR(2*n) / fatorialR(n)

print(fatorialQuadruploR(3))

#Ex 15#

