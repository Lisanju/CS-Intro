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

