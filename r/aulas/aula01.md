# Objetos, funções e scripts

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

O R vem com várias funções que você pode utilizar para fazer tarefas sofisticadas. Por exemplo, você pode arredondar um número com `round` ou calcular seu fatorial com `factorial`.

```
round(3.1415)
## 3

factorial(3)
## 6
```

Os valores que são passados para as funções são chamados de argumentos. Um argumento pode ser um dado, um objeto ou até mesmo o resultado de outra função.

```
mean(1:6)
## 3.5

mean(die)
## 3.5

round(mean(die))
## 4
```

Existe uma função chamada `sample`, que pega dois argumentos: um vetor x e um número indicado por `size`. A função `sample` retorna do vetor a quantidade de elementos especificada por `size`.

```
sample(x = 1:4, size = 2)
## 3 2
```

Repare que tanto `1:4` e `2` são especificados para um nome `x` ou `size`. Isso acontece porque, em R, os argumentos de uma função possuem nome.

Porém, usar o nome dos argumentos é opcional. É convencionado por programadores em R que não seja especificado o nome do primeiro argumento, isso porque é óbvio o que o primeiro argumento indica.

```
sample(die, size = 1)
## 2
```

Caso você escreva o nome de um argumento que a função não reconheça, você receberá o erro a seguir.

```
round(3.1415, corners = 2)
## Error in round(3.1415, corners = 2) : unused argument(s) (corners = 2)
```

Por isso, para averiguar os nomes dos argumentos de uma função, use a função `args`.

```
args(round)
## function (x, digits = 0) 
## NULL
```

Note que o argumento `digits` da função `round` é por padrão setado como 0. Isso acontece porque para algumas funções há argumentos que são opcionais, como é o caso de `digits`. Se não for especificado um valor para o argumento opcional, o R usará o valor setado como padrão.

```
round(3.1415)
## 3

round(3.1415, digits = 2)
## 3.14
```

## Criando a própria função

Toda função em R tem três partes básicas: nome, corpo de código e lista de argumentos. Para criar uma função em R, você precisa replicar essas partes em um objeto, o que pode ser feito através da função `function`.

```
funcao_criada <- function() {
  # corpo de código
}
```

Então, para criar uma função que role um dado, podemos fazer o seguinte:

```
roll <- function() {
  die <- 1:6
  dice <- sample(die, size = 2, replace = TRUE)
  sum(dice)
}

roll()
## 8 

roll()
## 3

roll()
## 7
```

Imagine que para função a seguir, você substitua o nome `die` pelo objeto `bones`.

```
roll2 <- function() {
  dice <- sample(bones, size = 2, replace = TRUE)
  sum(dice)
}
```

Caso você rode o código assim, o R retornará um erro: 

```
roll2()
## Error in sample(bones, size = 2, replace = TRUE) : 
##   object 'bones' not found
```

Isso acontece porque, para o escopo da função `sample` dentro da função `roll2`, não há declarado o objeto bones, logo, não há nenhum valor sendo usado pelo argumento.

Para reverter esse erro, você pode adicionar o argumento bones para a função `roll2`.

```
roll2 <- function(bones) {
  dice <- sample(bones, size = 2, replace = TRUE)
  sum(dice)
}

roll2(bones = 1:4)
##  3

roll2(bones = 1:6)
## 10

roll2(1:20)
## 31
```

## Scripts

Em R, um script é um arquivo de texto que você utiliza para salvar um código. No RStudio, você pode abrir um script em `File > New File > R script` na barra de menu. Os scripts são uma boa maneira de editar e fazer o proofreading de um código, além de ser uma cópia para compartilhar seu código com outras pessoas.

No RStudio, você pode salvar um script em `File > Save As`. Além disso, para executar o trecho de um script, você pode usar a opção Run (ou o atalho Control + Return). E, para rodar o script todo, você pode usar a opção Source.

Os scripts em R são salvos com a extensão `.r`.
