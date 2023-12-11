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
