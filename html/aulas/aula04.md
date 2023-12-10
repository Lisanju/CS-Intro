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

## Tabelas

