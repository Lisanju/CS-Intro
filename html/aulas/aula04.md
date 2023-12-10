# Formulários e tabelas

## Formulários

Os formulários são utilizados para a interação entre um usuário e o servidor, possibilitando a troca de dados ou informações.

`<form> ... </form>`

Um formulário HTML contém elementos de formulário, que são diferentes tipos de entrada, como campos de texto, caixas de seleção, botões de opção e botões de envio.

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

