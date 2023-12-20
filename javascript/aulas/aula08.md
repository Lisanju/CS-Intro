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

## Caminhar na árvore DOM

```
$("p").not("#ifsp"); // Seleciona todos os 'p', exceto id='ifsp'
$("p").eq(3); // Seleciona o 'p' com índice escolhido
$("p").eq(-2); // Seleciona o penúltimo 'p'
$("p").first(); // Seleciona o primeiro 'p'
$("p").last(); // Seleciona o último 'p'
$("p").children(); // Seleciona todos os filhos de todos 'p'
$("p").next(); // Seleciona os próximos irmãos de 'p'
$("p").prev(); // Seleciona irmãos anteriores de 'p'
$("p").parent(); // Seleciona o pai de todos os 'p'
```

Métodos como children, next e prev aceitam um parâmetro usado como filtro.

`$("p").children(".azul");` - Seleciona todos os filhos de "p" que tnham a classe "azul".

## Modificando elementos DOM

```
// Retorna o conteúdo html do elemento com id='teste' selecionado
var conteudo = $("#teste").html();
// Modifica o conteúdo html do elemento selecionado (id='teste')
$("#teste").html("<p>Teste</p>");
// Retorna o conteúdo text do PRIMEIRO elemento com classe 'verde'
var conteudo = $(".verde").text();
// Modifica o conteúdo text DE TODOS os elementos com classe 'verde'
$(".verde").text("novo conteúdo de exemplo");
// Retorna o valor digitado de um campo input com nome 'ifsp'
var idade = $("input[name=ifsp]").val();
// Modifica o valor de um campo input com nome 'ifsp'
$("input[name=ifsp]").val("13.125");
```

Os métodos text e html (e val) modificam ou acessam o conteúdo de uma tag `<tag>conteúdo</tag>`. Além do conteúdo, é possível modificar os atributos da tag.

```
/*
Retorna o valor do campo 'id' do primeiro 'div'
--- caso não exista o atributo? undefined ---
*/
var idDiv = $("div").eq(0).attr("id");
/*
Modifica o valor do atributo 'id' do último 'p'
--- caso não exista o atributo? adiciona o atributo! ---

*/
$("p").last().attr("id", "ifsp");
```

Um caso particular é o atributo multivalorado class. Existem três métodos específicos: addClass, hasClass e removeClass.

```
// Verifica se o elemento possui a classe 'azul'
if($("#conteudo").hasClass("azul")) {
  // Se existir, remove a classe 'azul' do elemento
  $("#conteudo").removeClass("azul");
} else {
  // Se não existir, adiciona a classe 'azul' ao elemento
  $("#conteudo").addClass("azul");
```
