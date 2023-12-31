# Posicionamento em CSS

Existem dois tipos de elementos, os inline e os blocos. Os inline sempre ocupam apenas o espaço necessário e não iniciam uma nova linha (ex. span). Os blocos sempre iniciam em uma nova linha e ocupam toda a largura disponível (ex. div).

O fluxo é o modo como o navegador organiza a página de elementos HTML. O navegador começa do topo do arquivo HTML e segue o fluxo dos elementos do início até o final, exibindo cada elemento que encontrar.

- Considerando os elementos de bloco, ele coloca uma quebra de linha entre cada. Assim, o primeiro elemento HTML em bloco é exibido no topo da página, uma quebra de linha é inserida e então seguida pelo segundo elemento, isso se segue do início ao fim do arquivo HTML. Isso é o fluxo dos elementos em bloco.

- Considerando os elementos inline, eles são inseridos da esquerda para a direita e do canto superior esquerdo ao canto inferior direito. Isso é o fluxo de elementos inline.

Quando um navegador deve colocar dois elementos inline lado a lado, e tais elementos tiverem margens, ele cria espaço suficiente entre os elementos para acomodar as duas margens. Se o elemento da esquerda tiver margem 10px e o da direita tiver margem 20px, o espaço entre eles será de 30px.

Quando um navegador coloca dois elementos em bloco um em cima do outro, ele junta as duas margens compartilhadas. A altura da margem compartilhada será igual à altura da margem maior. Se o elemento de cima tiver margem-inferior de 10px e o elemento inferior tiver margem-superior de 20px, o espaço entre eles será de 20px.

- O CSS permite alterar o tipo de caixa de um elemento usando a tag display. Se o valor da propriedade display valer block, um elemento inline será transformado em bloco. Se o valor for none, o elemento sairá do fluxo e ele não será exibido na página.

### Esquemas de posicionamento

A propriedade CSS usada para posicionar elementos HTML em uma página é chamada position. Existem usualmente os esquemas básicos de posicionamento a seguir:

- `static`.
- `relative`.
- `absolute`.
- `fixed`.
- `sticky`.

Um elemento com `position:static;` é posicionado de acordo com o fluxo normal da página. Os elementos HTML são posicionados estáticos por padrão.

Um elemento com `position:relative;` é posicionado em relação à sua posição normal. O posicionamento é feito sempre em relação ao fluxo normal configurando uma posição vertical ou horizontal usando as propriedades top, right, bottom ou left.

```
div#div02{
    position:relative;
    top:200px;
    left:20px;
    background-color:#3498DB;
}
```

- Note que, para esse caso de relative, esse posicionamento mantém o elemento no mesmo lugar que estava no fluxo, mas aplica um deslocamento em relação à sua posição original. Então, mesmo deslocado, esse elemento não influencia no posicionamento dos demais elementos.

Um elemento com `position:absolute;` remove o elemento do fluxo e o posiciona em relação ao parente posicionado mais próximo. Logo, se um elemento com `position:absolute;` não tiver ancestrais posicionados, ele usrá o corpo do documento e se moverá com a rolagem da página.

```
div#div02{
    position:absolute;
    top:200px;
    left:20px;
    background-color:#3498DB;
}
```

- Nesse caso, o div2 sairá do fluxo e será posicionada à 200px do topo e 20 da esquerda do seu ancestal (que é o elemento body).

O posicionamento `position:fixed` é uma subcategoria do posicionamento absoluto, no qual o elemento é posicionado em relação à janela de exibição, o que significa que sempre permanece no mesmo local, mesmo que a página seja rolada. As propriedades topo, direita, inferior e esquerda são usadas para posicionar o elemento.

O posicionamento `position:sticky` alterna entre relativo e fixo, dependendo da posição de rolagem. É relativo até que uma determinada posição de deslocamento seja alcançada na janela de visualização, então permanece fixo na posição definida (através das popriedades top e bottom).

## Flutuação

Através do conceito de flutuação, uma caixa flutuante pode ser mudada para a esquerda ou direita até que sua borda externa toque a borda da caixa que a contém ou uma outra caixa flutuante. Com a flutuação, as caixas são retiradas do fluxo normal. Logo, as demais caixas se comportam como se a caixa flutuante não estivesse no documento.

A propriedade `clear` especific quais elementos podem flutuar ao lado do elemento limpo e de qual lado. A propriedade `clear` pode ter um dos seguintes valores:

- `none` - Permite elementos flutuantes nos dois lados. Isso é padrão.
- `left` - Não são permitidos elementos flutuantes no lado esquerdo.
- `right` - Não são permitidos elementos flutuantes no lado direito.
- `both` - Não são permitidos elementos flutuantes nos dois lados.
- `inherit` - O elemento herda o valor de seu ancestral.

## Layout líquido e congelado

O layout líquido se expande para preencher qualquer largura que o navegador tenha. Já o layout congelado mantém a página bloqueada mesmo quando a tela do navegador é redimensionada.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>exemplo</title>
        <style>
            body{
                margin:0px;
                background-color:burlywood;
            }
            #divheader{
                background-image:url("");
                height:100px;
            }
            #cabecalho{
                margin:10px;
            }
            #principal{
                background-color:khaki;
                padding:15px;
                margin:0px 330px 10px 10px;
            }
            #barralateral{
                background-color:khaki;
                padding:15px;
                margin:0px 10px 10px 10px;
                width:280px;
                float:right;
            }
            #rodape{
                color:white;
                background-color:darkred;
                text-align:center;
                padding:15px;
                margin:10px;
                clear:right;
            }
        </style>
        <body>
            <div id="cabecalho">
                <div id="divheader">
                </div>
            </div>
            <div id="barralateral">
                <p>
                    <img src=""><br>
                </p>
                <ul>
                    <li>Item-01</li>
                    <li>Item-02</li>
                    <li>Item-03</li>
                    <li>Item-04</li>
                    <li>Item-05</li>
                </ul>
                <a href="">Fale conosco</a>
                <p>Lorem ipsum</p>
            </div>
            <div id="principal">
                <h1>Título-01</h1>
                <p>Lorem ipsum</p>
                <p>Lorem ipsum</p>
                <h1>Título-02</h1>
                <p>Lorem ipsum</p>
                <p>Lorem ipsum</p>
            </div>
            <div id="rodape">
                <p>Lorem ipsum</p>
            </div>
        </body>
    </head>
</html>
```

Para esse arquivo HTML, temos a seguinte disposição de div's: cabeçalho, barra lateral, principal e rodapé. Aplicando `float:right` na barra lateral, ela sai do fluxo e vai para a direita e a principal sobe.

Mas, para ficar com a disposição visível ao lado, devemos limitar a largura da barra lateral (280px) e aumentar a margem da principal (330px).

Por fim, o `clear:right` no rodapé foi necessário para a barra lateral não sobrepor ele.

Porém, toda essa disposição do arquivo HTML é para um layout líquido. E se quisermos congelar o layout? Vamos precisar alterar o HTML e o CSS.

Pelo lado do HTML, temos que inserir uma div envolvendo as div's já existentes. Neste caso, a div pode ser chamada de div "envólucro".

Pelo lado do CSS, temos o seguinte código para a div "envólucro".

```
#envolucro{
    width:800px;
    padding-top:5px;
    padding-bottom:5px;
    background-color:#675c47;
}
```

Ao definir `width:800px`, toda página caberá nesta largura. Como resultado, a página estará fixada, mas você notará que o layout inteiro estará disposto na esquerda do site.

Para centralizar a página, usamos mais duas propriedades no CSS do envólucro.

```
margin-left:auto;
margin-right:auto;
```

As margens da esquerda e direita como auto centralizam a div envólucro.

## Listas

Em listas não ordenadas, é possível simplificar a formatação por:

```
<style>
    ul.none{
        list-style-type:none;
    }
    ul.circle{
        list-style-type:circle;
    }
    ul.square{
        list-style-type:square;
    }
</style>
<body>
    <ul class="none">
        <li>Item um</li>
        <li>Item dois</li>
    </ul>
    <ul class="circle">
        <li>Item um</li>
        <li>Item dois</li>
    </ul>
    <ul class="square">
        <li>Item um</li>
        <li>Item dois</li>
        <li>Item três</li>
    </ul>
</body>
```

Em listas ordenadas, esta propriedade pode assumir os seguintes valores: upper-roman, lower-alpha, decimal, lower-latin, upper-latim, entre outros.

Através de `list-style-position` é possível alinhar a lista na vertical com o valor `outside` ou não alinhar com o valor `inside`.

## Links

Os links podem ter estilos diferentes dependendo do estado em que estão. Os quatro estados dos links são:

- `a: link` - Um link normal e não visitado.
- `a: visited` - Um link que o usuário visitou.
- `a: hover` - Um link quando o usuário passa o mouse sobre ele.
- `a: active` - Um link no momento em que é clicado.

A propriedade `text-decoration` é usada principalmente para remover os sublinhados dos links com o valor `none`.

## Barra de navegação

Uma barra de navegação é feita com uma lista de links:

```
<ul>
    <li><a href="principal.html">Home</a></li>
    <li><a href="noticias.html">Notícias</a></li>
    <li><a href="contato.html">Contato</a></li>
    <li><a href="sobre.html">Sobre</a></li>
</ul>
```

Para deixar a lista num formato de barra de navegação vertical, é necessário fazer as seguintes mudanças no HTML e CSS.

```
<ul>
    <li><a class="ativo" href="principal.html">Home</a></li>
    <li><a href="noticias.html">Notícias</a></li>
    <li><a href="contato.html">Contato</a></li>
    <li><a href="sobre.html">Sobre</a></li>
</ul>
```

```
<styles>
    ul{
        list-style-type:none;
        margin:0;
        padding:0;
        width:200px;
        background-color:#f1f1f1;
        border:1px solid #555;
    }
    li a{
        display:block;
        color:#000;
        padding:8px 16px;
        text-decoration:none;
    }
    li{
        text-align:center;
        border-bottom:1px solid black;
    }
    li:last-child{
        border-bottom:none;
    }
    li a.ativo{
        background-color:blue;
        color:white;
    }
    li a:hover:not(.ativo){
        background-color:#555;
        color:white;
    }
</style>
```

Respectivamente, em CSS, temos:

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/d1a16bde-e333-48b3-82f0-c2d3cbfbaa2d)

Já, para ter uma barra de navegação na horizontal, precisamos fazer as seguintes modificações em HTML e CSS.

```
<ul>
    <li><a href="principal.html">Home</a></li>
    <li><a href="noticias.html">Notícias</a></li>
    <li><a href="contato.html">Contato</a></li>
    <li><a href="sobre.html">Sobre</a></li>
</ul>
```

```
<styles>
    ul{
        list-style-type:none;
        margin:0;
        padding:0;
        overflow:hidden;
        background-color:#f3f3f3;
        border:1px solid #e7e7e7;
    }
    li{
        float:left;
    }
    li a{
        display:block;
        color:#666;
        text-align:center;
        padding:14px 16px;
        text-decoration:none;
    }
    li a.ativo{
        background-color:blue;
        color:white;
    }
    li a:hover:not(.ativo){
        background-color:#ddd;
    }
</style>
```

Em CSS, temos respectivamente:

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/c9289078-4aeb-4a89-9c66-f5fa6a05214d)

