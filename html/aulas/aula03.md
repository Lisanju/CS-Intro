# Listas ordenadas e não ordenadas

Existem dois tipos de listas, as ordenadas e as não ordenadas. As listas ordenadas listam itens através de números ou sequenciais.
As listas não ordenadas listam itens através de marcadores.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo sobre listas ordenadas</title>
    </head>
    <body>
        <h1>Primeiro exemplo sobre listas ordenadas</h1>
        <ol>
          <li>Caf&eacute;</li>
          <li>Ch&aacute;</li>
          <li>Leite</li>
        </ol>
    </body>
</html>
```
- Uma lista ordenada começa com a tag `<ol>`. Cada item da lista começa com a tag `<li>`.
- Por padrão, os itens da lista serão marcados com números.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo sobre listas ordenadas</title>
    </head>
    <body>
        <h1>Primeiro exemplo sobre listas n&atilde;o ordenadas</h1>
        <ul>
          <li>Caf&eacute;</li>
          <li>Ch&aacute;</li>
          <li>Leite</li>
        </ul>
    </body>
</html>
```
- Uma lista não ordenada começa com a tag `<ul>`. Cada item da lista começa com a tag `<li>`.
- Os itens da lista serão marcados com marcadores (pequenos círculos pretos) por padrão.

### Formatação do tipo de símbolo das listas

Para listas não ordenadas:
```
<ul style="list-style-type:disc;">
<ul style="list-style-type:circle;">
<!-- etc. -->
```
- disc - Um círculo é mostrado.
- circle - Um círculo vazio é mostrado.
- square - Um quadrado é mostrado.
- none - Nenhum marcador é mostrado.

Para listas ordenadas:
```
<ol type="1">
<ol type="A">
<!-- etc. -->
```
- 1 - 1,2,3,4 ...
- a - a,b,c,d ...
- A - A,B,C,D ...
- i - i,ii,iii,iv ...
- I - I,II,III,IV ...

### Listas Aninhadas
```
<ul>
    <li> Estados da região sul do Brasil:
        <ul>
            <li> Rio Grande do Sul </li>
            <li> Paraná </li>
            <li> Santa Catarina </li>
        </ul>
    </li>
    <li> Um estado da região sudeste:
        <ul>
            <li> São Paulo </li>
            <li> Rio de Janeiro </li>
            <li> Minas Gerais </li>
            <li> Espírito Santos </li>
        </ul>
    </li>
</ul>
```

### Listas de Descrição (DL)

Uma lista de descrição é uma lista de termos, com uma descrição de cada termo.

```
<dl>
    <dt>HTML</dt>
    <dd>HyperTextMarkupLanguage</dd>
    <dt>OL</dt>
    <dd>Listsa ordenadas com numeração</dd>
    <dt>UL</dt>
    <dd>Listas sem ordenação</dd>
    <dt>DL</dt>
    <dd>Listas de definição</dd>
    <dt>LI</dt>
    <dd>Elemento de lista</dd>
</dl>
```
- A tag `<dl>` inicia a lista.
- A tag `<dt>` contém o termo abreviado.
- A tag `<dd>` contém a definição.

