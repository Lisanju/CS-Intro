# Funções e Arrays

Nesta aula, será apresentada a variável do tipo Array, um importante recurso presente na linguagem JavaScript. Além disso, serão apresentadas funções em JavaScript, que são um conjunto de instruções que funcionam como subprogramas.

## Funções

O JavaScript, assim como a maioria das linguagens modernas, suporta a criação de funções.

Uma função é, grosso modo, um conjunto de instruções que são executadas sistematicamente dado um conjunto de parâmetros, podendo ou não retornar algum valor. Uma função pode ser vista como um subprograma.

Funções que não retornam nenhum valor são chamadas também de procedimentos (procedure).

Uma função pode conter uma ampla gama de instruções, como:
- Declaração de variáveis;
- Atribuição, cálculo e operações matemáticas e lógicas sobre as variáveis;
- Laços de repetição e condicionais diversos;
- Especificação e construção de objetos;
- Especificação de funções internas...

Existem diferentes formas de criar uma função, as duas principais são por declaração e por expressão.

```
function areaDoCirculo(raio){      // Por declaração
  return Math.PI * raio**2;
};

areaDoCirculo(10.134);
```

```
var areaDoCirculo = function(raio){  // Por expressão
  return Math.PI * raio**2;
};

areaDoCirculo(10.134);
```

## Função Arrow

Há também uma versão reduzida de especificar funções, chamada de arrow function.

Tem quase todos os recursos de uma função normal, com exceção de recursos como this, construtores e similares.

Introdução na linguagem JavaScript recentemente (ES6 - ECMAScript 2015).

```
let a = 10;
let b = 20;

var somatorio = function(a,b){               // Função por expressão
  return a + b;
}
console.log(somatorio(a,b));  // Imprimirá 30

var outrasoma = (a,b) => {return a + b};    // Função arrow
console.log(outrasoma)  // Imprimirá 30
```

Note que, caso haja apenas uma instrução na função, não é necessário o comando return `var outrasoma = (a,b) => { a + b }`.

- Uma função pode ser utilizada como parâmetro de outras funções.
- Uma função pode ser declarada dentro de outra função.
- Para retornar múltiplos valores, é preciso usar um array.

## Arrays

Arrays são vetores, também chamados de listas. São recursos importantes para qualquer linguagem de programação moderna.

O objetivo do vetor é o de armazenar um número qualquer de informações em uma única variável.

```
var vetor = Array();
vetor[0] = "IFSP";
vetor[1] = "JavaScript";
vetor[2] = 2019;
vetor[3] = true;
vetor[4] = Array();
vetor[5] = 1.4567;

//ou

var vetor = Array("IFSP", "JavaScript", 2019, true, Array(), 1.4567);

//ou

var vetor = ["IFSP", "JavaScript", 2019, true, Array(), 1.4567];
```

## Iteração

Podemos iterar sobre o vetor de diversas formas. O método mais básico é usando o length do vetor em um laço de repetição como o for.

```
var vetor = [1,2,3,4];

for(var i = 0; i < vetor.length; i++){
  console.log(vetor[i]);  // 1, 2, 3, 4
```

Outra forma de iteração é usando o IN:

```
var vetor = ["a", "b", "c", "d"];

for (valor in vetor){
  console.log(valor);  //1, 2, 3, 4 --> Não é retornado o valor da posição do vetor, mas sim o índice da posição
}
```

Uma forma de iterar sobre os valores é usando a operação OF:

```
var vetor = ["a", "b", "c", "d"];

for (valor of vetor){
  console.log(valor);  //a, b, c, d
}
```

## Manipulação de Arrays

Para adicionar um novo índice e valor no final do vetor `vetor.push()`, e no início `vetor.unshift()`.

```
var vetor = ["Banana", "Abacaxi", "Uva"];

vetor.push("Melão");    // É adicionado um índice 3 com o valor "Melão"

vetor.unshift("Melão");  // O valor "Melão" ocupa o índice 0 e todos os outros valores pulam um índice para frente.
```

Para remover do final `vetor.pop()` (e retorna o valor removido), e do início `vetor.shift()` (e retorna o valor removido).

`retorno = vetor.splice(indice_inicio, quantos_remover);`

É utilizado para remover vários elementos sequenciais do vetor. Em que `indice_inicio` é o índice do primeiro elemento a ser removido e `quantos_remover` é o número de elementos que devem ser removidos (é opcional, se não for especificado, removerá até o último elemento). Retorna os elementos que foram removidos como array.

## Atribuição

Para evitar atribuição por referência, deve-se copiar dos dados do vetor. Para isso, usa-se o `slice`.

`var novoVetor = vetorAntigo.slice();`

## Outros métodos úteis

```
var palavras = "Eu gosto muito de estudar".split(" ");
console.log(palavras);  // "Eu", "gosto", "muito", "de", "estudar"

var novaFrase = palavras.join("-");
console.log(novaFrase);  // "Eu-gosto-muito-de-estudar"
```

- `vetor.reverse();` - Reverte o vetor.
- `vetor.sort();` - Ordena o vetor.
- `vetor.indexOf(valor);` - Retorna o índice do primeiro elemento 'valor', ou -1 se não existir.
- `vetor.lastIndexOf(valor);` - Retorna o índice do último elemento 'valor', ou -1 se não existir.
- `vetor.includes(valor);` - Retorna true se 'valor' existir no vetor, ou false caso contrário.

