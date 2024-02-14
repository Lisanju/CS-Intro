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

def fibonacciR(n):
    if (n == 0 or n == 1):
        return n

    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

print(fibonacciR(6))

def fibonacciIt(n):
    if (n == 0 or n == 1):
        return n

    else:
        a = 0
        b = 1
        cont = 1

        while (cont < n):
            c = a + b
            a = b
            b = c
            cont = cont + 1

        return c

print(fibonacciIt(6))

#Ex 5#
