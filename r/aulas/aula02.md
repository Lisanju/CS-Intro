## Estrutura de dados

Em R, há diferentes aspectos para os tipos de objetos de dados existentes. A ideia dessa aula, então, é apresentar esses aspectos.

### Double

O tipo double é usado para representar números inteiros, normalmente representando variáveis continuas como peso e altura de uma pessoa.

```
x <- 8.14
y <- 8.0
z <- 87.0 + 12.9
```

Para checar se um objeto é do tipo double, use a função `is.double`.

```
typeof(x)
[1] "double"
is.double(8.9)
[1] TRUE
test <- 1223.456
is.double(test)
[1] TRUE
```

Note que o tipo double é apenas uma aproximação dos números reais. O computador pode não conseguir representar com exatidão números como π ou √2. Por isso, esteja
sempre atento quando for realizar operações com o tipo double, pois erros como o seguinte podem ocorrer:

```
0.3 == 0.1 + 0.1 + 0.1
[1] FALSE
```

### Integer

O tipo integer representa números naturais. Ele pode ser usado para variáveis contáveis, como o número de crianças de uma família.

```
nchild <- as.integer(3)
is.integer(nchild)
[1] TRUE
```

Note que 3.0 não é do tipo integer, nem 3 por padrão é um tipo integer.

```
nchild <- 3.0
is.integer(nchild)
[1] FALSE
nchild <- 3
is.integer(nchild)
[1] FALSE
```

Para o R, um 3 do tipo integer é diferente de um 3 do tipo double. No entanto, é possível realizar operações entre tipos double e integer sem problemas.

```
x <- as.integer(7)
y <- 2.0
z <- x/y
```

Em contraste com outras linguagens de programação, o resultado da operação acima em R é do tipo double, isto é, 3.5. O integer máximo em R é 2³¹ − 1.

```
as.integer(2^31 - 1)
[1] 2147483647
as.integer(2^31)
[1] NA
Warning message:
NAs introduced by coercion
```

### Complex

O tipo complex é usado para representar números complexos. Geralmente eles não são utilizados numa análise de dados estatísticos. Use a função `as.complex` ou `complex` para criar objetos do tipo complex.

```
test1 <- as.complex(-25+5i)
sqrt(test1)
[1] 0.4975427+5.024694i

test2 <- complex(5,real=2,im=6)
test2
[1] 2+6i 2+6i 2+6i 2+6i 2+6i
typeof(test2)
[1] "complex"
```

Note que por padrão as operações resultam em números reais. Então, sqrt(-1) resultará em NA. Use `sqrt(as.complex(-1))`.

### Logical

Objetos do tipo logical podem receber os valores TRUE ou FALSE e são usados para indicar se uma condição é verdadeira ou falsa. Esses objetos geralmente são expressos como o resultado de uma expressão lógica.

```
x <- 9
y <- x > 10
y
[1] FALSE
```

Por exemplo, o resultado da função `is.double` é um objeto do tipo logical, contendo TRUE ou FALSE.

```
is.double(9.876)
[1] TRUE
```

As expressões lógicas são normalmente construídas a partir dos operadores lógicos:

- `<` - menor que
- `<=` - menor ou igual que
- `>` - maior que
- `>=` - maior ou igual que
- `==` - igual
- `!=` - diferente

Os operadores lógicos AND, OR e NOT são expressos, respectivamente, por `&`, `—` e `!`.

```
x <- c(9,166)
y <- (3 < x) & (x <= 10)
[1] TRUE FALSE
```

Em R, cálculos também podem ser feitos através do tipo logical. Sendo este o caso em que FALSE é substituído por 0 e TRUE é substituído por 1. Então, por exemplo, é possível usar do tipo lógico para contar o número de TRUE's num vetor ou array.

```
x <- 1:15
## number of elements in x larger than 9
sum(x>9)
[1] 6
```

### Character

O objeto do tipo character é representado entre aspas duplas `" "`. Há diferentes formas de criar um objeto do tipo character:

```
x <- c("a","b","c")
x
[1] "a" "b" "c"
mychar1 <- "This is a test"
mychar2 <- "This is another test"
charvector <- c("a", "b", "c", "test")
```

### Factor

O tipo factor é usado para representar dados categóricos, isto é, dados que possuem como valor uma coleção de codes. Por exemplo:

- Variável 'sexo' com os valores masculino e feminino.
- Variável 'tipo-sanguineo' com os valores A, AB e O.

Cada code individual de uma variável factor é também chamada de level. Então, a variável 'sexo' possui 2 levels e a variável 'tipo-sanguineo' possui 3 levels.
Geralmente o tipo factor é confundido com o tipo character. Variáveis do tipo character são usadas para dar nome à camadas em gráficos, colunas ou linhas. Já variáveis do tipo factor são usadas quando você quer representar uma variável discreta em um dataframe e quer analisar ela.

Você pode criar um objeto factor a partir de um objeto character ou numérico usando a função `factor`.

```
sex <- c("male","male","female","male","female")

sex <- factor(sex)
sex
[1] male male female male female
```

Inicialmente, o objeto 'sex' é do tipo character. É necessário transformar ele com `factor`. 

Ao usar a função `levels`, é possível conferir quantos levels uma variável do tipo factor possui.

```
levels(sex)
[1] "female" "male"
```

Note que o resultado da função `levels` é do tipo character.

```
sex <- c(1,1,2,1,2)

sex <- factor(sex)
sex
[1] 1 1 2 1 2
Levels: 1 2
```

Caso você crie um objeto factor a partir da transformação de uma variável integer para factor, como representado acima, o resultado do objeto 'sex' não será do tipo integer (apesar de se parecer com).

Os números 1 representam level '1' e os números 2 representam level '2'. Por isso, operações aritméticas não funcionam com a variável 'sex'.

```
sex + 7
[1] NA NA NA NA NA
Warning message:
+ not meaningful for factors in: Ops.factor(sex, 7)
```

Para que você não se confunda, é possível renomear os levels 1 e 2:

```
levels(sex) <- c("male","female")
sex
[1] male male female male female
```

Você também pode transformar variáveis factor em double ou integer usando as funções `as.double` e `as.integer`.

```
sex.numeric <- as.double(sex)
sex.numeric
[1] 2 2 1 2 1
```

O número 1 indica o level female apenas porque female aparece antes alfabeticamente. Se a ordem dos levels for importante, você deve utilizar um factor ordenado. Use a função `ordered` e especifique a ordem dos levels no argumento.

```
Income <- c("High","Low","Average","Low","Average","High","Low")
Income <- ordered(Income, levels=c("Low","Average","High"))
Income
[1] High Low Average Low Average High Low
Levels: Low < Average < High
```
