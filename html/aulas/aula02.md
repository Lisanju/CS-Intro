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

### Comentários

As tags de comentários são usadas para inserir comentários no código-fonte HTML. Note que, na tag de abertura há uma exclamação, mas na de fechamento não. Os comentários não são exibidos pelo navegador, mas podem ajudar a documentar seu código-fonte HTML.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de comentário</title>
    </head>
    <body>
        <!-- Este é um comentário -->
        <p>Isto é um parágrafo</p>
        <!-- Comentários não são mostrados no navegador -->
    </body>
</html>
```

### Link externo

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <a href="http://www.ifsp.edu.br">
                    Instituto Federal
        </a>
    </body>
</html>
```
- Os links são encontrados em quase todas as páginas da Web.
- Os links permitem que os usuários naveguem de uma página para outra.
- O atributo href contém o link da página que você deseja visitar.

### Link local

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <a href="01_Aula02_Exemplo03_TagParagrafo.html">
                    Link para o exemplo da tag anterior
        </a>
    </body>
</html>
```
- Um link local (link para o mesmo site) é especificado com um URL relativo, (sem https://www...).
- A URL relativa corresponde ao caminho da página desejada.
- No caso do exemplo, a página requerida se encontra no caminho/arquivo: 01_Aula02_Exemplo03_TagParagrafo.html.

### Imagens

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Primeiro exemplo sobre imagens</title>
    </head>
    <body>
        <img src="ondaMar.jpg" alt="Ondas do mar...">
    </body>
</html>
```
- Em HTML as imagens são definidas pela tag `<img>`.
- A tag `<img>` é vazia, ou seja, não contém uma tag de fechamento e contém somente atributos.
- O atributo src define o local da imagem a ser mostrado pela página Web.
- O atributo alt cria uma alternativa para o browser se, por algum motivo, elen ão conseguir abrir a imagem.

### Caminhos de arquivos locais

<b> Caminho absluto: </b>

URL completo para um arquivo da internet, como "https://www.ifsp.edu.br/"

<b> Caminhos relativos de arquivos locais: </b>

Para um primeiro cenário, imagine que para o arquivo "01_Aula02_Exemplo05_TagLinksParte2_PathRelativo.html", a gente queira acessar o arquivo "figura_01.jpg". Nesse caso, o link relativo seria "/01_imgs/figura_01.jpg ". Isso porque a primeira / denota a raiz do diretório onde colocamos a estrutura de arquivos de páginas em um servidor.

Para um segundo cenário, no mesmo arquivo, desejamos acessar o arquivo "01_solarflare.jpg". Nesse caso, não há barra inicial, denotando que a pasta "01_imgs_filha" se encontra em um nível abaixo em relação a pasta do arquivo "01_Aula02_Exemplo05_TagsLinksParte2_PathRelativo.html".

Para um terceiro cenário, desejamos redirecionar para a página "index.html". Nesse caso, o link relativo é "../index.html". Os dois pontos iniciais seguidos da barra denotam que o arquivo "index.html" está em uma pasta um nível acima da pasta do arquivo origem.

Por exemplo:
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo-01 de link relativo</title>
    </head>
    <body>
        <h4>Link relativo com arquivo de imagem na pasta 01_imgs que encontra-se
na pasta raiz do servidor web: <em>/01_imgs/figura_01.jpeg</em></h4>
        <img src="/01_imgs/figura_01.jpeg" alt="Imagem de uma cachoeira">
        <br>
        <h4>Link relativo com arquivo de imagem na pasta 01_imgs_filha que
&eacute; uma sub-pasta da pasta onde o arquivo atual .html encontra-se:
<em>01_imgs_filha/01_solarflare.jpg</em></h4>
        <img src="01_imgs_filha/01_solarflare.jpg" alt="Imagem de uma
explos&atilde;o solar">
        <br>
        <h4>Link relativo para o arquivo index.html que encontra-se na pasta
localizada um n&iacute;vel acima da pasta do arquivo html corrente:
<em>../index.html</em></h4>
        <a href="../index.html">Voltar para o &iacute;ndice</a>
    </body>
</html>
```
