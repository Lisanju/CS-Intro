## Tipos e estruturas de dados

Em R, há diferentes aspectos para os tipos de dados existentes. A ideia dessa aula, então, é apresentar esses aspectos.

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

