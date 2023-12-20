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
