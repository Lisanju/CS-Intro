# Sintaxe básica em HTML

O HyperText Markup Language (HTML) é uma linguagem de marcação, que possui rótulos de marcação que definem as páginas Web.

As Tags HTML (rótulos de marcação) são palavras-chaves envolvidas por < > que normalmente aparecem em dupla: as tags de abertura e as de fechamento. As Web Pages (Documentos HTML) são conjuntos de Tags HTML em arquivos de texto pleno.

Por exemplo:
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Estrutura básica de um arquivo HTML</title>
    </head>
    <body>
        <h1> Esta tag serve para denotar um Título-1 </h1>
        <p> Esta tag serve para denotar um Parágrafo-1 </p>
    </body>
</html>
```

- A declaração `<!DOCTYPE html>` define este documento como sendo HTML5.
- O elemento `<head>` contém os metadados do documento HTML. Metadados são dados que definem outros dados, ou seja, descrevem características do documento, normalmente definindo o título do documento, sua codificação, estilos e scripts.
- O texto entre `<html>` e `</html>` descreve a página Web.
- O texto entre `<body>` e `</body>` é a parte visível do conteúdo da página.
- O texto entre `<h1>` e `</h1>` é mostrado como um título.
- O texto entre `<p>` e `</p>` é mostrado como um parágrafo.
- A tag `<meta charset="utf-8">` define a codificação do documento HTML como UTF-8.

Então, vimos que documentos HTML são definidos por elementos HTML. Em que os elementos HTML são tudo o que está entre uma tag de abertura e uma tag de fechamento. Alguns elementos HTML são vazios, sendo fechados logo na tag de abertura. Nota-se que as tags devem sempre ser escritas em minúsculo.

A maioria dos elementos HTML podem conter atributos. Além disso, um elemento HTML pode conter outro(s) elemento(s) HTML, o que é chamado de elemento HTML aninhado.

### Atributos

Atributos são sempre representados através do par nome = "valor", por exemplo:

```
<html>
    <body>
         <a href="http://www.ifsp/edu/br">Instituto Federal</a>
    </body>
</html>
```
- O href é o atributo que possui um endereço como valor.
- Os valores devem vir envolvidos por aspas.
- Tanto valores quanto nomes de atributos não diferenciam minúsculas de maiúsculas.

### Títulos

Os títulos podem mostrar a estrutura da sua página Web. As ferramentas de busca procuram pelos títulos:

```
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de T&iacute;tulo</title>
    </head>
    <body>
        <h1>T&iacute;tulo-1</h1>
        <h2>T&iacute;tulo-2</h2>
        <h3>T&iacute;tulo-3</h3>
    </body>
</html>
```
- O `<h1>` deve ser usado como título principal, seguido por `<h2>`, `<h3>` e assim por diante.
- O `<head>` indica o título da página Web.

### Parágrafos

O elemento HTML `<p>` define um parágrafo:

```
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de parágrafo</title>
    </head>
    <body>
        <p> Este texto está dentro de um parágrafo. </p>
        <p> Este texto está dentro de outro parágrafo </p>
    </body>
</html>
```

### Atributo style

A configuração do estilo de um elemento HTML pode ser feita com o atributo style para cada tag que desejamos formatar, sendo a base do CSS.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Primeiro exemplo sobre <em>style</em></title>
    </head>
    <body>
        <h1 style="color:blue;">Este t&iacute;tulo est&aacute; em azul.</h1>
        <p style="color:red;">Este par&aacute;grafo est&aacute; em vermelho.</p>
        <p style="font-family:courier;">Este par&aacute;grafo est&aacute; escrito na fonte <q>Courier</q>.</p>
        <p style="font-family:Verdana;">J&aacute; este, em <q>Verdana</q>.</p>
        <h2 style="text-align: center">Este t&iacute;tulo est&aacute; centralizado.</h2>
        <h2 style="text-align: right">Este t&iacute;tulo est&aacute; &agrave; direita.</h2>
    </body>
</html>
```
- O valor do atributo style deve contar um par composto pela chave e pelo seu valor. A chave é o tipo de estilo do elemento HTML que desejamos formatar e o vlor denota um valor pré-definido para o tipo escolhido, como `color:Blue` altera a fonte de um texto para azul, `font-family:courier` altera a família da fonte de um texto para courier e `text-align: center` alinha um texto no centro do browser.

### Elementos de formatação

- `<b>` - Texto em negrito.
- `<strong>` - Texto marcado com o significado "importante" e mostrado em negrito.
- `<i>` - Texto em itálico.
- `<em>` - Texto em itálico com significado enfatizado.
- `<mark>` - Texto marcado com uma cor.
- `<small>` - Texto mostrado com uma fonte de tamanho menor.
- `<del>` - Texto mostrado com uma linha em cima.
- `<ins>` - Texto mostrado sublinhado.
- `<sub>` - Texto subscrito.
- `<sup>` - Texto superescrito.

Por exemplo:

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de elementos de formatação</title>
    </head>
    <body>
        <p>Texto normal.</p>
        <p><b>Texto envolto com elemento &alt;b&gt;</b></p>
        <p><strong>Texxto envolto com elemento &alt;strong&gt;</strong></p>
        <p><del>Texto envolto com elemento &alt;del&gt;</del></p>
        <p><ins>Texto envolto com elemento &alt;ins&gt;</ins></p>
    </body>
</html>
```
