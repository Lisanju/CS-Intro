# Dataframes, Arrays e Vetores

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

