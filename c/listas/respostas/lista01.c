// Ex 1

#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Inicio do programa\nFim\n");

    system("pause");
    return 0;
}

// Ex 2

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    scanf("%d",&x);

    system("pause");
    return 0;
}

// Ex 3

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    scanf("%d",&x);

    printf("Valor lido: %d\n",x);

    system("pause");
    return 0;
}

// Ex 4

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    scanf("%d",&x);

    // A função print escreve na tela o valor 0.000000
    printf("Valor lido: %f\n",x);

    system("pause");
    return 0;
}

// Ex 5

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float x;
    scanf("%f",&x);

    // A função print escreve na tela o valor 0
    printf("Valor lido: %d\n",x);

    system("pause");
    return 0;
}

// Ex 6

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double x;
    scanf("%f",&x);

    printf("Valor lido: %e\n",x);

    system("pause");
    return 0;
}

// Ex 7

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x;
    scanf("%c",&x);

    printf("Codigo ASCII: %d\n",x);

    system("pause");
    return 0;
}

// Ex 8

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y;
    scanf("%d%d",&x,&y);

    printf("Printados na ordem inversa em que foram inseridos: %d %d\n",y,x);

    system("pause");
    return 0;
}

// Ex 9

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float x,y;
    scanf("%f%f",&x,&y);
    printf("Printados na ordem inversa em que foram inseridos: %f %f\n",y,x);
    system("pause");
    return 0;
}

// Ex 10

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int dia,mes,ano;
    scanf("%d/%d/%d",&dia,&mes,&ano);
    printf("%d/%d/%d\n",dia,mes,ano);
    system("pause");
    return 0;
}

// Ex 11

#include <stdio.h>
#include <stdlib.h>

int main()
{
    #define x 7.5
    printf("%f\n",x);

    system("pause");
    return 0;
}

// Ex 12

#include <stdio.h>
#include <stdlib.h>

int main()
{
    const float x = 7.5;
    printf("%f\n",x);

    system("pause");
    return 0;
}

// Ex 13

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x;
    scanf("%c",&x);
    printf("\"%c\"\n",x);

    system("pause");
    return 0;
}

// Ex 14

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x,y,z;
    scanf("%c %c %c",&x,&y,&z);
    printf("%c\n%c\n%c\n",x,y,z);

    system("pause");
    return 0;
}

// Ex 15

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x;
    int y;
    float z;
    scanf("%c %d %f",&x,&y,&z);
    printf("%c %d %f\n\n%c\t%d\t%f\n\n%c\n%d\n%f\n\n",x,y,z,x,y,z,x,y,z);

    system("pause");
    return 0;
}
