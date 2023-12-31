# Formulários e tabelas

## Formulários

Os formulários são utilizados para a interação entre um usuário e o servidor, possibilitando a troca de dados ou informações.

`<form> ... </form>`

Um formulário HTML contém elementos de formulário, que são diferentes tipos de entrada, como campos de texto, caixas de seleção, botões de opção e botões de envio.

### Label for e Input type text

```
<form>
    <label for="pNome">Primeiro Nome:</label><br>
    <input type="text" id="pNome" name="pNome" value="José"><br>
    <label for="uNome">Último Nome:</label><br>
    <input type="text" id="uNome" name="uNome" value="Oliveira">
</form>
```

- O exemplo acima cria um label usando a tag `<label>` para descrever o campo texto definido. Cria também um campo de entrada do tipo text, que permite a digitação de um texto (caracteres) usando `input type="text"`.
- A tag `<label>` possui o parâmetro `for`, esse atributo deve ter o mesmo valor do atributo `id` do elemento `<input>` para vinculá-los.
- A tag `<input>` possui os parâmetros: `type`, que define a forma como a entrada é mostrada (text, button, checkbox etc); `id`, que especifica um ID exclusivo para um elemento; `name`, que é usado como referência quando os dados do formulário são enviados; `value`, que especifica um valor inicial para um campo de entrada.

### Input type password e Input type checkbox

Os caracteres no campo senha (password) são apresentados como asteriscos.

```
<form>
    <label for="txtLogin">Login:</label><br>
    <input type="text" id="txtLogin" name="txtLogin"><br>
    <label for="pwd">Senha:</label><br>
    <input type="password" id="pwd" name"pwd">
</form>
```

Uma checkbox é um campo de múltipla escolha, no qual o usuário pode escolher mais de uma opção.

```
<form>
    <input type="checkbox" id="veiculo1" name="veiculo1" value="Bicicleta">
    <label for="veiculo1">Eu tenho uma bicicleta</label><br>
    <input type="checkbox" id="veiculo2" name="veiculo2" value="Carro">
    <label for="veiculo2">Eu tenho um carro</label><br>
    <input type="checkbox" id="veiculo3" name="veiculo3" value="Barco">
    <label for="veiculo3">Eu tenho um barco</label><br>
</form>
```

### Input type radio

Radio é mais um campo de múltipla escolha, mas nesse caso o usuário poderá escolher apenas uma opção. Os parâmetros seguem o mesmo roteiro do checkbox.

```
<form>
    <input type="radio" id="cbuilder" name="pref" value="cbuilder" checked>
    <label for="cbuilder">C++Builder</label><br>
    <input type="radio" id="php" name="pref" value="php">
    <label for="php">PHP</label><br>
    <input type="radio" id="delphi" name="pref" value="delphi">
    <label for="delphi">Delphi</label><br>
</form>
```

- Tanto para os campos checkbox e radio, o parâmetro `checked` é opcional e determina a marcaçào de uma opção inicial. Já o parâmetro `value` é obrigatório e especifica o valor da opção a ser enviada ao servidor.

### Input type reset | button | submit | textarea

- `<input type="reset">` - Apaga os dados e restaura o valor padrão dos campos de um formulário.
- `<input type="button" value="Texto escrito no botão">` - Botão clicável.
- `<input type="submit" value="enviar">` - Envia as informações digitadas ao servidor.

Obs: o parâmetro `value` é opcional.

- `<textarea>` - Utilizada para textos maiores, que podem ser livremente digitados.

```
<textarea name="opinião" rows="5" cols="40"> digite aqui sua avaliação deste curso </textarea>
```

- Em `<textarea>` o texto default é opcional, mas os parâmetros `rows` e `cols` devem ser especificados.

### Listbox: Select e Option

A tag `<select> ... </select>` é utilizada para criar uma lista de itens, em que um ou mais itens podem ser selecionadas. Cada item da lista deve ser especificado pelo parâmetro `<option>`. Quando o parâmetro `size` é omitido, a lista aparece fechada, caso contrário, a lista é exibida aberta e mostra a quantidade de linhas especificada por esse parâmetro.

```
<label for="cursos">Escolha um curso:</label>
<select id="cursos">
    <option value="bcb">C++Builder</option>
    <option value="php">PHP</option>
    <option value="delphi">Delphi</option>
    <option value="vb">Visual Basic</option>
    <option value="asm">Assembly</option>
</select>
```

O parâmetro `<multiple>` permite que vários itens possam ser selecionados utilizando as teclas CTRL ou SHIFT.

## Entrada de dados

### Input type number e range

O `<input type="number">` define um campo de entrada numérico.

```
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de fieldset e legend</title>
    </head>
    <body>
        <form>
            <label for="quantidade">Quantidade (entre 1 e 5):</label>
            <input type="number" id="quantidade" min="1" max="5">
        </form>
    </body>
</html>
```

O `<input type="range">` define um controle para inserir um número cujo valor exato não é importante (como um controle deslizante). O intervalo padrão é de 0 a 100, mas é possível definir restrições sobre quais números são aceitos com os atributos min, max e step.

```
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de fieldset e legend</title>
    </head>
    <body>
        <form>
            <label for="vol">Volume (entre 0 e 50):</label>
            <input type="range" id="vol" name="vol" min="0" max="50">
        </form>
    </body>
</html>
```

O elemento `<fieldset>` é utilizado para agrupar informações relacionadas em um formulário.
O elemento `<legend>` define um título para o elemento `<fieldset>`.

```
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo de fieldset e legend</title>
    </head>
    <body>
        <form>
            <fieldset>
                <legend>Informações pessoais</legend>
                <label for="Pnome">Primeiro Nome:</label><br>
                <input type="text" id="Pnome" name="nome" value="João"><br>
                <label for="Snome">Sobrenome:</label><br>
                <input type="text" id="Snome" name="nome" value="Oliveira"><br><br>
                <input type="submit" value="Submit">
            </fieldset>
        </form>
    </body>
</html>
```

O elemento `<datalist>` especifica uma lista de opções predefinidas para um elemento `<input>`. O atributo de lista do elemento `<input>` deve se referir ao atributo de id do elemento `<datalist>`.

```
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form>
            <input list="browsers" name="browser">
            <datalist id="browsers">
                <option value="Internet Explorer">
                <option value="Firefox">
                <option value="Chrome">
                <option value="Opera">
                <option value="Safari">
            </datalist>
            <input type="submit">
        </form>
    </body>
</html>
```

```
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
            <input type="range" id="a" value="50">100
            +<input type="number" id="b" value="50">
            =<output name="x" for="a b"></output>
        </form>
    </body>
</html>
```

A tag `<optgroup>` é usada para agrupar opções relacionadas em uma lista suspensa. Se você tiver uma lista longa de opções, é mais fácil gerenciar grupos de opções relacionadas a um usuário.

```
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form>
            <label for="carros">Escolha um carro: </label>
            <select id="carros">
                <optgroup label="Carro suecos">
                    <option value="volvo">Volvo</option>
                    <option value="saab">Saab</option>
                </optgroup>
                <optgroup label="Carro Alemães">
                    <option value="mercedes">Mercedes</option>
                    <option value="audi">Audi</option>
                </optgroup>
            </select>
        </form>
    </body>
</html>
```

### Input type color

O `<input type="color">` é usado para campos de entrada que devem conter uma cor. Dependendo do navegador utilizado, um seletor de cores pode aparecer no campo de entrada.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo color</title>
    </head>
    <body>
        <form>
            <label for="selecionaCor">Selecionar a sua cor favorita:</label>
            <input type="color" id="selecionaCor" name="selecionaCor" value="#ff0000">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type date

O `<input type="date">` é usado para campos de entrada que devem conter uma data. Dependendo do navegador, um seletor de datas pode aparecer no campo de entrada.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo date</title>
    </head>
    <body>
        <h1>Exemplo de input type date</h1>
        <form>
            <label for="nascimento">Data de nascimento:</label>
            <input type="date" id="nascimento" name="nascimento">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type email

O `<input type="email">` é usado para campos de entrada que devem conter um endereço de email. Dependendo do navegador, o endereço de email pode ser validado automaticamente quando enviado. Alguns dispositivos móveis reconhecem o tipo de email e adicionam ".com" ao teclado para corresponder à entrada de email.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo date</title>
    </head>
    <body>
        <h1>Exemplo de input type email</h1>
        <form>
            <label for="email">Digite seu email:</label>
            <input type="email" id="email" name="email">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type file

O `<input type="file">` define um campo de seleção de arquivo e um botão "Procurar" para upload de arquivos.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo date</title>
    </head>
    <body>
        <h1>Exemplo de input type file</h1>
        <form>
            <label for="arquivo">Selecione um arquivo:</label>
            <input type="file" id="arquivo" name="arquivo"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type month e week

O `<input type="month">` permite ao usuário selecionar um mês e ano, enquanto o `<input type="week">` permite ao usuário selecionar uma semana e ano.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo month</title>
    </head>
    <body>
        <h1>Exemplo de input type month</h1>
        <form>
            <label for="diames">Aniversário (dia e mês):</label>
            <input type="month" id="diames" name="diames">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo month</title>
    </head>
    <body>
        <h1>Exemplo de input type month</h1>
        <form>
            <label for="semana">Semana:</label>
            <input type="week" id="semana" name="semana">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type search

O `<input type="search">` é usado para campos de pesquisa (que se comporta como um campo de texto comum).

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo search</title>
    </head>
    <body>
        <h1>Exemplo de input type search</h1>
        <form>
            <label for="pesquisa">Pesquisar:</label>
            <input type="search" id="pesquisa" name="pesquisa">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type tel

O `<input type="tel">` é usado para campos de entrada que devem conter um número de telefone.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo tel</title>
    </head>
    <body>
        <h1>Exemplo de input type tel</h1>
        <form>
            <label for="telefone">Enter a phone number:</label><br><br>
            <input type="tel" id="telefone" name="telefone" placeholder="(99)99999-9999" pattern="\([0-9]{2}\)[0-9] {5}-[0-9]{4}" required><br><br>
            <small>Formato: (99)99999-9999</small><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

- O atributo `pattern` contém a expressão regular (o formato) que valida a entrada de um telefone.

### Input type time

O `<input type="time">` permite ao usuário selecionar um horário (sem fuso horário).

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo time</title>
    </head>
    <body>
        <h1>Exemplo de input type time</h1>
        <form>
            <label for="horario">Selecione um horário:</label>  
            <input type="time" id="horario" name="horario">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type url

O `<input type="url">` é usado para campos de entrada que devem conter um endereço de URL. Dependendo do navegador, o campo de URL pode ser validado automaticamente quando enviado. Alguns dispositivos móveis reconhecem o tipo de URL e adicionam ".com" ao teclado para corresponder à entrada de URL.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo URL</title>
    </head>
    <body>
        <h1>Exemplo de input type URL</h1>
        <form>
            <label for="homepage">Insira a sua homepage:</label>
            <input type="url" id="homepage" name="homepage">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

### Input type hidden

O `<input type="hidden">` define um campo de entrada oculto. Um campo oculto permite que os desenvolvedores da Web incluam dados que não podem ser vistos ou modificados pelos usuários quando um formulário é enviado. Um campo oculto geralmente armazena o registro do banco de dados que precisa ser atualizado quando o formulário é enviado.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo hidden</title>
    </head>
    <body>
        <h1>Exemplo de input type hidden</h1>
        <form>
            <label for="Pnome">Nome:</label>
            <input type="text" id="Pnome" name="Pnome"><br><br>
            <input type="hidden" id="cliId" name="cliId" value="1628">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

- Embora o input type hidden não seja visível no navegador, ao clicar no botão Submit, os valores inseridos pelo usuário (do input text) e do hidden (do input hidden) serão enviados ao servidor.

### Input type image

O `<input type="image">` define uma imagem como um botão de envio. O caminho para a imagem é especificado no atributo src.

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exemplo image</title>
    </head>
    <body>
        <h1>Exemplo de input type image</h1>
        <form>
            <label for="nome">Nome: </label>
            <input type="text" id="nome" name="nome"><br><br>
            <input type="image" src="01_imgs/imagem_submit.gif" alt="Submit" width="48" height="48">
        </form>
    </body>
</html>
```

## Tabelas

- `<table> ... </table>` - Indica o início e o fim da tabela.
- `<caption> título </caption>` - Define o título da tabela (opcional).
- `<tr> ... </tr>` - Início e fim de uma linha da tabela (Table Row).
- `<td> ... </td>` - Início e fim da célula que compõe a linha, divide a linha em colunas (Table Data).
- `<th> ... </th>` - Início e fim da célula do cabeçalho (Table Header).

```
<table>
    <tr>
        <th>Mês</th>
        <th>Custo</th>
    </tr>
    <tr>
        <td>Janeiro</td>
        <td>R$100</td>
    </tr>
    <tr>
        <td>Fevereiro</td>
        <td>R$80</td>
    </tr>
    <tr>
        <td>Soma</td>
        <td>R$180</td>
    </tr>
</table>
```

Os parâmetros possíveis para a tag `<table>` são: `COLSPAN`, que mescla células horizontais adjacentes. Se for atribuído COLSPAN=2 a uma célula, esta célula ocupará o seu espaço e o da próxima célula; `ROWSPAN`, quem escla células verticais adjacentes. Se for atribuído ROWSPAN=2 a uma célula, esta célula ocupará o seu espaço e o da célula abaixo; `WIDTH`, que especifica a largura de uma célula que pode ser definida em pixels ou em percentual referente à largura da tabela.
