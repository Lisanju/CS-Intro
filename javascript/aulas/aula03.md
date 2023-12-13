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

`<a href = "#" onClick = "alert("Cliquei nesse link")">Link teste</a>` - É uma maneira simples de adicionar eventos, porém de manutenção dificultada.

```
<body>
  <p>Um parágrafo de texto de exemplo</p>
  <script type="text/javascript">
    document.getElementsByTagName("p")[0].onClick = function(){
      alert("Cliquei no parágrafo");
      };
  </script>
</body>
```

A maneira acima é de mais fácil manutenção.

```
<head>
  <meta charset="utf-8">
  <title>Página de teste</title>
  <script type="text/javascript">
    window.onload = function(){
    document.getElementsByTagName("p")[0].onClick = function(){
      alert("Cliquei no parágrafo");
    };
  </script>
</head>
<body>
  <p>Um parágrafo de texto de exemplo</p>
</body>
```

O código acima não funciona. Para ele funcionar, é necessário acrescentar `window.onload` no `<script>`. Ele execut após todos os elementos HTML estiverem carregados.

```
<head>
  <meta charset="utf-8">
  <title>Página de teste</title>
  <script type="text/javascript">
    window.onload = function(){
      document.getElementsByTagName("p")[0].onClick = function(){
        alert("Cliquei no parágrafo");
      };
    };
  </script>
</head>
<body>
  <p>Um parágrafo de texto de exemplo</p>
</body>
```

Para ter uma maior flexibilidade, é possível usar um objeto do tipo evento como parâmetro.

```
document.getElementsByTagName("p")[0].onClick = function(evento){
  alert(evento.type);
}
```

- `type` - Retorna o tipo de evento que foi disparado (Click, MouseOver etc).
- `target` - Retorna o objeto ao qual o evento está atrelado.
- `preventDefault():` - Cancela o comportamento padrão do evento.

Para modificar uma propriedade CSS de um elemento selecionado:

`elemento.style.fontSize = "10px";`

Em que `style` altera o CSS do `elemento`, `fontSize` é o nome da propriedade CSS e `10px` é o novo valor da propriedade.

`getComputedStyle(elemento)["propriedae"];`

Em que `getComputedStyle(elemento)` retorna todos os valores dos estilos como um array e `propriedade` é a propriedade CSS desejada.
