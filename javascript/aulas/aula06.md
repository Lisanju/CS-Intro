# Manipulação DOM

Um dos recursos mais utilizados do JavaScript, além do controle de eventos, é o de manipular a árvore DOM (o "HTML" da página).

Com esses recursos é possível criar uma página inteira do zero, modificar elementos da tela, adicionar ou remover novas tags do usuário, esconder tags etc.

## Como modificar o conteúdo de uma tag HTML

Essa tag pode já estar inserida no HTML, precisando ser selecionada/referenciada usando um dos seletores de elementos já vistos antes. Ou ainda é possível modificar um elemento HTML em memória, que ainda não foi inserido na árvore DOM.

```
var elemento = document.getElementsByTagName("div")[0];
elemento.innerHTML = "Novo conteúdo do elemento";
```

O `.innerHTML` modifica o conteúdo interno do elemento selecionado, considerando as tags HTML.

```
var elemento = document.getElementsByTagName("div")[0];
elemento.innerText = "Novo conteúdo do elemento";
```

O `.innerText` modifica o conteúdo interno do elemento selecionado, não considerando as tags HTML.

```
var elemento = document.getElementsByTagName("input")[0];
elemento.value = "Novo conteúdo do input";
```

O `.value` é usado para manipular o conteúdo de tags usadas em formulários (input, select, textarea, etc).

Com os recursos de innerText, innerHTML e value, temos o controle do conteúdo interno de qualquer elemento HTML. Sendo possível alterar o conteúdo textual de um parágrafo, mudar o texto de um botão, ler e modificar o conteúdo de um campo input e coisas do tipo.

Porém, além do conteúdo, podemos querer manipular os atributos dos elementos HTML, isso é, qualquer um de seus detalhes de configuração (class, id, min, max, required, type, name, value, href, etc).

```
var elemento = document.getElementsByTagName("div")[0];
elemento.setAttribute("id","nana");
```

O `.setAttribute(atributo, valor)` modifica o atributo para o elemento selecionado. Se o atributo não existe, ele é criado.

```
var elemento = document.getElementsByTagName("div")[0];
elemento.getAttribute("id");
```

O `.getAttribute(atributo)` retorna o valor do atributo selecionado. Caso o atributo não exista, ele retorna NULL.

## Como modificar o conteúdo de uma folha de estilo CSS

Além do conteúdo e dos atributos, outro componente que forma a árvore DOM de uma página é a sua folha de estilos CSS. Podemos modificar qualquer propriedade CSS para todo elemento HTML.

```
var elemento = document.getElementsByTagName("p")[0];

// Muda o background-color para vermelho
elemento.style.backgroundColor = "red";

// Muda a cor da fonte para branca
elemento.style.color = "white";

// Aumenta o tamanho da fonte em 5px
// Primeiro, usando o getComputedStyle recupera o valor CSS correto do elemento
// Segundo, usa o parseInt para converter '16px' para '16'
// Por fim, adiciona 20 a esse número e concatena com a string 'px'.
elemento.style.fontSize = parseInt(getComputedStyle(elemento)["font-size"]) + 20 + "px";

// Imprime no console o valor do 'background-color' do elemento.
console.log(getComputedStyle(elemento)["background-color"]);
```

## Elementos criados em memória

Um elemento criado em memória pode ser modificado como um elemento qualquer: adicionar/modificar/remover seus atributos, estilos ou filhos. Mas é importante lembrar que o elemento criado só será exibido ao usuário depois de ser adicionado na árvore DOM pela função `appendChild`.

`var novoParagrafo = document.createElement("p");` cria um novo elemento HTML (p);

`novoParagrafo.innerText = "Novo parágrafo";` modifica o conteúdo textual do parágrafo;

`document.body.appendChild(novoParagrafo);` adiciona o novoParagrafo no `<body>` da página.
