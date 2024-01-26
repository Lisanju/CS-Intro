# Programação para linguistas
# 2022-2
#
# Estruturas de repetição: repeat, while, for

segredo <- "a"
vogais <- c("a", "e", "i", "o", "u")

# `repeat` ----

set.seed(123)
repeat {
    palpite <- sample(vogais, 1)
    print(palpite)
    if (palpite == segredo) {
        break
    }
}

# Falar sobre `set.seed()` e reprodutibilidade dos resultados
# Explorar:
# - Rodar algumas vezes o código sem `set.seed()`.
# - Testar valores diferentes de `set.seed()`.

# `while` ----

set.seed(123)
palpite <- sample(vogais, 1)
while(palpite != segredo) {
    print(palpite)
    palpite <- sample(vogais, 1)
    if (palpite == segredo) {
        print(palpite)
    }
}

# Comentário:
# Resultados parecidos, embora com algumas diferenças:
# 1. `while` exige que palpite seja gerado duas vezes.
# 2. palpite correto não é impresso no console (poderia
#    ser resolvido com um `if (palpite == segredo) print(palpite)`.
# 3. não exige `break` para evitar a repetição infinita.

# * Versão sem repetição de palpite errado ----

set.seed(123)
vogais <- c("a", "e", "i", "o", "u")
repeat {
    palpite <- sample(vogais, 1)
    if (palpite != segredo) {
        message("Errou! A vogal não é <", palpite, ">.")
        vogais <- vogais[-which(vogais == palpite)]
    } else {
        message("Acertou! A vogal é <", palpite, ">.")
        break
    }
}

## * Versão sem `break` ----
set.seed(123)
vogais <- c("a", "e", "i", "o", "u")
palpite <- sample(vogais, 1)
while(palpite != segredo) {
    message("Errou! A vogal não é <", palpite, ">.")
    vogais <- vogais[-which(vogais == palpite)]
    palpite <- sample(vogais, 1)
    if (palpite == segredo) {
        message("Acertou! A vogal é <", palpite, ">.")
    }
}

## * Versão com `break` ----
set.seed(123)
vogais <- c("a", "e", "i", "o", "u")
while(length(vogais) > 0) {
    palpite <- sample(vogais, 1)
    if (palpite != segredo) {
        vogais <- vogais[-which(vogais == palpite)]
        message("Errou! A vogal não é <", palpite, ">. Vogais restantes: ", vogais)

    } else {
        message("Acertou! A vogal é <", palpite, ">.")
        break
    }
}

# `for` ----

# Define de antemão o número de repetições a serem realizadas
# Elementos da construção:
# - Uma variável contadora.
# - Um vetor com uma sequência de elementos
#
# O número de repetições é o tamanho ou número de elementos no vetor
#
# O vetor pode ser de qualquer tipo de dado.

for(i in 1:5) message("i = ", i)

for(i in 1:5)
{
    j <- i ^ 2
    message("j = ", j)
}

for (i in 1:length(vogais)) {
    message("A vogal ", i, " é ", vogais[i])
}

for (i in vogais) {
    print(i)
}

for (i in c(T, F, T, T, F)) {
    print(i)
}

pal <- c("casa", "ônibus", "verde", "ela")
for (i in pal) {
    print(i)
}

tam <- c()
j <- 1
for (i in pal){
    tam[j] <- nchar(i)
    j <- j + 1
}
tam


# Exemplo de `for` trabalhando em um data.frame

turma <- data.frame(
    nome = c("Alice", "Beto", "Mariana", "Pedro", "Vanessa"),
    prova1 = c(8, 7, 6, 9, 7),
    prova2 = c(9, 6, 5, 3, 7),
    prova3 = c(7, 8, 8, 7, 8)
)

for (aluno in 1:nrow(turma)) {
    pessoa <- turma[aluno, 1]
    notas <- as.numeric(turma[aluno, 2:4])
    message(pessoa, ": média ", mean(notas))
}
