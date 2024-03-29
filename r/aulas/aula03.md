# Dataframes, listas e vetores

## Dataframe

Um dataframe é uma estrutura de dado adequada para uso estatístico. Funciona como uma planilha de dados.

```
vog.df <- data.frame(pos=c(1, 2, 3), dur=c(103.288, 143.24, 89.54), car= c("e", "a", "o"), ton=c(F, T, F))
```

É possível observar o conteúdo de um dataframe invocando a variável que o armazena.

```
vog.df
##   pos     dur car   ton
## 1   1 103.288   e FALSE
## 2   2 143.240   a  TRUE
## 3   3  89.540   o FALSE
```

Um dataframe é um quadro retangular assim como uma matriz, porém, diferentemente da matriz, um dataframe permite armazenar objetos de diferentes tipos. Ou seja, é uma estrutura de dados heterogênea.

Cada linha do dataframe é uma observação e cada coluna corresponde a uma variável.

Para criar um dataframe, utiliza-se a função `data.frame`.

```
# criando um dataframe
dados <- data.frame(
  datas = c(
    "2013-01-01", "2013-01-02", "2013-01-03", "2013-01-04", "2013-01-05",
    "2013-01-06", "2013-01-07", "2013-01-08", "2013-01-09", "2013-01-10",
    "2013-01-11", "2013-01-12", "2013-01-13", "2013-01-14", "2013-01-15"
  ),
  cidade = rep("Santa Maria", 15),
  tar = c(31, 35, 21, 23, 33, 17, 18, 16, 34, 27, 15, 28, 22, 29, 32)
)

dados
##         datas      cidade tar
## 1  2013-01-01 Santa Maria  31
## 2  2013-01-02 Santa Maria  35
## 3  2013-01-03 Santa Maria  21
## 4  2013-01-04 Santa Maria  23
## 5  2013-01-05 Santa Maria  33
## 6  2013-01-06 Santa Maria  17
## 7  2013-01-07 Santa Maria  18
## 8  2013-01-08 Santa Maria  16
## 9  2013-01-09 Santa Maria  34
## 10 2013-01-10 Santa Maria  27
## 11 2013-01-11 Santa Maria  15
## 12 2013-01-12 Santa Maria  28
## 13 2013-01-13 Santa Maria  22
## 14 2013-01-14 Santa Maria  29
## 15 2013-01-15 Santa Maria  32

class(dados)
## [1] "data.frame"

is.data.frame(dados)
## [1] TRUE
```

Acima há um dataframe com medidas de temperatura da estação de Santa Maria, retirado do Ebook Análise de Dados Ambientais com R.

É possível usar a função `str` para averiguar as variáveis de um dataframe.

```
str(dados)
## 'data.frame':    15 obs. of  3 variables:
##  $ datas : chr  "2013-01-01" "2013-01-02" "2013-01-03" "2013-01-04" ...
##  $ cidade: chr  "Santa Maria" "Santa Maria" "Santa Maria" "Santa Maria" ...
##  $ tar   : num  31 35 21 23 33 17 18 16 34 27 ...
```

Já a função `summary` retorna um resumo estatístico das variáveis de um dataframe.

```
summary(dados)
##     datas              cidade               tar      
##  Length:15          Length:15          Min.   :15.0  
##  Class :character   Class :character   1st Qu.:19.5  
##  Mode  :character   Mode  :character   Median :27.0  
##                                        Mean   :25.4  
##                                        3rd Qu.:31.5  
##                                        Max.   :35.0
```

Através da função `rownames` é possível atribuir um nome para cada observação do dataframe.

```
# novos nomes para as linhas de dados
rownames(dados) <- paste0("linha", rownames(dados))
dados
##              datas      cidade tar
## linha1  2013-01-01 Santa Maria  31
## linha2  2013-01-02 Santa Maria  35
## linha3  2013-01-03 Santa Maria  21
## linha4  2013-01-04 Santa Maria  23
## linha5  2013-01-05 Santa Maria  33
## linha6  2013-01-06 Santa Maria  17
## linha7  2013-01-07 Santa Maria  18
## linha8  2013-01-08 Santa Maria  16
## linha9  2013-01-09 Santa Maria  34
## linha10 2013-01-10 Santa Maria  27
## linha11 2013-01-11 Santa Maria  15
## linha12 2013-01-12 Santa Maria  28
## linha13 2013-01-13 Santa Maria  22
## linha14 2013-01-14 Santa Maria  29
## linha15 2013-01-15 Santa Maria  32
```

Apesar desse recurso existir, normalmente ele não é muito utilizado porque é possível adicionar uma coluna com nome para identificar cada observação.

Por isso, para remover os nomes das observações, use `rownames(dados) <- NULL`.

Os nomes das variáveis de um dataframe podem ser adicionados com a função `names` ou também `colnames`.

```
names(dados)
#> [1] "datas"  "cidade" "tar"

# mesmo que names(dados)
colnames(dados)
#> [1] "datas"  "cidade" "tar
```

## Acesso de dados em um dataframe

Para acessar as variáveis de um dataframe, é possível usar os operadores de extração de elementos `[`, `[[` ou `$`. Observe a seguir as diferenças nos resultados de cada operador.

```
# variáveis do dataframe

names(dados)
## [1] "datas"  "cidade" "tar"

# acessando os dados de temperatura

dados[, 3]
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

# ou

dados[, "tar"]
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

# ou

dados$tar
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

is.vector(dados$tar)
## [1] TRUE

# note a diferença no resultado da extração
dados["tar"]
##    tar
## 1   31
## 2   35
## 3   21
## 4   23
## 5   33
## 6   17
## 7   18
## 8   16
## 9   34
## 10  27
## 11  15
## 12  28
## 13  22
## 14  29
## 15  32

class(dados["tar"])
## [1] "data.frame"

dados[["tar"]]
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

class(dados[["tar"]])
## [1] "numeric"

dados[, "tar"]
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

class(dados[, "tar"])
## [1] "numeric"
```

Além disso, também é possível acessar as variáveis de um dataframe através da função `with(data, expr)`.

```
# acesso a variáveis de um dataframe

with(data = dados, expr = tar)
##  [1] 31 35 21 23 33 17 18 16 34 27 15 28 22 29 32

tarK <- with(data = dados, expr = tar + 273.15)
tarK
##  [1] 304.15 308.15 294.15 296.15 306.15 290.15 291.15 289.15 307.15 300.15
## [11] 288.15 301.15 295.15 302.15 305.15

# gráfico de uma variável usando with()
with(data = dados, 
     # parâmetro expr geralmente não é mostrado
       plot(tar + 273.15, type = "o")
     )
```

O argumento `expr` pode ser substituído por qualquer expressão ou conjunto de expressão que envolvam as variáveis de um dataframe. Caso você o substitua por uma expressão com mais de uma linha, você deve utilizar `{`.

```
with(dados, 
     {
       dates <- as.Date(datas)
       plot(dates, tar, type = "o")
     }
)
```

## Indexação, seleção e substituição de dados em um dataframe

Como os dataframes possuem duas dimensões, é possível indexicar tanto linhas quanto colunas.

```
quadro_dados[inds_lin, inds_col]

# exclui a primeira e a última observação para todas variáveis

(inds_lin <- -c(1, nrow(dados)))
## [1]  -1 -15

(inds_col <- 3)
## [1] 3

dados[inds_lin, inds_col]
##  [1] 35 21 23 33 17 18 16 34 27 15 28 22 29
```

Podemos acessar a temperatura no dia 2013-01-09 usando:

```
dados[dados$datas == "2013-01-09", "tar"]
#> [1] 34
```

Para acrescentar uma nova variável chamada `prec`:

```
# acrescentar uma nova variavel
dados$prec <- c(rep(0, 5), 10, 18, 4, 0, 0, 5, 0, 0, 2, 0)

dados
##         datas      cidade tar prec
## 1  2013-01-01 Santa Maria  31    0
## 2  2013-01-02 Santa Maria  35    0
## 3  2013-01-03 Santa Maria  21    0
## 4  2013-01-04 Santa Maria  23    0
## 5  2013-01-05 Santa Maria  33    0
## 6  2013-01-06 Santa Maria  17   10
## 7  2013-01-07 Santa Maria  18   18
## 8  2013-01-08 Santa Maria  16    4
## 9  2013-01-09 Santa Maria  34    0
## 10 2013-01-10 Santa Maria  27    0
## 11 2013-01-11 Santa Maria  15    5
## 12 2013-01-12 Santa Maria  28    0
## 13 2013-01-13 Santa Maria  22    0
## 14 2013-01-14 Santa Maria  29    2
## 15 2013-01-15 Santa Maria  32    0
```

A função `subset` permite que um subconjunto de dados de um dataframe seja gerado.

```
# subconjunto baseado em condição lógica
ss1 <- subset(dados, datas == "2013-01-09", select = "tar")
ss1
#>   tar
#> 9  34
# subconjunto baseado em condição lógica
ss2 <- subset(dados, tar > 26 & prec > 0)
ss2
#>         datas      cidade tar prec
#> 14 2013-01-14 Santa Maria  29    2
# subconjunto baseado em condição lógica
ss3 <- subset(dados, tar > 26 | prec > 0)
ss3
#>         datas      cidade tar prec
#> 1  2013-01-01 Santa Maria  31    0
#> 2  2013-01-02 Santa Maria  35    0
#> 5  2013-01-05 Santa Maria  33    0
#> 6  2013-01-06 Santa Maria  17   10
#> 7  2013-01-07 Santa Maria  18   18
#> 8  2013-01-08 Santa Maria  16    4
#> 9  2013-01-09 Santa Maria  34    0
#> 10 2013-01-10 Santa Maria  27    0
#> 11 2013-01-11 Santa Maria  15    5
#> 12 2013-01-12 Santa Maria  28    0
#> 14 2013-01-14 Santa Maria  29    2
#> 15 2013-01-15 Santa Maria  32    0
# subconjunto baseado em condição lógica
ss4 <- subset(dados,
  datas %in% c("2013-01-09", "2013-01-13", "2013-01-15"),
  select = -cidade
)
ss4
#>         datas tar prec
#> 9  2013-01-09  34    0
#> 13 2013-01-13  22    0
#> 15 2013-01-15  32    0
# subconjunto baseado em condição lógica
ss4 <- subset(dados,
  !datas %in% c("2013-01-09", "2013-01-13", "2013-01-15"),
  select = -cidade
)
ss4
#>         datas tar prec
#> 1  2013-01-01  31    0
#> 2  2013-01-02  35    0
#> 3  2013-01-03  21    0
#> 4  2013-01-04  23    0
#> 5  2013-01-05  33    0
#> 6  2013-01-06  17   10
#> 7  2013-01-07  18   18
#> 8  2013-01-08  16    4
#> 10 2013-01-10  27    0
#> 11 2013-01-11  15    5
#> 12 2013-01-12  28    0
#> 14 2013-01-14  29    2
```

Para alterar, remover ou incluir variáveis num dataframe é possível usar a função específica `transform`. Normalmente ela é utilizada para alterar mais de uma variável simultaneamente.

```
# mudança do dataframe, alteração de várias variáveis
dados <- transform(dados,
  cidade = ifelse(1:nrow(dados) > 8, "Sao Sepe", cidade),
  datas = c(datas[1:8], datas[1:7]),
  anomalias = ifelse(cidade == "Santa Maria",
    tar - mean(tar[cidade == "Santa Maria"]),
    tar - mean(tar[cidade == "Sao Sepe"])
  )
)
dados
#>         datas      cidade tar prec anomalias
#> 1  2013-01-01 Santa Maria  31    0       5.6
#> 2  2013-01-02 Santa Maria  35    0       9.6
#> 3  2013-01-03 Santa Maria  21    0      -4.4
#> 4  2013-01-04 Santa Maria  23    0      -2.4
#> 5  2013-01-05 Santa Maria  33    0       7.6
#> 6  2013-01-06 Santa Maria  17   10      -8.4
#> 7  2013-01-07 Santa Maria  18   18      -7.4
#> 8  2013-01-08 Santa Maria  16    4      -9.4
#> 9  2013-01-01    Sao Sepe  34    0       8.6
#> 10 2013-01-02    Sao Sepe  27    0       1.6
#> 11 2013-01-03    Sao Sepe  15    5     -10.4
#> 12 2013-01-04    Sao Sepe  28    0       2.6
#> 13 2013-01-05    Sao Sepe  22    0      -3.4
#> 14 2013-01-06    Sao Sepe  29    2       3.6
#> 15 2013-01-07    Sao Sepe  32    0       6.6
# alterar só uma variavel, anomalia normalizada
dados$anomalias.norm <- ifelse(dados$cidade == "Santa Maria",
  dados$anomalias / sd(dados$anomalias[dados$cidade == "Santa Maria"]),
  dados$anomalias / sd(dados$anomalias[dados$cidade == "Sao Sepe"])
)
dados
#>         datas      cidade tar prec anomalias anomalias.norm
#> 1  2013-01-01 Santa Maria  31    0       5.6      0.7321669
#> 2  2013-01-02 Santa Maria  35    0       9.6      1.2551433
#> 3  2013-01-03 Santa Maria  21    0      -4.4     -0.5752740
#> 4  2013-01-04 Santa Maria  23    0      -2.4     -0.3137858
#> 5  2013-01-05 Santa Maria  33    0       7.6      0.9936551
#> 6  2013-01-06 Santa Maria  17   10      -8.4     -1.0982504
#> 7  2013-01-07 Santa Maria  18   18      -7.4     -0.9675063
#> 8  2013-01-08 Santa Maria  16    4      -9.4     -1.2289944
#> 9  2013-01-01    Sao Sepe  34    0       8.6      1.3392114
#> 10 2013-01-02    Sao Sepe  27    0       1.6      0.2491556
#> 11 2013-01-03    Sao Sepe  15    5     -10.4     -1.6195115
#> 12 2013-01-04    Sao Sepe  28    0       2.6      0.4048779
#> 13 2013-01-05    Sao Sepe  22    0      -3.4     -0.5294557
#> 14 2013-01-06    Sao Sepe  29    2       3.6      0.5606001
#> 15 2013-01-07    Sao Sepe  32    0       6.6      1.0277669
```

## Listas

Listas são um tipo de vetor. Porém, a lista é uma estrutura de dado mais versátil por três motivos:

- Os elementos podem ser objetos de diferentes tipos;
- Cada elemento pode ter um tamanho diferente;
- Os elementos podem conter estruturas de dados diferentes (como uma matriz e outro vetor).

Para criar uma lista, utiliza-se a função `list`. A especificação do conteúdo de uma lista é similar à função `c()`. Apenas separamos por vírgula os elementos da lista.

```
# lista de dados heterogêneos
lst <- list(
  # 4 vetores atômicos
  c(1L, 6L, 10L, NA),
  c(-1, 0, 1, 2, NA),
  c(FALSE, NA, FALSE, TRUE),
  c('ae', NA, "ou"),
  # uma lista com 2 elementos 
  list(0, 1)
)
lst
#> [[1]]
#> [1]  1  6 10 NA
#> 
#> [[2]]
#> [1] -1  0  1  2 NA
#> 
#> [[3]]
#> [1] FALSE    NA FALSE  TRUE
#> 
#> [[4]]
#> [1] "ae" NA   "ou"
#> 
#> [[5]]
#> [[5]][[1]]
#> [1] 0
#> 
#> [[5]][[2]]
#> [1] 1
```

A função `str` permite uma visualização rápida da estrutura de uma lista.

```
str(lst)
#> List of 5
#>  $ : int [1:4] 1 6 10 NA
#>  $ : num [1:5] -1 0 1 2 NA
#>  $ : logi [1:4] FALSE NA FALSE TRUE
#>  $ : chr [1:3] "ae" NA "ou"
#>  $ :List of 2
#>   ..$ : num 0
#>   ..$ : num 1
```

É possível criar listas aninhadas, isto é, uma lista que armazena outra lista. Através da função `is.recursive` é possível verificar se uma lista é aninhada.

```
is.recursive(lst)
## [1] TRUE
```

As listas podem ter nomes para seus componentes.

```
names(lst)
## NULL

names(lst) <- c("vetor_int", "vetor_dbl", "vetor_log", "vetor_char", "lista")

lst
## $vetor_int
## [1]  1  6 10 NA
## 
## $vetor_dbl
## [1] -1  0  1  2 NA
## 
## $vetor_log
## [1] FALSE    NA FALSE  TRUE
## 
## $vetor_char
## [1] "ae" NA   "ou"
## 
## $lista
## $lista[[1]]
## [1] 0
## 
## $lista[[2]]
## [1] 1
```

## Vetores

É uma estrutura de dados unidimensional, uma sequência de dados ordenada de elementos sem hierarquia interna.

Para criar um vetor, basta usar a função combine `c()`.

```
ex1 <- c(1, 5, 8)
ex1
## [1] 1 5 8
```

O que pode ser combinado em um vetor - coerção:

- Conversão de número em caractere `c(1, "a")`;
- Valor lógico para número, T vira 1 e F vira 0 `c(T, 0)`;
- Valor lógico para caractere, T vira "TRUE" e F vira "FALSE" `c("a", T)`.

Consideremos os vetores abaixo.

```
v1 <- c(1, 2, 3)
v2 <- c(2, 4, 6)
v3 <- 2
v4 <- c(2, 4, 6, 8)
```

Compare os resultados das expressões abaixo.

```
v1 * v2
# [1]  2  8 18
v1 * v3
# [1] 2 4 6
```

No primeiro caso, o primeiro elemento de v1 é multiplicado pelo primeiro elemento de v2, o segundo de v1 pelo segundo de v2 e assim por diante. No segundo caso, a operação de multiplicação é aplicada de forma distributiva, isto é, cada elemento de v1 é multiplicado pelo elemento único de v3.

Considere a expressão abaixo.

```
v1 * v4
# Warning in v1 * v4: comprimento do objeto maior não é múltiplo do comprimento do objeto menor
```

O problema é que o número de elementos não é o mesmo. Números precisam ser iguais ou um dos vetores precisa ser unitário. Outra possibilidade é que o vetor maior tenha um número de elementos que seja múltiplo do número de elementos do vetor menor.

```
v5 <- c(0, 1)
v4 * v5
# [1] 0 4 0 8
```

O resultado da operação sugere que o primeiro elemento de v5 multiplica o primeiro e o terceiro elementos de v4 e o segundo de v5 multiplica o segundo e o quarto de v4.

```
paste0(c("b", "n", "n"), c("a"))
# [1] "ba" "na" "na"

paste0(c("c", "l", "b", "r"), c("o", "a"))
# [1] "co" "la" "bo" "ra"
```

Para acessar os elementos de um vetor, bastar utilizar a notação `nome[indice]`, sendo que podem haver diferentes índices: `[1] ,[1:2], [c(1, 3, 4)]`.

As funções a seguir são funções importantes associadas à vetores.

`lenght` - para descobrir o tamanho de um tipo de dado.
`sum` - para somar os valores de um vetor.
`seq` - para gerar uma sequência de elementos.
