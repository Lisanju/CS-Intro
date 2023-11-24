# 1 - Faça um programa que leia 10 inteiros e imprima sua média #

c = 0
soma = 0

while(c<10):
    n = int(input("Insira um número inteiro: "))
    
    soma = soma + n
    c = c + 1
    
print("A média dos números fornecidos é: ",soma/10)

# 2 - Uma empresa contrata um encadanor a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhos pelo encadanor e imprima a quantia líquida que deverá ser paga, #
# sabendo-se que são descontados 8% para imposto de renda #

numeroDias = int(input("Insira o número de dias trabalhados: "))
valorDias = 0
c = 0

while(c<numeroDias):
    valorDias = valorDias + 30
    c = c + 1
    
desconto = (8/100)*valorDias
total = valorDias - desconto

print("O total a ser pago, com o desconto, é de: ", total)

# 3 - Escreva o menu de opções a seguir. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. #
# Escolha a opção: #
# 1 - Soma de 2 números #
# 2 - Diferença entre 2 números (maior pelo menor) #
# 3 - Produto entre 2 números #
# 4 - Divisão entre 2 números (o denominador não pode ser 0) #

ler = int(input("Escolha a opção:\n"
                "1 - Soma de 2 números.\n"
                "2 - Diferença entre 2 números (maior pelo menor).\n"
                "3 - Produto entre 2 números\n"
                "4 - Divisão entre 2 números (o denominador não pode ser 0)"))
                
if(ler==1):
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    print("A soma dos dois números é: ", n1+n2)
    
elif(ler==2):
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    
    if(n1>=n2):
        print("A diferença entre os dois números é: ", n1-n2)
        
    else:
        print("A diferença entre os dois números é: ", n2-n1)
        
elif(ler==3):
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    print("O produto entre os dois números é: ", n1*n2)
    
elif(ler==4):
    n1 = int(input("Insira um número para numerador: "))
    n2 = int(input("Insira outro número para denominador: "))
    
    if(n2==0):
        print("O denominador não pode ser igual a 0")
        
    else:
        print("A divisão entre os dois números é: ", n1/n2)
    
else:
    print("Erro: opção inválida")

# 4 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela a seguir: #
# CONSUMO | (Km/l) | MENSAGEM #
# menor que | 8 | Venda o carro! #
# entre | 8 e 14 | Ecônomico! #
# maior que | 12 | Super econômico! #

km = int(input("Insira uma distância em Km: "))
l = int(input("Insira uma quantidade em litros: "))

kml = km/l

if(kml<8):
    print("Venda o carro!")
    
elif(8<kml<14):
    print("Econômico!")
    
elif(kml>14):
    print("Super econômico!")
    
# 5 - Faça um programa que calcule e escreva o valor de S #
# S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50 #

num = 1
soma = 0

for dem in range(1,50+1):
    soma = soma + num/dem
    num = num + 2
    
print(soma)
