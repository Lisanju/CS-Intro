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

