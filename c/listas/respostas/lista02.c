// Ex 1

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,z;
    printf("Digite um numero inteiro: ");
    scanf("%d",&x);
    y = x + 1;
    z = x - 1;
    printf("Antecessor de %d = %d\nSucessor de %d = %d\n",x,z,x,y);
    system("pause");
    return 0;
}

// Ex 2

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float x,y;
    printf("Digite um numero real: ");
    scanf("%f",&x);
    y = x/5;
    printf("Quinta parte de %f = %f\n",x,y);
    system("pause");
    return 0;
}

// Ex 3

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,z,soma;
    printf("Digite tres valores inteiros:\n");
    scanf("%d %d %d",&x,&y,&z);
    soma = x + y + z;
    printf("Soma = %d\n",soma);
    system("pause");
    return 0;
}

// Ex 4

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float a,b,c,d,media;
    printf("Digite quatro valores reais: \n");
    scanf("%f %f %f %f",&a,&b,&c,&d);
    media = (a+b+c+d)/4;
    printf("Media aritmetica = %f\n",media);
    system("pause");
    return 0;
}

// Ex 5

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int idade,anoAtual,anoNasc;
    printf("Digite sua idade e o ano atual, respectivamente: \n");
    scanf("%d %d",&idade,&anoAtual);
    anoNasc = anoAtual - idade;
    printf("Ano de nascimento = %d\n",anoNasc);
    system("pause");
    return 0;
}

// Ex 6

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float kmh,ms;
    printf("Digite uma velocidade em km/h: \n");
    scanf("%f",&kmh);
    ms = kmh/36;
    printf("Convertida em m/s = %f\n",ms);
    system("pause");
    return 0;
}

// Ex 7

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float real,cota,dolar;
    printf("Digite um valor em real e a cotacao do dolar, respectivamente: \n");
    scanf("%f %f",&real,&cota);
    dolar = real * cota;
    printf("Convertido em dolar = %f\n",dolar);
    system("pause");
    return 0;
}

// Ex 8

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int c,f;
    printf("Digite uma temperatura em graus Celsius: \n");
    scanf("%d",&c);
    f = c * (9/5) + 32;
    printf("Em graus Fahrenheit = %d\n",f);
    system("pause");
    return 0;
}

// Ex 9

#include <stdio.h>
#include <stdlib.h>

const float pi = 3.141592;
int main()
{
    float g,r;
    printf("Digite um angulo em graus: \n");
    scanf("%f",&g);
    r = g * (pi/180);
    printf("Em radianos = %f\n",r);
    system("pause");
    return 0;
}

// Ex 10

#include <stdio.h>
#include <stdlib.h>

const float imp = 780000.00;
int main()
{
    float g1,g2,g3;
    g1 = imp * (46.0/100.0);
    g2 = imp * (32.0/100.0);
    g3 = imp - (g1 + g2);
    printf("Ganhador 1 = %f\nGanhador 2 = %f\nGanhador 3 = %f\n",g1,g2,g3);
    system("pause");
    return 0;
}

// Ex 11
