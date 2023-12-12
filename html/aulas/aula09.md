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

