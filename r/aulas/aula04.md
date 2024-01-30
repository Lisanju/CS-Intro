# Estruturas de controle do fluxo de execução

## Estruturas condicionais

## If

O `if` permite executar um código caso uma condição especificada pelo programador seja cumprida, ignorando um resultado falso.

```
x <- 30
if (x == 30) {
  res <- "Número igual a 30"
  print(res)
}
```

## Else

Caso `else` seja adicionado no código, se a condição especificada retornar um resultado falso, é executado o código especificado após `else`.

```
x <- 30
if (x == 30) {
  res <- "Número igual a 30"
} else {
    res <- "Número diferente de 30"
  }
print(res)
```

Note que o `else` deve ser localizado na mesma linha que a chave do `if`, se não o script não funcionará.

## Else if

Caso seja necessário verificar condições sucessivamente, é possível utilizar `else if`. É um encadeamento de estruturas de condições em um script.

```
x <- 30
if (x == 30) {
  res <- "Número igual a 30"
} else if (x > 30{
    res <- "Número maior que 30"
  } else {
      res <- "Número menor que 30"
    }
print(res)
```

## Estruturas de repetição

## While

A estrutura `while` realiza um teste lógico de repetição, em que caso a condição especificada pelo programador seja verdadeira o código continuará executando um bloco de código.

Quando o teste retornar falso, a repetição é interrompida.

```
x <- 1
while(x <= 10) {
  print(x)
  x <- x + 1
}
```

## For

A estrutura de repetição `for` permite que a gente execute um loop de código em casos onde sabemos de antemão o número de repetições que devem ser realizadas. Para isso, especificamos o intervalo de repetições em `for`.

```
for (i in 1:10) {
  print(i)
}
```

## Repeat e Break

O `repeat` executa sucessivamente um código até ser interrompido pelo comando `break`.

```
x = c(11:13) 
soma = 0 # inicia a variável soma com 0
n = length(x) # n recebe o valor do comprimento do vetor x, no caso n = 3
i = 1
repeat { # executa os comandos entre {} enquanto i for menor ou igual a n
  soma = soma + x[i]
  print(paste("i = ", i, ",  x[", i, "] = ",x[i], ", soma = ",soma, sep=''))
  i = i + 1
  if (i > n) { # quando i > n, o comando break é executado 
    break      # e o laço é interrompido
  }
}
## [1] "i = 1,  x[1] = 11, soma = 11"
## [1] "i = 2,  x[2] = 12, soma = 23"
## [1] "i = 3,  x[3] = 13, soma = 36"

soma
## [1] 36
```

O fluxo do laço `repeat` é parecido com o `while`, a diferença está em que para `repeat` a condição é testada em qualquer ponto do laço, não antes da execução do laço. O comando `break` interrompe a execução do código assim que for executado.

## Next

O comando `next` é usado para interromper uma iteração de um laço.

```
x = c(10:30)
n = length(x)
soma = 0
for (i in 1:n) {
  if (i < 11) {
       next
  }
  soma = soma + x[i]
  print(paste("i = ", i, ",  x[", i, "] = ", x[i], ", soma = ",
              soma, sep='')) 
}
## [1] "i = 11,  x[11] = 20, soma = 20"
## [1] "i = 12,  x[12] = 21, soma = 41"
## [1] "i = 13,  x[13] = 22, soma = 63"
## [1] "i = 14,  x[14] = 23, soma = 86"
## [1] "i = 15,  x[15] = 24, soma = 110"
## [1] "i = 16,  x[16] = 25, soma = 135"
## [1] "i = 17,  x[17] = 26, soma = 161"
## [1] "i = 18,  x[18] = 27, soma = 188"
## [1] "i = 19,  x[19] = 28, soma = 216"
## [1] "i = 20,  x[20] = 29, soma = 245"
## [1] "i = 21,  x[21] = 30, soma = 275"
```

No laço acima, enquanto i < 11, o comando next é executado, interrompendo a iteração corrente e indo para o início da próxima iteração. Então, para i = 1, 2, até 11, os dois comandos após o if não são executados.
