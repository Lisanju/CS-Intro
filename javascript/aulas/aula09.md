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
- 
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
