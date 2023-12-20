# RESTFull API

Neste conteúdo, trataremos de uma questão bastante importante no desenvolvimento web moderno, relacionado ao webservices. Ao contrário de sites tradicionais, um webservice trata-se de um sistema web onde as respostas seguem um determinado protocolo, e os dados são devolvidos ao requerente sem qualquer informação gráfica (ou seja, não é composto de HTML + CSS + JS). Esse tipo de informação é extremamente útil para a criação de sistemas backend que respondem a requisições de um computador, de uma tv, de um celular, etc.


Vamos conhecer um dos formatos mais populares de webservice, chamado de REST, e aprender algumas de suas principais características.

## Comunicação com webservice

No mundo moderno o usuário pode acessar conteúdos online usando celulares, TVs, computadores e outros dispositivos. Nesse caso, um sistema que "funciona mal" em determinada situação pode ter problemas de aceitação e perder sua clientela com o passar do tempo. O uso de diferentes dispositivos e em diferentes situações leva a um maior custo de desenvolvimento. Afinal, quanto maior a gama de dispositivos a serem considerados, maior o número de testes a executar e mais "complexo" torna-se a interface.



Considere por exemplo a rede social Facebook. Caso você acesse pelo navegador de seu computador, você verá um website adaptado para as necessidades de um computador. Uma equipe desenvolveu o sistema precisamente para atender suas necessidades, incluindo trocas de mensagens entre o cliente/servidor e todo o backend, como banco de dados e similares. Há uma equipe inteira para desenvolver e manter o site funcionando.

Agora, imagine o aplicativo em celulares iOS ou Android. Sua interface é completamente diferente, com comportamento também diferente. Mas ambos têm o mesmo objetivo. Ou seja, precisam realizar a comunicação entre o cliente e servidor, armazenar dados no banco de dados, etc.

Note que há muitas similaridades entre a versão do website e outra do aplicativo. O funcionamento básico é o mesmo. A maior diferença é, realmente, a interface da aplicação. Isso quer dizer que é possível, a algum nível, usar um mesmo backend, e mudar apenas o frontend de acordo com a necessidade.

Uma das formas mais fáceis e comuns de realizar isso é por meio do uso dos chamados webservices (serviços web, em tradução livre). Um webservice tem como principal diferença de um site normal o fato de não ter qualquer informação sobre a interface do sistema. Usando um webservice adequado, não importa o dispositivo ou a forma de visualização, podemos criar sistemas compatíveis entre si com interfaces diferentes sobre os mesmos dados! A princípio, um webservice nem sequer precisa de uma interface gráfica!

Exemplos de webservices podem ser visualizados a todo o momento em apps diversos como Uber, Facebook e similares. Ao fazer o download de um app do tipo, apenas a interface da aplicação ficará contida no celular. A lógica de negócio e todas as iterações são realizar por um webservice específico. Nesse sentido, o webservice se torna uma API a ser utilizada por diferentes aplicações. A imagem a seguir ilustra o uso do webservice como uma API para outras interfaces/API.

## REST API

Um webservice pode ser desenvolvido de diferentes formas, com vantagens e desvantagens diferentes conforme o método adotado. A princípio, existiam poucos padrões de como um webservice deve ser construído, quais informações deve enviar ao cliente, etc.

Um exemplo de webservice criado é o SOAP, inicialmente chamado de XML-RPC, criado em 1998 por pesquisadores da Microsoft.

Já em 2000, Roy Fielding propôs em sua tese de doutorado (ver https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) um modelo de API web baseada em HTTP customizável e flexível chamada de REST (REpresentational State Transfer). O modelo proposto não impõe nenhuma regra de como o serviço deve ser implementado (por exemplo, qual a linguagem de programação adotada). Roy, porém, especificou seis diretivas básicas da API REST, explicadas a seguir:

- Comunicação cliente-servidor: deve haver uma separação entre o cliente (que somente conhece os endereços dos recursos) e o servidor (que somente recebe e processa os dados). O cliente deve poder ser modificado/evoluído sem qualquer modificação no servidor.
- Sem estado (stateless): cada requisição do cliente deve conter TODAS as informações necessárias para processar a requisição. Não é usado variáveis de ambiente ou conhecimento de contexto no lado do servidor (embora possa ser utilizado, e até recomendável, no lado do cliente).
- Cacheável: os recursos que puderem ser cacheáveis assim o devem ser. Isso evita o excesso de comunicação entre cliente-servidor.
- Interface uniforme: a interface de comunicação e de mensagem deve ser padronizada e adotada no webservice inteiro, de forma lógica e sucinta.
- Sistema em camadas: a interface de comunicação deve ser utilizada em camadas, onde um recurso ou componente não tem acesso direto e/ou imediato a outras camadas próximas.
- Código sobre demanda (opcional): o cliente pode ter sua funcionalidade estendida por meio do download de novos trechos de códigos a serem executados, facilitando o deploy de aplicações.

Popularmente, uma API REST que faz uso de todos os recursos (menos o sexto, opcional) é dito RESTFull.

A grande vantagem do uso de uma API REST é que, após ser entendida, grande parte dos outros webservices REST pode ser compreendida mais facilmente.

## Recursos 

O principal objetivo e foco do REST é o de receber e enviar ao cliente os chamados recursos. Um recurso é uma unidade de informação básica, composta de diferentes campos e seus valores.

Uma representação aproximada de um recurso REST é um objeto utilizado em programação orientada-a-objetos ou a uma tabela em um banco de dados relacional. 

Por exemplo, considere um recurso do tipo "pessoa". Esse recurso possui diferentes atributos/valores possíveis de acordo com a necessidade da aplicação, como por exemplo:

- email
- idade
- sexo
- data_cadastro
- id

Essas informações devem ser acessíveis toda vez que um recurso "pessoa" específico seja solicitado pelo cliente. Ou seja, um recurso "completo" é enviado do servidor ao cliente.

Na prática costuma-se representar um recurso usando alguma linguagem como JSON ou XML para atender aos requisitos de uniformidade. Assim, ao requisitar uma "pessoa" ao servidor, uma possível resposta poderia ser:

```
{
   "id": 5,
   "email": "teste@ifsp.edu.br",
   "sexo": "M",
   "data_cadastro": "04/08/2020",
   "idade": 72
}
```

## Verbos HTTP

A API REST faz uso extensivo dos verbos HTTP, sendo inclusive erroneamente confundido com o protocolo em alguns casos. 

A REST utiliza os verbos pré-definidos do HTTP para identificar quais operações estão sendo realizadas sobre um determinado recurso. Os verbos HTTP utilizados pelo REST e seus usos são:

- GET - Verbo utilizado para requisitar um recurso da API.
- POST - Verbo utilizado para criar um novo recurso.
- PUT - Verbo utilizado para atualizar um recurso específico.
- PATCH - Verbo utilizado para atualizar uma parte de um recurso específico.
- DELETE - Verbo utilizado para deletar um recurso.

É importante frisar que nem todos os métodos são adotados da forma inicialmente especificada. Por exemplo, é comum usar apenas o PUT para editar um recurso (ignorando o PATCH). Em geral, porém, é bastante incomum suprimirem os métodos GET e POST.

## Exemplos de requisições

Considere um sistema web implementado no lado servidor que possua um recurso básico chamado de pessoa e que possua os seguintes campos/atributos:

- id
- email
- sexo
- idade
- data_cadastro

Considere ainda que nosso webservice usando a REST API esteja hospedada em "http://endereco/". Com isso, podemos definir o formato básico da interação conforme os tópicos a seguir.

### Requisição de recurso

Para obtermos um recurso usamos o verbo GET. Para obtermos uma lista de todas as pessoas, realizamos uma consulta GET para o endereço "http://endereco/pessoa" que retornará algo como o seguinte:

```
{
    "status": 200,
    "data": [
        {
            "id": 1,
            "email": "teste@ifsp.edu.br",
            "data_cadastro": "01/01/2020",
            "sexo": "F"
        },
        {
            "id": 2,
            "email": "teste2@ifsp.edu.br",
            "data_cadastro": "01/01/2020",
            "sexo": "M"
        },
        {
            "id": 3,
            "email": "noemail@gmail.com",
            "data_cadastro": "23/04/2017",
            "sexo": "M"
        }
    ]
}
```

Caso queiramos os dados de uma pessoa específica, podemos usar sua chave primária (normalmente conhecida como ID) na requisição. Assim, a pessoa com id=5 pode ser obtida com uma requisição GET para "http://endereco/pessoa/5".

```
{
    "status": 200,
    "data": [
        {
            "id": 5,
            "email": "aindaexiste@yahoo.com",
            "data_cadastro": "23/04/1998",
            "sexo": "M"
        }
    ]
}
```

Veja que a resposta é basicamente a mesma. A única diferença é o número de "pessoas" retornado pelo sistema.

### Cadastrar um recurso

Para cadastrar um novo recurso no sistema, usamos o verbo POST. Assim, enviamos os dados em um formato pré-estabelecido para o servidor no endereço "http://endereco/pessoa".

```
{
    "email": "testenovo@outlook.com",
    "data_cadastro": "23/04/2019",
    "sexo": "M"
}
```

Uma possível resposta, a ser enviada pelo servidor indicando o sucesso, é exibida a seguir:

```
{
    "status": 201
}
```

Atenção: Note que alguns desenvolvedores recomendam que após o cadastro seja retornado alguma informação que aponte ao novo recurso adicionado ao website, tal como:

```
{
    "status": 201,
    "id": 10
}
```

ou 

```
{
    "status": 201,
    "recurso": "http://endereco/pessoa/10"
}
```

### Atualização de um recurso

Para atualizar um recurso, temos duas opções usando o PATCH ou o PUT. O endereço de requisição ("http://endereco/pessoa/id", onde id é o número que identifica o recurso) é comum a ambos os verbos.

Caso usemos o POST, devemos especificar TODOS os campos do recurso e seu valor modificado.

```
{
    "email": "testenovo@outlook.com",
    "data_cadastro": "23/04/2019",
    "sexo": "M"
}
```

Já no caso do PATCH, podemos especificar apenas alguma(s) parte do recurso em si, como por exemplo a correção do "sexo" de uma pessoa:

```
{
    "sexo": "F"
}
```

Note que ambos os métodos devem saber QUAL o recurso a ser atualizado, por isso é imprescindível o envio da informação de indexação na url ("http://endereco/pessoa/10", por exemplo).

A resposta possível de um servidor se a requisição for bem sucedida é:

```
{
    "status": 200
}
```

### Remover um elemento

Para removermos um elemento, basta enviar uma requisição usando o verbo DELETE para o endereço "http://endereco/pessoa/id", onde id é o número que identifica o recurso.

Note que, a princípio não é necessário que o corpo da mensagem contenha qualquer conteúdo (afinal, pedir para DELETAR um id específico é auto-explicativo). Caso seja bem sucedido, o servidor pode responder algo como:

```
{
    "status": 200
}
```

## Código de status

Como você deve ter percebido anteriormente, a maioria das requisições têm como resposta um parâmetro chamado de "status". Tal parâmetro é opcional, mas pode ser usado para indicar o status da requisição sendo realizada.

Ao invés de criarmos nossos próprios códigos de status, podemos usar os códigos de status do protocolo HTTP. No link a seguir, você encontra todos os códigos estabelecidos: https://cheatography.com/kstep/cheat-sheets/http-status-codes/

Dentre todos esses códigos, alguns são mais utlizados do que outros. A seguir (baseado no link https://codeburst.io/know-your-http-status-a-cheat-sheet-for-http-status-codes-5fb43863e589) foram copiados alguns dos status mais comuns e seu significado.

- 200 — OK: Ok. The request went fine and the content requested was returned. This is normally used on GET requests

- 201 — Created: The resource was created and the server has acknowledged it. It could be useful on responses to POST or PUT requests. Additionally, the new resource could be returned as part of the response body.

- 204 — No Content: The action was successful but there is no content returned. Useful for actions that do not require a response body, such as a DELETE action.

- 301 — Moved Permanently: This resource was moved to another location and the location is returned. This header is especially useful when URLs change over time (maybe due to a change in version, a migration, or some other disruptive change), keeping the old ones and returning a redirection to the new location allows old clients to update their references in their own time.

- 400 — Bad Request: The request issued has problems (for example, might be lacking some required parameters). A good addition to a 400 response might be an error message that a developer can use to fix the request.

- 401 — Unauthorized: Especially useful for authentication when the requested resource is not accessible to the user owning the request

- 403 — Forbidden: The resource is not accessible, but unlike 401, authentication will not affect the response.

- 404 — Not Found: The URL provided does not identify any resource. A good addition to this response could be a set of valid URLs that the client can use to get back on track (root URL, previous URL used, etc.).

- 405 — Method Not Allowed: The HTTP verb(e.g POST, GET, PUT etc)used on a resource is not allowed — for instance, doing a PUT on a resource that is read-only.

- 500 — Internal Server Error: A generic error code when an unexpected condition is met and the server crashes. Normally, this response is accompanied by an error message explaining what went wrong.

## Autenticação e autorização

Em muitos sistemas, usamos sistemas de autenticação e autorização para incluir, atualizar e deletar os recursos. 

Por exemplo, para remover uma pessoa do servidor, podemos necessitar que apenas um determinado tipo de usuário possa realizar a operação (um moderador, por exemplo). Caso não seja feita essa restrição, qualquer usuário poderia excluir qualquer pessoa do sistema!

Podemos querer saber quem fez algo (autenticação) ou quem pode fazer algo (autorização). Existem diferentes formas básicas e didáticas de fazer isso, como por exemplo fazer a seguinte requisição para adicionar uma pessoa:

```
{
    "login": "IFSP",
    "senha": "testenovo",
    "email": "testenovo@outlook.com",
    "data_cadastro": "23/04/2019",
    "sexo": "M"
}
```

Onde "login" e "senha" são informações de quem está fazendo a requisição.

Caso o login/senha sejam válidos e tem a autorização para fazer a requisição, ela é completada com sucesso. Caso contrário, ela é cancelada...

Obviamente, tais recursos são extremamente limitados e para fins didáticos apenas. Caso tenha interesse em sistemas mais robustos e profissionais, consulte links como este: https://blog.restcase.com/4-most-used-rest-api-authentication-methods/

