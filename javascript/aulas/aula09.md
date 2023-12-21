# JSON e AJAX

Uma das necessidades básicas da web é a troca de mensagens entre computadores diferentes, considerando diferentes programas, sistemas operacionais e hardwares.

Como fazer a comunicação ser efetiva, tanto para o computador quanto para os humanos?

### XML

É de fácil leitura pros humanos. Um computador consegue compreender facilmente. Porém, desperdiça muito espaço para representar dados.

```
<biblioteca>
   <livro>
      <autores>
         <autor>Ingrid</autor>
         <autor>Paulo</autor>
      </autores>
      <titulo>O livro</titulo>
      <ano>1998</ano>
   </livro>
   <livro>
      <autores>
         <autor>Paulo</autor>
         <autor>Antônia</autor>
      </autores>
      <titulo>A história</titulo>
      <ano>2016</ano>
   </livro>
</biblioteca>
```

### Arquivos binários

Rápido e econômico, além dos computadores conseguirem lidar facilmente com eles. Porém, podem ser criados sem qualquer padrão, deixando de funcionar em alguns casos. E nenhum ser humano consegue ler.

```
101010001010010101110111000100011100
011011100011110011010101011001101010
100110101010101010101010101010000010
101011111000001101101010101010101010
111111100101010101001000101010100101
010101010101010101010101110101010101
01010101010101111110000000
```

### JSON

Inspirado em XML, é padronizado o suficiente para ser compreendido pelos computadores e humanos. É enxuto o suficiente, não precisando transmitir dados desnecessários. É baseado na representação de objetos de JavaScript, mas que pode ser usado em qualquer outra linguagem.

Imagine a seguinte informação.

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/5a6d3c0b-1cb8-418b-b6bf-8550e19a1d63)

Usando XML teríamos:

```
<nome>Sherlock</nome>
<sobrenome>Holmes</sobrenome>
<profissao>Detetive</profissao>
<telefone>5555-1234</telefone>
```

Usando JSON teríamos:

```
{
"nome": "Sherlock",
"sobrenome": "Holmes",
"profissao": "Detetive",
"telefone": "5555-1234"
}
```

## Formato de arquivo

Os dados são organizados em pares, chamados de chave e valor, separados por dois pontos.

`{"chave" : "valor"}`

Os `{ }` representam um objeto.

```
{"nome" : "maria"}      // Um objeto
{"nome" : "josé"}      // Outro objeto
{"nome" : "joão"}      // Mais outro objeto
```

Os `[ ]` representam um vetor ou conjunto de dados.

```
[
   {
   "nome": "maria"
   },
   {
   "nome": "joão"
   },
   {
   "nome": "josé"
   }
]
```

## Valores possíveis

Um valor pode ser: string, número, true/false, null, Objeto ou Array.

Apenas strings devem estar entre aspas duplas.

```
{
   "nome": "Moriarty",
   "idade": 34,
   "profissao": "Gênio do crime",
   "vivo": true,
   "extra": [
      1234.65,
      false,
      "vivo",
      {
      "ajudantes": 0
      }
   ]
}
```

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/583cc329-cd4c-438e-88ae-5a7434635f52)

## JSON com JavaScript

```
var pessoa = '{"nome" : "Moriarty", "idade" : 34}';
var json_convertido = JSON.parse(pessoa);

console.log(pessoa);
console.log(json_convertido);
```

O `JSON.parse(string);` converte uma string no formato JSON para um objeto em JavaScript.

Depois de ser convertido em objeto, os dados podem ser acessados facilmente pelo JavaScript.

```
var pessoa='{"nome":"Moriarty","idade":34,"profissao":"Gênio do crime"}';
var json_convertido = JSON.parse(pessoa);

console.log(json_convertido.nome);
if(json_convertido.idade > 18) {

console.log("Maior de idade!");

} else {

console.log("Menor de idade!");

}
console.log(json_convertido.profissao);
```

Com `JSON.stringify(objeto)`, um objeto também pode ser transformado em JSON.

```
var objeto_pessoa = {
   "nome : "Moriarty",
   "idade" : 34,
   "profissao" : "Gênio do crime"
}

var json_string = JSON.stringify(objeto_pessoal);
console.log(json_string);
```

## AJAX

AJAX (Asynchronous JavaScript and XML) é um conjunto de tecnologias utilizada por sites modernos, permitindo iterações rápidas e fluídas ao usuário.

- Síncrono: o próximo comando/instrução só é executado quando o comando/instrução atual for finalizado. Por exemplo, o site carrega apenas quando todos os dados estão carregados.

- Assíncrono: permite que a próxima instrução/comando execute mesmo enquanto o comando atual está sendo executado. Por exemplo, exibir a lista de amigos, mesmo se a lista ainda não está totalmente carregada.

Para realizar uma requisição usando o AJAX com JavaScript puro é necessário implementar diversas instruções, sendo bem mais complicado do que deveria:

```
<!DOCTYPE html>
<html>
<body>

<h2>The XMLHttpRequest Object</h2>
<h3>Start typing a name in the input field below:</h3>

<p>Suggestions: <span id="txtHint"></span></p> 
<p>First name: <input type="text" id="txt1" onkeyup="showHint(this.value)"></p>

<script>
function showHint(str) {
  if (str.length == 0) { 
    document.getElementById("txtHint").innerHTML = "";
    return;
  }
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("txtHint").innerHTML =
    this.responseText;
  }
  xhttp.open("GET", "gethint.php?q="+str);
  xhttp.send();   
}
</script>

</body>
</html>
```

Felizmente, o jQuery oferece vários comandos específicos para AJAX. Alguns comandos mais simples para casos comuns. Uma requisição completa, com todos os recursos possíveis.

## JSON com jQuery

Podemos obter e processar arquivos JSON usando a seguinte função:

`$.getJSON(url, dados, funcao_para_tratamento);`

Os dados obtidos são automaticamente convertidos de JSON para objetos JavaScript.

Por exemplo:

`$.getJSON("pagina_de_exemplo.php", funcao_para_tratamento);`

url: “site.php”, “pagina_externa.html”, “http://webservice.com/acessar.php”.

dados (opcional): “idade=10”, “nome=ifsp”, “op=cadastro&nome=web&q=10+90”.

funcão_para_tratamento:

```
function funcao_para_tratamento(dados) {
   console.log(dados.nome);
   console.log(dados.idade);
   console.log(dados.profissao);
}
```

Os dados retornados pelo endereço podem ter vários objetos. Nesse caso, é necessário percorrer os objetos como no exemplo abaixo:

```
function funcao_para_tratamento(dados) {
   for (var i = 0; i < dados.length; i++) {
      console.log(dados[i].algo);
      console.log(dados[i].outro_algo);
   }
}
```

Os dados podem ser percorridos também usando o método each do jQuery (para objetos).

```
function funcao_para_tratamento(dados) {
   $.each(dados, function(chave, valor) {
      console.log("O valor de " + chave + " é " + valor);
   });
}
```

## AJAX com jQuery

O jQuery oferece um método .ajax bastante flexível, capaz de suportar diversas configurações diferentes. Todas as opções são opcionais.

```
$.ajax({
   url: 'http://www.algumsite.com', // Destino. Pode ser externo (site) ou local (arquivo)
   type: 'POST', // O método de envio. GET ou POST
   data: {// As informações que deseja-se enviar. Objeto transforma-se em JSON
      "nome": "Mickey Mouse",
      "idade": 18
   },
   async: true, // Se a requisição é assíncrona (true - padrão) ou não (false)
   success: function(msg) {
      // Faz algo quando a resposta foi recebida. msg é entendido como json.
      processaResposta(msg);
   },
   error: function(request, status, erro) {
      // Faz algo quando houve algum erro.
      alert(erro);
   }
});
```

### Type

No protocolo HTTP são previstas diversas formas de comunicação entre um cliente e o servidor. Esses métodos são chamados de verbos HTTP (HTTP Verbs). Entre eles:

- GET;
- HEAD;
- POST;
- PUT;
- DELETE.

Cada verbo tem uma finalidade própria, embora possam ser usadas de maneira intercambiável. Mais informações em: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods

Os métodos mais utilizados são GET e POST.

- GET: Passagem de valores pelo endereço (head) da mensagem. Possui tamanho máximo fixo. É de fácil manipulação, inclusive por um usuário comum. Inadequado para diversos tipos de informações sensíveis, como senhas, endereços de email e outros.

- POST: Passagem de valores pelo corpo (body) da mensagem. Não possui um tamanho máximo. Mais difícil de ser manipulado. Inadequado para identificar o estado ou página particular de um website.

Note que uma mesma requisição pode conter tanto parâmetros GET quanto POST.

```
$.ajax({
   url: 'http://www.algumsite.com?id=10&op=cadastrar',      // Parâmetro GET
   type: 'POST',
   data: "local=sao+carlos&estado=sao+paulo&pais=brasil"   // Parâmetro POST
});
```

### getJSON x AJAX

Qual a diferença entre os métodos getJSON e AJAX?

1. O AJAX suporta qualquer tipo de resposta (HTML, XML, JSON). O getJSON espera apenas um JSON.

2. getJSON não possui diversos campos (como o error do AJAX).

3. getJSON utiliza apenas o método GET. Já o AJAX suporta os demais métodos ou verbos HTTP.

Na dúvida, use o método AJAX.

Além disso, para facilitar, além do método AJAX, existem dois métodos auxiliares para os métodos GET e POST.

```
$.get("http://site_externo.com/cadastrar.php","pm1=val1&pm2=val2", function(data) {
   // Código a ser executado quando o resultado for obtido
});

$.post("outro_site.php", function(data) {
   // Código a ser executado quando o resultado for obtido
});
```

Ambos os métodos são similares ao getJSON, mas suportam qualquer tipo de retorno (e não apenas JSON).
