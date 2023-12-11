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
