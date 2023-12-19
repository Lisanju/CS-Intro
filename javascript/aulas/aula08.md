# jQuery

É uma biblioteca JavaScript que visa a simplificação na manipulação do DOM, nas chamadas de AJAX e no gerenciamento de Eventos. É muito utilizado por desenvolvedores de JavaScript.

Para usá-lo, basta adicionar o seguinte comando no `<head>` de seu site:

```
<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.slim.min.js">
</script>
```

## Princípio básico

Basicamente cada comando jQuery possui o seguinte formato:

`$(seletor).ação();`

Em que "seletor" indica qual elemento HTML ou CSS se refere e a ação ao o que deve acontecer.

### Seletores

O jQuery suporta uma ampla gama de seletores, similar ao CSS em si:

```
$("div"); // Todos os divs da página

$(".azul"); // Todos os elementos com classe 'azul'

$("#primeiro"); // Elemento com id 'primeiro'

$("div p"); // Todos os 'p' filhos de algum 'div'

$("div[id]"); // Todos os 'div' que possuam o atributo 'id'

$("[name=teste]"); // Todos os elementos com a atributo 'name' que tenha valor 'teste'

$("div p:first-child"); // Todos os primeiros 'p' que sejam filhos de um 'div'
```

### window.onload

É um comando padrão do JavaScript, permite forçar o navegador a executar um trecho de código após a página estar carregada.

Porém, essa funções possui seus vícios:
- A função é executada apenas após o conteúdo estiver totalmente carregado (o que acontece se a página demorar para estar pronta?);
- Cada navegador pode implementar a operação da forma que quiser;
- Em alguns casos, `window.onload` é desnecessariamente lento.

Para lidar com isso, em jQuery é possível usar:

```
$(document).ready(function(){
  /* Código a ser executado após
      o carregamento da página
  */
});
```

Um código base para o uso do jQuery pode ser visto a seguir:

```
<!DOCTYPE html>
<html lang='pt-br'>
  <head>
    <meta charset='utf-8'>
    <title>Título</title>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script>
      $(document).ready(function () {
        /* Código a ser executado após
            o carregamento da página
        */
      });
    </script>
  </head>
  <body>
  </body>
</html>
```

## Eventos

O JavaScript suporta a especificação de eventos sobre os elementos.

```
$("#submeter").click(function(e){
});

$("body").on("click", "#submeter", function(e){
});
```

Todos os eventos são suportados:

```
$("#submeter").mouseover(function(e) {...});
$("#submeter").dblclick(function(e) {...});
$("#submeter").keypress(function(e) {...});
$("#submeter").mouseenter(function(e) {...});
```

Mas como identificar qual o elemento específico que causou o evento executado? Para isso, há duas opções:

1. Usando JavaScript puro

```
$("button").click(function(e) {
  e.target; // Objeto que causou o evento...
});
```

2. Usando o jQuery

```
$("button").click(function(e) {
  $(this); // Objeto que causou o evento...
});
```
