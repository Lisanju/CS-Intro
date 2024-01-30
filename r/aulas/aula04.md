# Estruturas condicionais e de repetição

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

