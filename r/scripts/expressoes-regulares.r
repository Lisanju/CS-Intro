# Programação para linguistas
# 2022-2
#
# Exemplo de uso de expressões regulares (regex)
#

help("regex")

# Carregamento de lista de palavras
pal <- read.delim("~/ensino/ufscar/ling-prog/regex/lista_petrus.txt", header=FALSE)

# Função `grep()` encontra padrões definidos pelo usuário
# Argumentos relevantes:
# - `pattern`: padrão a ser encontrado em um vetor.
# - `x`: vetor no qual o padrão será buscado.
# - `value`:
#     + `FALSE`, retorna índices das correspondências;
#     + `TRUE`, retorna os valores literais das correspondências.

# Palavras que contém o padrão literal "oo" em qualquer posição
grep("oo", x = pal$V1, value = TRUE)

# Teste com argumento `value = FALSE`
grep("oo", x = pal$V1, value = FALSE)

pal$V1[grep("oo", x = pal$V1, value = FALSE)]

# Representantes
# `.`: casa uma ocorrência de um caractere qualquer
grep("^p.tr.", x = pal$V1, value = TRUE)

# Lista: [] só casa ocorrências dos caracteres que ela contém.

# Palavras iniciadas por uma ocorrência dos caracteres na lista [ptcs],
# seguido de "í"
grep("^[ptcs]í", x = pal$V1, value = TRUE)

# Lista [pbf] seguido de [lr] e "a"
# [lr] têm que estar presentes
grep("^[pbf][lr]a", x = pal$V1, value = TRUE)

# Aqui, [lr] pode estar presente ou não
grep("^[pb][lr]?a", x = pal$V1, value = TRUE)

# "qu" seguido de uma das vogais em final de palavra
grep("qu[aeiou]$", x = pal$V1, value = TRUE)

# Agrupamento, indicado por ()
# Busca pela lista [bfp] ou "qu" seguidos de "a" em início de palavra
grep("^([bfp]|qu)a", x = pal$V1, value = TRUE)

# Quantificadores ----
# Aplicam-se ao caractere que o antecede

# `?`: opcional (zero ou uma ocorrência)
grep("me[s]?$", x = pal$V1, value = TRUE)

# `+`: uma ou mais ocorrências
# Palavras que têm "ps", "t", "c" e "s"
# entremeadas por pelo menos um caractere
grep("^ps.+t.+c.+s", x = pal$V1, value = TRUE)

# `{m,n}`: de m a n ocorrências
# Palavras que têm entre três e quatro ocorrências
# de "t" entremeadas exatamente por um caractere
grep("(t.){3,4}", x = pal$V1, value = TRUE)

# Igual ao anterior, mas agora as três ou quatro ocorrências
# de "t" podem ser entremeadas por um ou mais caracteres
grep("(t.+){3,4}", x = pal$V1, value = TRUE)

# `*`: o item anterior será casado zero ou mais vezes
# Palavras em que há exatamente duas ocorrências de "p"
# mas pode não haver nenhum caractere entre eles.
grep("(p.*){2}", x = pal$V1, value = TRUE)
