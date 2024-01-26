# Programação para linguistas
#
# Tópico: Entrada e saída de dados (E/S) - Input/Output (I/O)

# Carregar bibliotecas necessárias
# Instalar a biblioteca antes, caso isso não tenha sido feito antes
library(stringr)

# Mudar o diretório de trabalho para o diretório onde você colocou os
# arquivos .txt que usaremos no código a seguir.
#
# Lembrete! Caminhos para diretórios no Windows são expressos da seguinte forma:
#
# - "C:\\diretorio\\subdiretorio\\"
# - "C:/diretorio/subdiretorio/"
setwd("~/ensino/ufscar/ling-prog/io/")

# Função `scan()` ----

## `what = "character"`: o material a ser lido é composto por texto (caracteres)
## `sep="\n"`: quebra de linha `\n` é usado como elemento separador, cada elemento do vetor é um "parágrafo".
## `strip.white = TRUE`: linhas vazias (sem texto, linhas "puladas") são ignoradas

quincas <- scan(file="quincas_borba.txt", what="character", sep="\n", strip.white = TRUE)
head(quincas, 10)

## `file = `: pode ser também uma URL válida.
## Tentar "https://www.gutenberg.org/ebooks/3333.txt.utf-8"
## "Luís de Camões - Os Lusíadas"

# `sep = ""`: Cada elemento do vetor é uma sequência separada por espaço no arquivo-fonte.
# Nesse caso, cada elemento é uma palavra.
quincas2 <- scan(file = "quincas_borba.txt", what = "character", sep = "")
head(quincas2, 20)

# Usar a função `gsub()` para eliminar todos os caracteres que não sejam
# letras `a-zA-Z`, letras com diacríticos `\u00C0-\u00FF` e o hífen `-`.
quincas_palavras <- gsub(
    pattern = "[^a-zA-Z\u00C0-\u00FF-]",
    replacement = "",
    x = quincas2
    )
head(quincas_palavras, 20)

# Elimina elementos vazios no vetor `""`
quincas_palavras_limpas <- quincas_palavras[quincas_palavras != ""]
head(quincas_palavras_limpas, 20)

# Converte caracteres para caixa baixa
quincas_palavras_baixa <- tolower(quincas_palavras_limpas)
head(quincas_palavras_baixa, 20)

# Gera tabela de frequencia das palavras no vetor
quincas_freq_pal <- table(quincas_palavras_baixa)

# 50 palavras mais frequentes
quincas_freq_100 <- head(sort(quincas_freq_pal, decreasing = T), 100)

# Transforma a tabela em um `data.frame`
quincas_df <- data.frame(
    palavra = names(quincas_freq_100),
    frequencia = as.numeric(quincas_freq_100)
)

# Podemos dividir o texto em "frases" ao invés de "parágrafos".
# Usamos como delimitadores para identificar frases sinais de pontuação:
# ponto final, três pontos, ponto e vírgula, exclamação e interrogação.

## Juntamos todo o texto em um vetor com uma só posição
quincas3 <- paste(quincas, collapse = " ")
length(quincas3)
## Agora separamos o texto completo em "frases" usando os sinais de
## pontuação como delimitadores.
## A biblioteca `stringr` precisa estar instalada.
quincas_frases <- stringr::str_split_1(quincas3, pattern = "[\u2014.;!?]+")
head(quincas_frases, 30)

## Elimina espaços em branco no início e fim de cada elemento do vetor
quincas_frases_limpo <- trimws(quincas_frases)
head(quincas_frases_limpo, 30)

# Arquivo de dados estruturado (formato tabular)
#
# Função `read.delim()` ----

# Dados em formato tabular
# - Explorar o comando "Import Dataset" disponível na aba "Environment"
# do RStudio.
# - Caixas de seleção na janela correspondem a alguns dos argumentos da
# função `read_delim()`.
tabela <- read.delim("epentese.txt")

# Função `write.table()` ----

write.table(x = quincas_df,
            sep = "\t",
            file = "quincas_freq.txt",
            quote = FALSE,
            row.names = FALSE
            )
