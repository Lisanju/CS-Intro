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

