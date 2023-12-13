# Conceitos iniciais em JavaScript

Nesta aula, serão apresentados fundamentos ao desenvolvimento web com JavaScript, como variáveis, laços condicionais e de repetição e interação com usuários.

## Código-fonte

É possível colocar o código-fonte diretamente no arquivo HTML ou em um arquivo externo (declaração externa).

```
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <script type="text/javascript">
    ...
    </script>
  </head>
  <body>
    <script type="text/javascript">
    ...
    </script>
  </body>
</html>
```

- O código-fonte pode aparecer diretamente no `<head>` ou no `<body>`.

```
<head>
  <meta charset="utf-8">
  <title>Página de teste</title>
  <script src="arquivoExterno.js"></script>
</head>
```

- No caso de uma declaração externa, o diretório deverá ser especificado no `<head>`.

A tag `<script>` pode ser declarada diversas vezes no código e os valores declarados em cada bloco de código são globais. Pode-se misturar declarações no código HTML com declarações externas.

## Comentários

```
<script type="text/javascript">
  //Este é um comentário

  /*
    Este comentário
    tem várias
    linhas
  */
</script>
```

## Variáveis

- Não devem possuir caracteres especiais, acentos ou espaços;
- Diferenciam maiúscula de minúscula;
- Aceita os caracteres especiais $ e _;
- camelCase (contadorRegressivo, numVarBol, ...).

`var nomeDaVariavel = 10;`

- var - Palavra reservada para variáveis;
- ; - Opcional no final de cada declaração de variável;
- 10 - Atribuição de valor (no caso, do valor 10).

## Tipos de variáveis

Cada variável JavaScript pode ser:
- Boolean
- null
- undefined
- Number
- String
- Symbol
- Object

```
<script type="text/javascript">
  var nome;            // Undefined
  nome = "Elisa";      // String
  var idade = 10;      // Número
  idade = nome;        // String
  var verdade = true;  // Booleano
  var falso = false;   // Booleano
  var x1 = 10, x2;     // Declaração composta
  var pi = 3.1416;     // Número
  var nulo = null;     // Nulo
</script>
```

## Operadores aritméticos

- `+` - Soma (ou concatenação);
- `-` - Subtração;
- `*` - Multiplicação;
- `/` - Divisão;
- `**` - Potência;
- `%` - Resto da divisão (ex: 5%2=1);
- `++` - Incremento;
- `--` - Decremento;
- `=` - Atribuição.

### Detalhes

Todos os números são representados em ponto flutuante.

Não há caracteres. Um caractere é uma string com tamanho 1.

