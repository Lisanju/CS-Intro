## Transformações em CSS

### Forms

Para selecionar todos os inputs da página HTML, use o seletor `input`.

Caso deseje selecionar por tipo de input, use o seguinte seletor `input[type=tipo de input]`.

- `input[type=text]`
- `input[type=password]`
- `input[type=radio]`

```
<style>
  input[type=text]{
    width:100%;
    padding:16px 8px;
    box-sizing:border-box;
    border:2px solid darkblue;
    border-radius:8px;
    background-color:rgb(194,212,229);
    color:rgb(7,7,104);
  }
</style>

<form>
  <label for="nome">Nome</label>
  <input type="text" id="nome">
  <label for="email">Email</label>
  <input type="text" id="email">
  <label for="nac_BR">Brasileira</label>
  <input type="radio" name="nacionalidade" id="nac_BR" value="Brasileira">
  <label for="nac_AR">Argentina</label>
  <input type="radio" name="nacionalidade" id="nac_AR" value="Argentina">
  <label for="nac_PA">Paraguaia</label>
  <input type="radio" name="nacionalidade" id="nac_PA" value="Paraguaia">
  <input type="submit" value="Submit">
</form>
```

No CSS, é definido a largura pro input de 100% da largura do elemento pai (form), espaço entre borda e conteúdo, largura do conteúdo é embutida com padding e margin, configuração da borda do input text, borda com vértices arredondados e cores de fundo e de texto.

``` 
<style>
  input[type=text]{
    width:100%;
    box-sizing:border-box;
    border:2px solid #ccc;
    border-radius:4px;
    font-size:16px;
    background-color:white;
    background-image:url("");
    background-size:1em 1em;
    background-position:10px 10px;
    background-repeat:no-repeat;
    padding:12px 20px 12px 40px;
  }
</style>
<body>
  <form>
    <label for="procurar">Procurar</label>
    <input type="text" id="procurar" placeholder="Procurar...">
    <br><br><input type="submit" value="Submit">
  </form>
</body>
```

No CSS acima, é incluída uma imagem no input text, lagura e altura da imagem e posição em relação à esquerda-topo.

```
<style>
  select{
    width:100%;
    padding:16px 20px;
    border:none;
    border-radius:4px;
    background-color:#f1f1f1;
    margin-bottom:50px;
  }

  input[type=button]{
    background-color:aqua;
    border:none;
    color:darkblue;
    padding:16px 32px;
    text-decoration:none;
    margin:4px 2px;
    cursos:pointer;
  }
</style>
<body>
  <form>
    <select id="pais" name="pais">
      <option value="br">Brasil</option>
      <option value="ar">Argentina</option>
      <option value="par">Paraguai</option>
    </select>
    <br><br>
    <input type="button" value="Escolher País">
  </form>
</body>
```

No CSS acima, é estilizado a largura, a borda e o raio do vértice do select e o tipo de ponteiro ao passar sobre o botão (o ponteiro é uma mão ao passar sobre o botão).

## Transformações

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utd-8">
    <title>Exemplo-03: Forms-select</title>
    <style>
      #div1{
        width:100px;
        height:100px;
        background-color:aqua;
        border:solid 1px darkblue;
        }
      #div1:hover{
        transform:translate(20px,20px);
        }
    </style>
  </head>
  <body>
    <div id="div1"></div>
  </body>
</html>
```

`transform:translate(20px,20px);`

Ao passar com o mouse por cima do elemento (hover), faz uma translação 20px a partir da esquerda e 20px a partir do topo.

Existem outros métodos de transformação de elementos HTML em CSS:

- `rotate()` - `transform:rotate(20deg)` - Rotaciona 20 graus no sentido horário.
- `scale()` - `transform:scale(2,5)` - Dobra a largura e quintuplica a altura.
- `scaleX()` - `transform:scaleX(2)` - Dobra a largura.
- `scaleY()` - `transform:scaleY(4)` - Quadruplica a altura.
- `skewX()` - `transform:skewX(20deg)` - Inclina 20 graus em relação ao eixo X.
- `skewY()` - `transform:skewY(20deg)` - Inclina 20 graus em relação ao eixo Y.

