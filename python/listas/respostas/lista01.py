#Ex 1#

intn = int(input("Digite um número inteiro: "))
print(intn)

#Ex 2#

rn = float(input("Digite um número real: "))
print(rn)

#Ex 3#

int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
int3 = int(input("Digite mais um número inteiro: "))
print(int1+int2+int3)

#Ex 4#

rn = float(input("Digite um número real: "))
print(rn**2)

#Ex 5#

rn = float(input("Digite um número real: "))
print(rn/5)

#Ex 6#

celsius_temp = float(input("Digite uma temperatura em graus Celsius: "))
fahrenheit_temp = (celsius_temp*9)/5 + 32
print("A temperatura em graus Fahrenheit é: ", fahrenheit_temp)

#Ex 7#

fahrenheit_temp = float(input("Digite uma temperatura em graus Fahrenheit: "))
celsius_temp = (fahrenheit_temp*5)/9 - 32
print("A temperatura em graus Celsius é: ", celsius_temp)

#Ex 8#

kelvin_temp = float(input("Digite uma temperatura em graus Kelvin: "))
celsius_temp = kelvin_temp - 273.15
print("A temperatura em graus Celsius é: ", celsius_temp)

#Ex 9#

celsius_temp = float(input("Digite uma temperatura em graus Celsius: "))
kelvin_temp = celsius_temp + 273.15
print("A temperatura em graus Kelvin é: ", kelvin_temp)

#Ex 10#

kmh_v = float(input("Digite uma velocidade em km/h: "))
ms_v = kmh_v/3.6
print("A velocidade em m/s é: ", ms_v)

#Ex 11#

ms_v = float(input("Digite uma velocidade em m/s: "))
kmh_v = ms_v*3.6
print("A velocidade em km/h é: ", kmh_v)

#Ex 12#

m_d = float(input("Digite uma distância em milhas: "))
km_d = m_d*1.61
print("A distância em km é: ", km_d)

#Ex 13#

km_d = float(input("Digite uma distância em km: "))
m_d = km_d/1.61
print(m_d)

#Ex 14#

g_ang = float(input("Digite um ângulo em graus: "))
rad_ang = (g_ang*3.14)/180
print("O ângulo em radianos é: ", rad_ang)

#Ex 15#

rad_ang = float(input("Digite um ângulo em radianos: "))
g_ang = (rad_ang*180)/3.14
print("O ângulo em graus é: ", g_ang)

#Ex 16#

p_comp = float(input("Digite um comprimento em polegadas: "))
cm_comp = p_comp*2.54
print("O comprimento em centímetros é: ", cm_comp)

#Ex 17#

cm_comp = float(input("Digite um comprimento em centímetros: "))
p_comp = cm_comp/2.54
print("O comprimento em polegadas é: ", p_comp)

#Ex 18#

mc_vol = float(input("Digite um valor de volume em metros cúbicos: "))
l_vol = mc_vol*1000
print("O valor de volume em litros é: ", l_vol)

#Ex 19#

l_vol = float(input("Digite um valor de volume em litros: "))
mc_vol = l_vol/1000
print("O valor do volume em metros cúbicos é: ", mc_vol)

#Ex 20#

kg_m = float(input("Digite um valor de massa em quilogramas: "))
lb_m = kg_m/0.45
print("O valor de massa em libras é: ", lb_m)

#Ex 21#

lb_m = float(input("Digite um valor de massa em libras: "))
kg_m = lb_m*0.45
print("O valor de massa em quilogramas é: ", kg_m)

#Ex 22#

j_comp = float(input("Digite um comprimento em jardas: "))
m_comp = j_comp*0.91
print("O valor do comprimento em metros é: ", m_comp)

#Ex 23#

m_comp = float(input("Digite um comprimento em metros: "))
j_comp = m_comp/0.91
print("O valor do comprimento em jardas é: ", j_comp)

#Ex 24#

mq_a = float(input("Digite um valor de área em metros quadrados: "))
ac_a = mq_a*0.000247
print("O valor da área em acres é: ", ac_a)

#Ex 25#

ac_a = float(input("Digite um valor de área em acres: "))
mq_a = ac_a/0.000247
print("O valor da área em metros quadrados é: ", mq_a)

#Ex 26#

mq_a = float(input("Digite um valor de área em metros quadrados: "))
hec_a = mq_a*0.0001
print("O valor da área em hectares é: ", hec_a)

#Ex 27#

hec_a = float(input("Digite um vlaor de área em hectares: "))
mq_a = hec_a*1000
print("O valor da área em metros quadrados é: ", mq_a)

#Ex 28#

v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
v3 = int(input("Digite mais um valor: "))
print(v1**2 + v2**2 + v3**2)

#Ex 29#

n1 = int(input("Nota P1: "))
n2 = int(input("Nota P2: "))
n3 = int(input("Nota P3: "))
n4 = int(input("Nota P4: "))
media = (n1+n2+n3+n4)/4

#Ex 30#

v_real = float(input("Digite um valor de dinheiro em real: "))
cot_dolar = float(input("Digite a cotação do dolar: "))
v_dolar_convertido = v_real*cot_dolar

#Ex 31#

intn = int(input("Digite um número inteiro: "))
print("Antecessor: ", intn - 1, " Sucessor: ", intn + 1)

#Ex 32#

intn = int(input("Digite um número inteiro: "))
print(((intn*3)+1) + ((intn*2)-1))

#Ex 33#

lado = float(input("Digite o valor do lado de um quadrado: "))
print("A área desse quadrado é: ", lado*lado)

#Ex 34#

raio = float(input("Digite o valor do raio de um círculo: "))
print("A área desse círculo é: ", (raio**2)*3.141592)

#Ex 35#

a = int(input("Cateto a: "))
b = int(input("Cateto b: "))
hipotenusa = (a**2 + b**2)**0.5
print("A hipotesuna é: ", hipotenusa)

#Ex 36#

altura = float(input("Digite a altura de um cilindro circular: "))
raio = float(input("Digite o raio desse mesmo cilindro: "))
volume = 3.141592*(raio**2)*altura
print("O volume desse cilindro circular é: ", volume)

#Ex 37#

valor_produto = float(input("Digite o valor do produto: "))
desconto = valor_produto*(12/100)
valor_com_desconto = valor_produto - desconto
print("O valor do produto com desconto é: ", valor_com_desconto)

#Ex 38#

salario = float(input("Salário: "))
aumento = salario*(25/100)
salario_aumento = salario + aumento
print("O salário com aumento é: ", salario_aumento)

#Ex 39#

imp = 780000.00
d1 = imp*(46/100)
d2 = imp*(32/100)
d3 = imp*(22/100)
g1 = imp - d1
g2 = imp - d2
g3 = imp - d3
print("O ganhador 1 receberá: ", g1, "\nO ganhador 2 receberá: ", g2, "\nO ganhador 3 receberá: ", g3)

#Ex 40#

valor_p_dia = 30.00
dias_trabalhados = float(input("Digite o número de dias trabalhados: "))
quantia_liquida = valor_p_dia*dias_trabalhados
desconto = quantia_liquida*(8/100)
total = quantia_liquida - desconto
print("O encanador receberá R$", total, " por ", dias_trabalhados, "dias trabalhados.")

#Ex 41#

valor_de_hora = float(input("Digite o valor de hora de trabalho em reais: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_pago = valor_de_hora*horas_trabalhadas
print(valor_pago+(valor_pago*(10/100)))

#Ex 42#

salario_base = float(input("Digite o salário-base de um funcionário: "))
grat = salario_base*(5/100)
imposto = salario_base*(7/100)
salario_total = salario_base + grat - imposto
print("O funcionário recebe: ", salario_total)

#Ex 43#

valor = float(input("Digite um valor: "))
total_desconto = valor - (valor*(10/100))
total_parcelado = valor/3
total_comissao_vista = total_desconto + (total_desconto*5/100)
total_comissao_parcelado = total_desconto + (valor*5/100)
print("Com desconto de 10%, o valor a se pagar é: ", total_desconto)
print("O valor parcelado em três vezes sem juros é de ", total_parcelado, " por parcela")
print("A comissão do vendedor em venda à vista é: ", total_comissao_vista)
print("A comissão do vendedor em venda parcelada é: ", total_comissao_parcelado)

#Ex 44#

alturade = int(input("Digite a altura atual do degrau: "))
alturaal = int(input("Digite a altura do degrau que deseja alcançar: "))
print("Faltam ", alturaal - alturade, " para alcançar o degrau desejado")

#Ex 45#

numero = int(input("Digite um número de três dígitos (100 - 999): "))
inverso = int(str(numero)[::-1])
print(inverso)

#Ex 46#

a = int(input("Digite um número entre (1000 e 9999): "))

if (a < 10000 and a > 999):
    for digito in str(a):
        print(digito)

else:
    print("Número inválido.")

# Ex 47 #

s = int(input("Digite um valor em segudos: "))
m = s / 60
h = m / 60
print(f"Horas: {h}\nMinutos: {m}\nSegundos: {s}")

# Ex 48 #

print("A seguir, digite o horário de início do experimento biológico.")
hI = int(input("Em que hora começou? "))
mI = int(input("Em que minuto começou? "))
sI = int(input("Em que segundo começou? "))
d = int(input("Quantos segundos durou o experimento biológico?"))

mI = mI + hI * 60
sI = sI + mI * 60
sI = sI + d

sT = sI % 60
mTa = (sI - sT) / 60
mTd = mTa % 60
hT = (mTa - mTd) / 60

print(f"{int(hT)}:{int(mTd)}:{int(sT)}")

# Ex 49 #

anoAtual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
print(f"Você nasceu em {anoAtual - idade}")

# Ex 50 #

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
r = (x**2 + y**2)**1/2
print(f"A distância é: {r}")

# Ex 51 #

a1 = float(input("Aposta do jogador 1: "))
a2 = float(input("Aposta do jogador 2: "))
a3 = float(input("Aposta do jogador 3: "))
v = float(input("Valor do prêmio: "))
atotal = a1+a2+a3
p1 = a1/atotal
p2 = a2/atotal
p3 = a3/atotal
r1 = v*p1
r2 = v*p2
r3 = v*p3
print(f"O jogador 1 recebe {r1}, o jogador 2 recebe {r2} e o jogador 3 recebe {r3}.")

# Ex 52 #

c = float(input("Comprimento do terreno: "))
l = float(input("Largura do terreno: "))
p = float(input("Preço do metro de tela: "))
mQ = c*l
custo = mQ**1/2
print(f"O custo é {custo}")
