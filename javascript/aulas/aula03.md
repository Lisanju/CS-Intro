# Eventos em JavaScript

Nesta aula, o recurso de eventos em JavaScript é apresentado, sendo importante para o desenvolvimento de páginas web interativas.

## Eventos

Um evento é o método utilizado pelo desenvolvedor para tornar a página mais responsiva e próxima de aplicativos tradicionais.

Diversos eventos podem ser executados sobre elementos HTML diferentes.

A comunicação entre o HTML e o JavaScript é feita, geralmente, através de um seletor.

## Seletores
```
<div id="primeiroDiv" class="texto">
  <h1>Primeiro título</h1>
  <p>Primeiro parágrafo de texto de exemplo</p>
</div>

<div id="segundoDiv" class="texto">
  <h1>Segundo título</h1>
  <p>Segundo parágrafo de texto de exemplo</p>
</div>
```

Dado o código HTML acima, é possível usar os seguintes seletores em JavaScript:

`var div = document.getElementById("primeiroDiv");` - Pelo Id.

`var div = document.getElementsbyTagName("p")[1];` - Pela tag. Note que o `[1]` se refere à segunda tag `<p>` (a contagem começa do 0).

`var div = document.getElementsByClassName("texto")[0];` - Pela classe.

Além dos seletores de elementos HTML, pode-se percorrer a árvore DOM seguindo o relacionamento de parentesco de pai, filho, irmão etc.

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/635eb126-72f3-40fb-97b6-0c7b09a9526c)

```
var x = document.getElementById("id");
                                                    // Retornam inclusive nós vazios (undefined)
x.parentNode;      // Pai do nó selecionado
x.nextSibling;     // Próximo irmão
x.previousSibling  // Irmão anterior
x.childNodes;      // Retorna lista de filhos
                                                                // Retornam apenas nós válidos (que estejam dentro de tags)
x.parentElementl           // Elemento pai do nó selecionado
x.nextElementSibling;      // Próximo elemento irmão
x.previousElementSibling;  // Elemento irmão anterior
x.children;                // Retorna a lista de elementos filhos
```

A interação do usuário dá origem aos eventos. Alguns eventos comuns são o Click, DoubleClick, MouseOver e Keypress.

A lista a seguir contém vários eventos: https://developer.mozilla.org/en-US/docs/Web/Events

