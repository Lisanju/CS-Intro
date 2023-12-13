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

## Concatenação de strings

Como o operador `+` é usado tanto para soma quanto para concatenação entre strings, o JavaScript adota como padrão que, caso `+` apareça entre uma string e um número, a partir desse momento, todos os `+` seguintes no mesmo nível de prioridade serão considerados como concatenação.

## Laços condicionais

If, Else If e Else.
```
var idade = 10;
if(idade < 13){
  console.log("Acesso negado");
}
else if(idade < 18){
  console.log("Acesso limitado");
}
else{
  console.log("Acesso ilimitado");
}
```

Switch (case, default e break).
```
var cidade="SPO";
switch(cidade){
  case "CAM":
    alert("Campinas");
    break;
case "SPO":
    alert("São Paulo");
    break;
case "SCL":
    alert("São Carlos");
    break;
default:
    alert("Não reconhecido");
    break;
}
```

Há dois pares gêmeos de comparadores de igualdade e desiguladade, o par restrito e o par com conversor de tipo.

- Conversor de tipo - `==` e `!=`, se as variáveis sendo comparadas são iguais, eles se comportam normalmente. Mas caso sejam de tipos diferentes, os tipos são convertidos.
- Restrito - `===` e `!==`, não realizam conversão de tipo, funcionam como todas as demais linguagens.

```
var str = "10";
str == 10 // convertido -> true!
```

Mas cuidado, pois há casos onde a conversão de tipo pode dar resultados inesperados.

```
"" == false;
"0" == 0
"" == 0
```

Todas as comparações acima não são válidas (não são iguais) caso seja usado o comparador estrito.

## Operadores lógicos

- `<` - Menor que;
- `>` - Maior que;
- `<=` - Menor/igual que;
- `>=` - Maior/igual que;
- `==` - Igual (com conversão de tipo);
- `!=` ou `<>` - Diferente (com conversão de tipo);
- `===` - Igual (sem conversão de tipo);
- `!==` - Diferente (sem conversão de tipo);
- `&&` - Operação AND lógica;
- `||` - Operação OR lógica;
- `!` - Operação NOT lógica.

