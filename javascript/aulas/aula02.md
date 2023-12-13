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

## Laços de repetição

For, While e Do While.
```
for(i = 0; i < 12; i++){                    //(inicialização; condição; incremento)
  console.log("Iteração número " + i);
}

var contador=0;
while(contador < 12){
  console.log("Iteração número " + contador);
  contador++;
}

var contador = 0;
do{
  console.log("Iteração número " + contador);
  contador++;
} while (contador < 12);
```

## Interação com o usuário

`alert("Teste de algoritmo");`

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/0affc1f8-00b9-493b-9dff-a0573f5dd62e)

```
var resp = confirm("Você está entendendo?");
if(resp === true){
  console.log("Entendi");
}
else{
  console.log("Não entendi");
}
```

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/58d2f5e0-c1af-4293-ba01-947d308d02a3)

```
var nome = prompt("Qual é o seu nome?, "João");     // "João" é um valor padrão opcional
if(nome != null){
  alert("Olá " + nome);
}
```

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/b0751c69-9e54-45d6-b9cb-336c7afa291e)

## var e let
Além do var, uma variável ainda pode ser declarada como let

`var valor = 10;` e `let valor = 10;`

A diferença é o alcance do escopo de cada variável:
- Variáveis declaradas como let são consideradas de escopo limitado (chamado de escopo em bloco);
- Variáveis declaradas como var possuem escopo global. Com içamento de variável.

## Içamento de variável

Variáveis identificadas como var são içadas ao começo do código independentemente de onde estavam.

```
<script>
  x = 10;      //Funciona!
  var x;
</script>
```

```
<script>
  x = 10;      //Não funciona :(
  let x;
</script>
```

```
var x = 10;
if(x > 0){
  var y = "Oi";
}
console.log(x); // 10
console.log(y); // "Oi"

var x = 10;
if(x > 0){
  let x = "Oi";
}
console.log(x); // 10

var x = 10;
if(x > 0){
  let y = "Oi";
}
console.log(x); // 10
console.log(y); // Erro
```

## const

Variáveis podem ser declaradas como tipo const. Possuem escopo limitado (assim como o let), devem ser atribuídos um valor e não podem ser modificados, mas somente lidos.

```
var x = 10;
if(x > 0){
  const y = "Oi";
}
console.log(x); // 10
console.log(y); // Erro

const x = 10;
if(x > 0){
  x = "Oi"; // Erro
}

const x; // Erro
```
