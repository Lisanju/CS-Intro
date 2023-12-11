# Plano de fundo e modelo de caixa em CSS

## Plano de fundo

As propriedades de plano de fundo do CSS são usadas para definir os efeitos de plano de fundo dos elementos que estão sendo estilizados.

### background-color

Cor de fundo do elemento selecionado. A propriedade `opacity` especifica a opacidade de um elemento, varia de 0 a 1 e quanto menor, mais transparente a cor de fundo.

```
<style>
  body{
    background-color:gray;
  }
  #div1{
    background-color:yellow;
    opacity:0.7;
  }
</style>
```

### background-image

Imagem de fundo do elemento selecionado. Note que, no caso da background-image, ela especifica uma imagem de fundo de um element e, por default, ela é repetida por toda a página.

```
<style>
  body{
    background-image:url("DIRETÓRIO");
  }
</style>
```

### background-repeat

Altera como o modo de repetição de imagens é configurado. Explicação por valor: `repeat-x` repeate a imagem somente no eixo-x, `repeat-y` repete a imagem somente no eixo-y e `no-repeat` não repete a imagem.

```
<style>
    #div1>h2{
        color:white;
    }
    #div1{
        background-image:url("");
    }
    #div2{
        background-image:url("");
        background-repeat:repeat-x;
    }
    #div3{
        background-image:url("");
        background-repeat:repeat-y;
        background-size:250px;
    }
</style>
```

### background-position

Coloca a imagem de fundo em uma posição específica.

```
<style>
    body{
        background-image:url("");
        background-repeat:no-repeat;
        background-position:right top;
        margin-right:300px;
```

### background-attachment

Especifica se a imagem de segundo plano deve ser rolada ou não com o restante da página.

```
<style>
    body{
      background-image:url("");
      background-repeat:no-repeat;
      background-position:right top;
      background-attachment:fixed;
      margin-right:300px;
    }
</style>
```

- `fixed` para imagem fixa e `scroll` para imagem não fixa.

## Modelo de caixa

Cada elemento HTML pode ser considerado uma caixa retangular. O modelo de caixa CSS é uma caixa que envolve todos os elementos HTML, consiste em margens, bordas, preenchimento e conteúdo real.

Para calcular a largura total de um elemento como o parágrafo:

`Largura total do elemento parágrafo = margem x 2 + borda X 2 + padding x 2 + width`

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/db5bf219-f82a-4dee-8682-315e039ff41c)

- Nesse caso, `largura total = 10 x 2 + 1 x 2 + 10 x 2 + 200 = 242 pixels`.

### Pra que serve o modelo de caixa?

Quando você combina as 4 variáveis (margin, border, padding e width), há diversas formas de se determinar o layout de um elemento com seu espaço interno e a margem.

É possível manter todos os elementos (caixa com margem, borda, preenchimento e conteúdo), retirar a margem (caixa com borda, preenchimento e conteúdo), retirar o preenchimento (caixa com borda e conteúdo), manter apenas margem (caixa com margem e conteúdo), variar o formato da borda para sólida ou tracejada, colorir a borda, estender as margens, recuar o conteúdo para o canto inferior direito do preenchimento...

### Estilo de uma borda

- `border-style:dotted;` - Borda pontilhada.
- `border-style:dashed;` - Borda tracejada.
- `border-style:solid;` - Borda sólida.
- `border-style:double;` - Borda dupla.
- `border-style:groove;` - Borda com ranhura.
- `border-style:ridge;` - Borda de cume.
- `border-style:inset;` - Borda inserida.
- `border-style:outset;` - Borda de fronteira inicial.
- `border-style:none;` - Nenhuma borda.
- `border-style:hidden;` - Borda escondida.
- `border-style:dotted dashed solid double;` - Borda mista.

Para estilizar um dos lados da borda:

- `border-top-style` - Borda superior.
- `border-right-style` - Borda direita.
- `border-bottom-style` - Borda inferior.
- `border-left-style` - Borda esquerda.

Para arredondar a borda:

- `border-radius` - Pode receber qualquer valor em pixels que se refere ao raio do vértice arredondado da borda estilizada.

### Largura e cores de bordas

- `border-width` - Em px/pt/cm/em/etc e na seguinte ordem: larguras superior, direita, inferior e esquerda.
- `border-color` - Red, blue, green etc.

### Propriedades de margens

A propriedade `margin` pode receber quatro valores, respectivamente os tamanhos das margens superior, direita, inferior e esquerda. Ou:

- `margin-top` - Tamanho da margem superior.
- `margin-right` - Tamanho da margem direita.
- `margin-bottom` - Tamanho da margem inferior.
- `margin-left` - Tamanho da margem esquerda.

Essas propriedades podem assumir os seguintes valores:
- `auto` - O browser calcula a margem de forma a centralizar horizontalmente o elemento dentro de seu container.
- `length` - Valor em px/pt/pc/etc.
- `%` - Especifica uma margem em % da largura do elemento que contém o elemento estilizado.
- `inherit` - Especifica que a margem deve ser herdada do elemento pai.

Às vezes, as margens superior e inferior dos elementos são unidas em uma única margem igual à maior das duas margens.

### Propriedades de preenchimento

A propriedade `padding` pode receber quatro valores, respectivamente superior, direito, inferior e esquerdo. Caso receba apenas três valores, trata-se respectivamente de superior, direito/inferior e esquerdo.

- `padding-top` - Tamanho do preenchimento superior.
- `padding-right` - Tamanho do preenchimento direita.
- `padding-bottom` - Tamanho do preenchimento inferior.
- `padding-left` - Tamanho do preenchimento esquerda.

Essas propriedades podem assumir os seguintes valores:
- `length` - Valor em px/pt/pc/etc.
- `%` - Especifica em % da largura do elemento que contém o elemento estilizado.
- `inherit` - Especifica que deve ser herdada do elemento pai.

### Propriedades do conteúdo

- `height` - Altura do conteúdo do elemento.
- `width` - Largura do conteúdo do elemento.

- `auto` - Isso é padrão. O navegador calcula a altura e a largura.
- `length` - Define o valor de height;width em px/pt/pc/etc.
- `%` - Especifica um preenchimento em % do height;width do elemento que contém o elemento estilizado.
- `init` - Seta o height;width com seu valor padrão.
- `inherit` - Especifica que o heiht;width deve ser herdada do elemento pai.

A propriedade `max-width` é usada para definir a largura máxima de um elemento. Ao reduzir a janela da página, uma barra de rolagem surge caso a largura máxima seja atravessada.

```
<style>
    div{
      height:100px;
      max-width:500px;
      background-color:powderblue;
    }
</style>
```
