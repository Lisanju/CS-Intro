# Manipulação de datas com Moment.js

No desenvolvimento web front-end, uma das tarefas que o desenvolvedor costuma se deparar, e até subestimar, é a exibição e manipulação de datas, horários e similares. O problema ocorre pois às vezes queremos facilitar a exibição de uma informação ao usuário. Por exemplo, nossos sistemas sabem sem problema que uma foto foi cadastrada no dia 02/04/2020 às 19:31:22. Mas e se quisermos exibir que dia da semana era? Segunda-feira? Terça-feira? E caso queiramos saber quanto tempo se passou desde então? "23 dias, 18 horas e 14 minutos"?

Enfim, como podemos fazer esse tipo de manipulação de forma mais "fácil"? Precisamos mesmo criar um algoritmo específico para isso? Não! Graças a biblioteca Moment.js, podemos realizar operações de manipulação de datas avançadas de maneira simples e sem complicação.

# Moment.js

A biblioteca javascript Moment.js pode ser acessada na sua sua página inicial https://momentjs.com/.

A biblioteca Moment.js é uma biblioteca do tipo stand-alone, onde não é necessário nenhuma outra biblioteca auxiliar para ser utilizada.

A biblioteca vem em dois sabores diferentes: com informações de localização (chamado de internacionalização - il8n) ou sem tal opção. Caso o desenvolvedor use a versão com il8n, pode-se realizar operações como imprimir informações na linguagem escolhida, possibilitando o uso de palavras como "fevereiro", "agosto", "segunda-feira", "sunday" e etc.

## Como importar a biblioteca?

Há duas formas confiáveis de realizar a importação da biblioteca em seu arquivo HTML: baixando o arquivo da biblioteca ou usando um CDN.

### Baixando o arquivo

Nessa opção, a versão atual da biblioteca deve ser manualmente baixada e colocada em uma pasta próxima do arquivo HTML sendo desenvolvido. Há duas opções, uma usando o locale e outra sem tal opção.

Versão sem locale: https://momentjs.com/downloads/moment.min.js

Versão com locale: https://momentjs.com/downloads/moment-with-locales.min.js

Após baixado os arquivos, você pode importar a biblioteca usando uma tag script tal como:

`<script src="moment.js.min"></script>`

Ou, usando o locale:

`<script src="moment-with-locales.min.js"></script>`


### Usando um CDN

Caso você opte por usar um CDN, ou seja, aproveitar-se da banda de um terceiro, você pode usar o servidor https://cdnjs.com/libraries/moment.js/.

Nesse caso, basta incluir os seguintes comandos em seu HTML:

`<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.27.0/moment.min.js"></script>`

Ou, sua versão com locales:

`<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.27.0/moment-with-locales.min.js"></script>`

### Usar locale ou não?

A pergunta é válida por um motivo simples: o uso da versão locale adiciona cerca de 4 vezes o tamanho da biblioteca na página final. Embora a diferença seja menos de 50Kb, algo que pode ser ignorado na maioria da vezes, é sempre bom reduzir o tamanho de um site caso seja possível.

Na dúvida, use a versão com locale. O peso extra não é muito grande e no geral vale a pena. O uso da versão base da biblioteca sem locale é recomendável apenas quando você quiser fazer manipulações numéricas com datas e não convertê-las em formato "textual". Em sites profissionais, uma forma de desenvolver é a de usar a versão básica e, somente quando for detectada a necessidade de usar a versão completa, trocar para a versão com locale.

Lembre-se, caso opte por locale, de setar a linguagem que deseja utilizar antes de utilizar a biblioteca. Para isso, você pode utilizar o comando:

`moment.locale("pt-br"); // Informa a biblioteca para usar a localização 'pt-br'`

Você pode utilizar as outras linguagens disponíveis e/ou modificar a linguagem a qualquer momento. Caso não seja setado o locale, será utilizado a versão inglesa dos Estados Unidos.

### Usar CDN ou arquivo local?

Em 99,99% dos casos, a melhor opções é usar um CDN. A única opção onde um arquivo local talvez possa fazer mais sentido é quando você quer desenvolver um site localmente com um sistema offline, com banda limitada, ou onde seu navegador está com o cache desativado.

Nesse link, você pode ver bons motivos para usar um CDN: https://www.globaldots.com/blog/9-benefits-using-cdn

# Criando um objeto moment

Em geral, o primeiro passo ao usar a biblioteca Moment é criar um objeto próprio dela. Esse objeto representa um momento na linha temporal, como um determinado horário de um determinado dia.

No seu modo mais simples, basta atribuir a uma variável o valor da função moment(), que retornará então o tempo AGORA para a variável. Exemplo:

`var agora = moment();`

Em vários casos, porém, gostariamos de manipular alguma data ou horário que não seja imediatamente AGORA (por exemplo, para calcular quantos dias faltam para um determinado evento). Ou seja, queremos que a variável aponte para uma data futura ou passada para ser manipulada.

Nesse caso, existem diversas formas. Em geral, basta passar como parâmetro para a função moment() uma string contendo a descrição da data e/ou horário. Por padrão, a biblioteca tentará fazer o parser usando padrão ISO-8061 (https://en.wikipedia.org/wiki/ISO_8601). Exemplo:

`var data = moment("2020-08-01 14:32:13"); //Cria um momento no dia 01/08/2020 as 14h, 32m e 13s`

Em geral, o formato ISO-8061 é amplamente utilizado e deve funcionar adequadamente bem na maioria dos casos. Porém, a biblioteca permite o uso de um parser complexo definido pelo próprio desenvolvedor.

Por exemplo, considere o seguinte formato de data, indicando o dia 13 de fevereiro de 2020, as 18h, 24m e 21s.

`13 Fev. 20 18-24-21`

Como podemos perceber, a string acima está fora do formato ISO-8601. Podemos, porém, realizar o parser de tal horário usando o seguinte comando:

`var data = moment("13 Fev. 20 18-24-21", "DD MMM YY HH-mm-ss");`

Existem uma combinação diferentes para definir o formato desejado para a data/hora. Para mais informações, consulte as tabelas de configurações na documentação oficial: https://momentjs.com/docs/#/parsing/string-format/

# Alterar um momento

Após criado um objeto de data e/ou hora no Moment, podemos alterar o momento em si usando métodos do tipo Get (obter o valor) e Set (alterar o valor).

Por exemplo, considere o seguinte momento no tempo, parseado usando o ISO-8061

var data = moment("2020-08-01 14:32:13"); //Cria um momento no dia 01/08/2020 as 14h, 32m e 13s

A seguir, algumas alterações possíveis:

- Horas

```
data.hour(21); // Altera a hora para 21h
data.hour(); //Retorna 21
data.set("hour", 13); //Altera a hora para 13h
data.get("hour"); // Retorna 13
```

- Minutos

```
data.minute(13); // Altera os minutos para 13m
data.minute(); // Retorna 13
data.set("minute", 22); // Altera os minutos para 22m
data.get("minute"); // Retorna 22
```

- Segundos

```
data.second(13); // Altera os segundos para 13s
data.second(); // Retorna 13
data.set("second", 22); // Altera os segundos para 22s
data.get("second"); // Retorna 22
```

- Ano

```
data.year(2013); // Altera o ano para 2013
data.year(); // Retorna 2013
data.set("year", 1090); // Altera o ano para 1090
data.get("year"); // Retorna 1090
```

- Mês

```
data.month(0); // Altera o mês para Janeiro
data.month(); // Retorna 0
data.month("Dezembro"); // Altera o mês para dezembro (11)
data.month("Jun"); // Altera o mês para junho (5)
data.set("month", 3); // Altera o mês para abril
data.get("month"); // Retorna 3
```

- Dia

```
data.date(21); // Altera o dia para 21
data.date(); // Retorna 21
data.set("date", 1); // Altera o dia para 1
data.get("date"); // Retorna 1
```

# Manipular um momento

Já sabemos como criar um momento específico no tempo e também como modificá-lo em termos de dias, horas, minutos, etc.

Porém, e se quisermos adicionar ou remover alguma unidade de tempo do nosso momento? Dado o momento atual, podemos por exemplo colocar mais dez minutos para que uma determinada ação ocorra? Poderíamos fazer algo assim:

```
let data = moment(); // Cria um momento agora
let minutos = data.get("minute"); // Obtém os minutos do horário
data.set("minute", minutos+10); // Soma dez minutos ao horário
```

Apesar de funcionar, é pouco eficiente. Uma opção melhor é:

Manipular o momento significa adicionar ou remover uma certa quantidade de tempo de um objeto momento. O código abaixo, por exemplo, adiciona 3 dias ao momento.

```
let agora = moment();
agora.add(3, "days");
```

Também podemos remover um tempo de um objeto momento. Por exemplo, podemos visualizar esse exato momento no ano passado usando...

```
let agora = moment();
agora.subtract(1, "years");
```

Podemos encadear os acréscimos ou decréscimos de datas/horas em uma única instrução:

```
let agora = moment();
agora.add(3,"days").add(2,"hours").subtract(1,"months")
```

Para reduzir o tamanho das instruções e facilitar o desenvolvimento dessas manipulações, podemos usar as versão abreviadas de minutos, dias, segundos, anos e similares conforme a tabela a seguir:

![image](https://github.com/Lisanju/CS-Intro/assets/106002045/e58e62f7-1c22-4cd2-9e7b-c822872c02dc)

# Exibir um momento

Depois de todas as alterações e manipulações realizadas, é comum termos que exibir ou mostrar a nova data/hora para o usuário. Nesse caso, podemos usar os vastos recursos da Moment.js para obtermos uma forma agradável de exibir as informações.

A formatação do formato de saída de um moment é dada usando o método `format()`.

```
moment().format();
moment().format(String);
```

Caso não seja passado nenhuma string como parâmetro, é utilizado o padrão ISO 8601 para expressar o momento. Como exemplo:

```
moment.format(); //Imprime --> "2020-08-01T16:02-05:00"
```

Já a segunda opção (passagem de parâmetro String para o método) modifica a saída de forma customizável. Considere os seguintes exemplos:

```
var data = moment();
data.format("dddd, MMMM D YY, hh:mm:ss a"); // Retorna "Sábado, Agosto 1 20, 04:23:19 am"
data.format("ddd, HH"); // Retorna "Sáb, 23"
data.format("[Hoje é] DD [de] MMMM [de] YYYY"); //Retorna "Hoje é 01 de Agosto de 2020"
data.format("LL"); // Retorna "Agosto 1, 2020"
data.format("L"); // Retorna "01/08/2020"
```

A lista de opções de formatação é extensa, incluindo opção como antes e depois de cristo, anos estendidos, dias do ano, quadrimestres e muitos outros. Note que várias das opções mencionadas necessitam do uso correto da versão com locale estabelecido. A lista completa com todas as opções de formatação pode ser acessada em: https://momentjs.com/docs/#/displaying/format/

# Customização e outros usos avançados

Por fim, além dos recursos mencionados, a biblioteca Moment.js conta com recursos mais avançados que permite um grande grau de customização dos resultados pelo desenvolvedor.

### Comparação entre momentos

É possível comparar se dois momentos são iguais ou um depois do outro. Veja os exemplos a seguir:

```
moment("2020-12-01").isBefore("2020-12-02"); // True
moment("2020-12-02").isSame("2020-12-03"); // False
moment("2020-10-20").isAfter("2020-10-19"); // True
moment("2020-01-01").isBetween("2019-12-31", "2020-12-31"); // True
moment([2020]).isLeapYear(); // True (checa se o ano é bissexto)
```

### Customização de um locale

É possível modificar as informações do locale de acordo com o desejado. Por exemplo:

```
moment.updateLocale("pt-br", {
    monthsShort : [ 
        "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"
    ]
});
```

Altera a forma abreviada do locale pt-br dos meses do ano (jan...dez) para (m1...m12).

Existem muitas opções de customização. Você pode conferir mais detalhes e outras informações em https://momentjs.com/docs/#/customization/
