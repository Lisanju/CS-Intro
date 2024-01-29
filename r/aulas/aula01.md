# Objetos, funções, argumentos e scripts

## Objetos

Um objeto nada mais é que um nome que você usa para chamar por um dado armazenado na memória do computador.

Para criar um objeto em R, escolha um nome e use o `<-` para indicar o valor a ser armazenado nele.

```
die <- 1:6
# um objeto chamado 'die' que armazena valores de 1 a 6.
```

Quando um objeto é criado, ele irá aparecer no painel de ambientação do RStudio, localizado no canto direito superior. Esse painel mostra todos os objetos criados desde que o RStudio foi aberto.

Você pode nomear um objeto em R de praticamente qualquer coisa, mas há algumas restrições. Primeiro, um objeto não pode começar com um número. Segundo, um objeto não pode conter em seu nome os símbolos especiais `!`, `$`, `@`, `-`, `/` ou `*`.

Note que o R é uma linguagem de caso sensitivo, o que significa que letras maiúsculas e minúsculas são entendidas como caracteres diferentes.

Com a função `ls`, você pode conferir os nomes de objetos que já estão sendo utilizados:

```
ls()
## "a"         "die"       "my_number" "name"     "Name"
```

Outra alternativa para ver os nomes de objetos já utilizados é olhar no painel de ambientação do RStudio.

Em R, é utilizado uma forma de manipulação de matrizes chamada element-wise execution, em que o R aplica a mesma operação para cada elemento em um conjunto de números. Então, se você rodar `die - 1`, o R irá subtrair 1 de cada elemento do objeto 'die'.

Por outro aldo, quando você roda `die * die`, o R alinhará os dois vetores e multiplicará o primeiro elemento do vetor 1 pelo primeiro elemento do vetor 2 e assim por diante. Caso o vetor 1 seja menor que o vetor 2, os elementos do vetor 1 irão se repetir até que o número de elementos seja equivalente ao vetor 2.

```
1:2
## 1 2

1:4
## 1 2 3 4

die
## 1 2 3 4 5 6

die + 1:2
## 2 4 4 6 6 8

die + 1:4
## 2 4 6 8 6 8
Warning message:
In die + 1:4 :
  longer object length is not a multiple of shorter object length
```

Mas isso tudo não quer dizer que o R não possa fazer a multiplicação tradicional de matrizes. Para isso, você deve especificar através de `%*%` para multiplicação interna e `%o%` para multiplicação externa.

```
die %*% die
## 91

die %o% die
##      [,1] [,2] [,3] [,4] [,5] [,6]
## [1,]    1    2    3    4    5    6
## [2,]    2    4    6    8   10   12
## [3,]    3    6    9   12   15   18
## [4,]    4    8   12   16   20   24
## [5,]    5   10   15   20   25   30
## [6,]    6   12   18   24   30   36
```

Caso queira transpor uma matriz ou pegar seu determinante, você pode usar respectivamente `t` e `det`.

## Funções
