# DIV, SPAN e elementos semânticos

## Elementos de bloco e inline

Todo elemento HTML possui uma forma de exibição padrão, dependendo do tipo de elemento que é. Existem dois valores de exibição: bloco e inline.

### Elemento de bloco

Um elemento no nível do bloco sempre inicia em uma nova lniha e ocupa toda a largura disponível (se estende para a esquerda e direita, tanto quanto possível).

Por exemplo, o `<div>` é um elemento que define um contêiner que permite agrupar conteúdo, formatá-lo e posicioná-lo na tela utilizando técnicas para formatação de estilos CSS. Assim, você pode definir um elemento `<div>` e colocar outros elementos em seu interior.

```
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
      <title>Exemplo div</title>
    </head>
    <body>
      <div id="cabecalho">
          <h1>Coloque o título aqui</h1>
          <hr>
      </div>
      <div id="menuEsquerda">
          <p>Menu da esquerda:</p>
          <ul>
              <li>Item-01 do menu</li>
              <li>Item-02 do menu</li>
              <li>Item-03 do menu</li>
          </ul>
          Fim do menu da esquerda
      </div>
      <div id="conteudoDireita">
          <h1>Título do conteúdo do menu-01</h1>
          <p>Conteúdo no item do Menu</p>
      </div>
    </body>
<html>
```
- O elemento div não é visível no site, sua função é agrupar um conjunto de tags. Note que uma div inicia em uma nova linha.

### Outros elementos de bloco

- `<address>`
- `<article>`
- `<aside>`
- `<blockquote>`
- `<canvas>`
- `<dd>`
- `<div>`
- `<dl>`
- `<dt>`
- `<fieldset>`
- `<figcaption>`
- `<figure>`
- `<footer>`
- `<form>`
- `<h1>-<h6>`
- `<header>`
- `<hr>`
- `<li>`
- `<main>`
- `<nav>`
- `<noscript>`
- `<ol>`
- `<p>`
- `<pre>`
- `<section>`
- `<table>`
- `<tfoot>`
- `<ul>`
- `<video>`

### Elemento inline

Através destes tipos de elementos é possível formatá-los com CSS ou manipular seu conteúdo com JavaScript. Por exemplo, um desses elementos é o `<span>`.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo span</title>
    </head>
    <body>
        <p>Meu carro é <span style="color:red">vermelho</span> e o seu não é.</p>
    </body>
<html>
```

- O estilo do conteúdo do span foi formatado para vermelho.

### Outros elementos inline

- `<a>`
- `<br>`
- `<i>`
- `<object>`
- `<small>`
- `<time>`
- `<abbr>`
- `<button>`
- `<img>`
- `<output>`
- `<span>`
- `<tt>`
- `<acronym>`
- `<cite>`
- `<input>`
- `<q>`
- `<strong>`
- `<var>`
- `<b>`
- `<code>`
- `<kbd>`
- `<samp>`
- `<sub>`
- `<bdo>`
- `<dfn>`
- `<label>`
- `<script>`
- `<sup>`
- `<big>`
- `<em>`
- `<map>`
- `<select>`
- `<textarea>`

## Elementos semânticos

