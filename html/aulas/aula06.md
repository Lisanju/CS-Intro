# Conceitos iniciais em CSS

O Cascading Style Sheets (CSS) descreve como os elementos HTML devem ser exibidos pelo navegador, sendo capaz de controlar o layout de várias páginas da Web de uma só vez. As folhas de estilo externas são armazenadas em arquivos CSS.

As folhas de estilo definem o estilo para páginas Web desenvolvidas em HTML, incluindo: design, layout e adaptações para dispositivos de tamanhos diferentes.

Um conjunto de regras CSS consiste de um seletor e um bloco de declaração.

`h1 {color:blue; font-size:12px;}`

- O seletor aponta para o elemento HTML que você deseja estilizar (`h1`).
- O bloco de declaração contém uma ou mais declarações separadas por ponto e vírgula.
- Cada declaração inclui um nome de propriedade CSS e um valor, separados por dois pontos (`color:blue` e `font-size:12px`).
- Os blocos de declaração são cercados por chaves.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Sintaxe do CSS</title>
        <style>
            p {
            color:red;
            text-align:center;
            }
        </style>
    </head>
    <body>
        <p>Esta página mostra como a sintaxe do CSS funciona</p>
        <p>Este parágrafo está estilizado com CSS</p>
    </body>
</html>
```

É possível definir múltiplas regras CSS.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Segundo exemplo de CSS</title>
        <style>
            body {
            background-color:blueviolet;
            }
            h1 {
            color:white;
            text-align:center;
            }
            p {
            font-family:verdana;
            font-size:25px;
            }
        </style>
    </head>
    <body>
        <h1>Múltiplas regras CSS</h1>
        <p>Este é o parágrafo</p>
    </body>
</html>
```

## Seletores

Os seletores permitem que você estilize um determinado elemento HTML ao selecionar ele. Os seletores CSS podem ser divididos em cinco categorias:
- Seletores simples - A seleção é baseada nos atributo id, name e class.
- Pseudoclasses - A seleção é baseada em estados.
- Pseudo-elementos - Seleciona e estiliza parte de um elemento.
- Seletores de atributo - A seleção é baseada em um atributo ou seu valor.

### Seletor simples

O seletor seleciona elementos HTML com base no nome do elemento.

`p {color:red; text-align:center;}`

O seletor baseado em id usa este atributo para selecionar um elemento específico, já que os id devem ser únicos dentro de uma página. Para escrever esse seletor use o símbolo # seguido do id desejado.

`#p2 {text-align:center; color:darksalmon; background-color:agua;}`

- Nesse caso, somente o elemento HTML com id="p2" é estilizado.

O seletor baseado em classe usa o atributo class para selecionar um ou mais elementos. Para escrever esse seletor use o símbolo . seguido da classe desejada.

`.teste{text-align:center; color:darksalmon; background-color:aqua;}`

- Neste caso, todos os elementos HTML com class="teste" são estilizados.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Segundo exemplo de CSS</title>
        <style>
			p.teste{
            font-family:verdana;
            font-size:25px;
            }
        </style>
    </head>
    <body>
        <h1>Múltiplas regras CSS</h1>
        <p class="teste">Este é o parágrafo</p>
    </body>
</html>
```

Os elementos HTML também podem se referir a mais de uma classe.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Segundo exemplo de CSS</title>
        <style>
			p.centro{
            text-align:center;
            color:darksalmon;
            background-color:aqua;
            }
      p.vermelho{
            background-color:red;
            }
        </style>
    </head>
    <body>
        <h1 class="centro">Múltiplas regras CSS</h1>
        <p class="centro vermelho">Este é o parágrafo</p>
    </body>
</html>
```

O seletor * seleciona todos os elementos HTML. Seletores separados por vírgula substituem seletores com propriedades iguais.

`* {text-align:center; color:red;}` e `h1,h2,p {text-align:center; color:red;}`

### Seletores combinados

Um seletor CSS pode contar mais de um seletor simples, existindo quatro combinadores diferentes:

- `div p {background-color:yellow;}` - Seleciona todos os elementos `<p>` dentro dos elementos `<div>`.
- `div > p {background-color:red;}` - Seleciona todos os elementos `<p>` filhos de um elemento `<div>`.
- `div + p {background-color:blue;}` - Seleciona todos os elementos `<p>` que aparecem logo após os elementos `<div>`.
- `div - p {background-color:pink;}` - Seleciona todos os elementos `<p>` irmãos dos elementos `<div>`.

### Seletores pseudoclasses

Uma pseudoclasse é usada para definir um estado especial de um elemento, podendo ser usada para estilizar um elemento quando um usuário passar o mouse sobre ele, estilizar links visitados e não visitados de maneira diferente e estilizar um elemento quando ele receber foco.

- `:active` - Ex. `a:active` - Seleciona o link ativo.
- `:checked` - Ex. `input:checked` - Seleciona todo elemento `<input>` assinalado.
- `:disabled` - Ex. `input:disabled` - Seleciona todo elemento `<input>` desabilitado.
- `:first-child` - Ex. `p:first-child` - Seleciona todos os elementos `<p>` que são o primeiro filho de seu pai.

### Seletores pseudo-elementos

Um pseudo-elemento é usado para estilizar partes específicas de um elemento, podendo ser usada para estilizar a primeira letra ou linha de um elemento e inserir conteúdo antes ou depois do conteúdo de um elemento.

- `::after` - Ex. `p::after` - Inserir algo após o conteúdo de cada elemento `<p>`.
- `::before` - Ex. `p::before` - Inserir algo antes do conteúdo de cada elemento `<p>`.
- `::first-letter` - Ex. `p::first-letter` - Seleciona a primeira letra de cada elemento `<p>`.
- `::first-line` - Ex. `p::first-line` - Seleciona a primeira linha de cada elemento `<p>`.
- `::selection` - Ex. `p::selection` - Seleciona a parte de um elemento que é selecionado por um usuário.

### Seletores de atributo

O seletor `[attribute]` é usado para selecionar elementos com um atributo específico.

- `[attribute]` - Ex. `[target]` - Seleciona todos os elementos com um atributo target.
- `[attribute=value]` - Ex. `[target=_blank]` - Seleciona todos os elementos com target=_blank.
- `[attribute~=value]` - Ex. `[title~=flor]` - Seleciona todos os elementos com um atributo title que contém a palavra flor.
- `[attribute|=value]` - Ex. `[lang|=en]` - Seleciona todos os elementos com um valor de atributo lang começando com en.
- `[attribute^=value]` - Ex. `a[href^="https"]` - Seleciona todos os elementos `<a>` cujo valor do atributo href começa com https.
- `[attribute$=value]` - Ex. `a[href$=".pdf"]` - Seleciona todos os elementos `<a>` cujo valor do atributo href termina com .pdf.
- `[attribute*=value]` - Ex. `a[href*="w3schools"]` - Seleciona todos os elementos `<a>` cujo valor do atributo href contém a substring w3schools.

## Como adicionar CSS em sua página HTML

Existem três maneiras de inserir uma folha de estilo, que são CSS externo, CSS interno e CSS embutido.

CSS externo: cada página HTML deve incluir uma referência ao arquivo da folha de estilos externa dentro do elemento `<link>`, dentro da seção principal.

Por exemplo - `<link rel="stylesheet" type="text/css" href="DIRETÓRIO.css">`

CSS interno: o estilo interno é definido dentro do elemento `<style>`, dentro do elemento `<head>`.

CSS embutido: é necessário adicionar o atributo style ao elemento relevante. O atributo style pode conter qualquer propriedade CSS.

Por exemplo - `<p style="color:red;">Parágrafo</p>`

### Sobre a ordem da cascata

Que estilo será usado quando houver mais de um estilo especificado para um elemento HTML? Todos os estilos em uma página serão cascateados em uma nova folha de estilos virtuais pelas seguintes regras, onde o primeiro tem maior prioridade:
- Estilo embutido (dentro de um elemento HTML);
- Folhas de estilo externas e internas (na seção principal);
- Padrão do navegador.
