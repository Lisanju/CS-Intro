# Dataframes, Arrays e Vetores

## Dataframe

Um dataframe é uma estrutura de dado adequada para uso estatístico. Funciona como uma planilha de dados, formado por colunas que podem armazenar variáveis de diferentes tipos.

```
vog.df <- data.frame(pos=c(1, 2, 3), dur=c(103.288, 143.24, 89.54), car= c("e", "a", "o"), ton=c(F, T, F))
```

É possível observar o conteúdo de um dataframe invocando a variável que o armazena.

```
vog.df
#   pos     dur car   ton
# 1   1 103.288   e FALSE
# 2   2 143.240   a  TRUE
# 3   3  89.540   o FALSE
```
