# Histórico do JavaScript

Nesta aula, os objetivos são relembrar conceitos básicos de programação web, diferenciando páginas web estáticas e dinâmicas, além de introduzir conceitos básicos e o histórico do JavaScript.

## Como funciona a web?

Existe um cliente e um servidor:

- Cliente - Quem usa a web. Envia requisições ao servidor, recebendo alguma resposta dele (textos, imagens, vídeos etc.). Por exemplo, computadores, smartphones, câmeras de segurança e geladeiras.

- Servidor - É um equipamento (geralmente um computador ou cluster), que recebe as informações enviadas do cliente. Contém software específico que realiza as operações programadas. Geralmente inclui um sistema de banco de dados.

## Em mais detalhes

O usuário digita um endereço web (www.endereco.com.br). As informações enviadas são agrupadas em uma requisição.

O sistema operacional (ou o roteador) transforma o endereço em um número de 32bits (ipv4) ou 64bits (ipv6).

Com o endereço da máquina de destino (que é o servidor), o roteador encaminha a requisição pela internet.

Usando tabelas de endereçamento, a requisição é encaminhada progressivamente até o destino (de roteador para roteador).

Uma vez no destino, o firewall verifica se a requisição é válida.

Se for válida, a requisição é enviada ao software associado.

O servidor executa o script conforme programado, eventualmente acessando o banco de dados, gerando o resultado esperado (um arquivo HTML, em geral).

O resultado é enviado ao cliente (processo similar ao envio da requisição do cliente ao servidor).

O cliente, então, recebe a resposta e executa a resposta conforme programado.

## Backend e Frontend

O desenvolvimento web pode ser organizado em backend ou frontend. O frontend trata de tudo aquilo que o usuário vê ou interage. Composto basicamente por arquivos HTML, CSS e JS. Já o backend trata de trechos de código que executam de acordo com os parâmetros/requisições dos usuários, gerando o código que será executado ou exibido no navegador (frontend). Geralmente contém requisições a um banco de dados. Pode conter códigos PHP, Java, C#, JS e muitos outros.

## Páginas estáticas

Páginas web que usam puramente HTML5 e CSS3 são páginas estáticas.

A interação do usuário pouco afeta a apresentação do site. A adição ou remoção de novos elementos na página depende diretamente do servidor.

HTML e CSS não são linguagens de programação, pois não permitem a adição de lógica de negócios (apesar do HTML5 e CSS3 apresentarem diversos recursos dinâmicos que melhoram a interação entre usuário e página web, esses recursos ainda são limitados).

## Páginas dinâmicas

Permite uma interação com o usuário mais elaborada, sem necessitar comunicação com o servidor. Tem como consequência a redução do tráfego entre cliente e servidor, aumentando o desempenho do servidor e reduzindo o consume de banda do cliente.

Adiciona lógica de negócios ao site, facilitando o uso de checagens e verificações de maneira imediata, entre outras funcionalidades.

Permite a manipulação direta dos elementos CSS e HTML da página web (DOM).

## JavaScript

Em 1987, Dan Winkles criou a linguagem HyperTalk para a Apple. Criada para iniciantes em programação, sendo simples e amigável.

```
on mouseUp
  put "100,100" into pos
  repeat with x = 1 to the nnumber of card buttons
    set the location of card button x to pos
    add 15 to item 1 of pos
  end repeat
end mouseUp
```

Em 1994, a Netscape contratou Brendan Eich para criar uma linguagem de programação para seu navegador. Inicialmente, Brendan propôs usar a linguagem Scheme, sendo mais complexa e menos amigável que o HyperTalk.

```
(define (list-of-squares n)
  (let loop ((i n) (res '()))
    (if (< i 0)
      res
        (loop (- i 1) (cons (* i i) res)))))
(list-of-squares 9) ===> (0 1 4 9 16 25 36 49 64 81)
```

No fim, Brendan criou uma linguagem chamada inicialmente de Mocha, usando conceitos das linguagens Java, Scheme, Self e Perl. Foi lançada oficialmente em 1995 com o nome de LiveScript.

Devido a guerra dos navegadores com a Microsoft, a Netscape forma uma parceira com a Sun, mudando o nome da linguagem para JavaScript.

Em 1997, a Netscape padronizou a linguagem, chamando ela de ECMAScript.

### Sobre a linguagem

- Linguagem interpretada - O navegador executa o programa usando um motor próprio.
- Possui orientação a objetos.
- Tipagem fraca e dinâmica - Permite que variáveis sejam declaradas sem um tipo definido, que pode mudar durante a execução do programa.
- Funções de primeira classe - Funções podem ser definidas dentro de outras funções, podem ser parâmetros de outras funções etc.
- Single-thread - Computa a execução do código do começo ao fim sem interrupção.
- Versão 9 - ECMAScript 2018.

### O que o JavaScript não pode fazer?

- Acessar diretamente um banco de dados.
- Escrita de arquivos comuns (com exeção de cookies).
- Acessar dados de domínios externos.


