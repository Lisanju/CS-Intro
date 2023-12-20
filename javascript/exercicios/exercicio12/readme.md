## Proposta de exercício

No endereço https://banco-dados-teste.glitch.me/ existe um webservice simples capaz de efetuar as operações básicas de criar, recuperar, atualizar e deletar (do inglês CRUD) produtos fictícios. Cada produto possui diversos campos diferentes, exemplificados a seguir:

```
"_id":  "5ffcab54b7cea400afa92749",
"title": "Produto teste 2 ",
"description": "Produto inicial",
"price": 1,
"createdAt": "2021-01-11T19:47:32.706Z",
"updatedAt": "2021-01-12T01:57:48.489Z",
"__v": 0
},
```

O seu objetivo, nessa atividade, é o de desenvolver uma página web utilizando a comunicação AJAX capaz de realizar as operações de cadastrar um produto, editar um produto, listar os produtos e deletar um produto. Um exemplo da operação de um site que realiza as atividades é exemplificado a seguir:

https://youtu.be/QCE22zta74o?si=fc9YY0y3x-zmnuSI

As rotas ou pontos de acesso para que os recursos possam ser utilizados são:

- /api/produtos -- GET e POST
- /api/produtos/:id -- GET, PUT e DELETE
- 
Quanto a rota /api/produtos, uma requisição GET indica a operação de listar os produtos e POST indica a operação de cadastrar um novo produto.

Já para a rota /api/produtos/:id (onde id é o valor do _id de cada produto), uma requisição GET retorna as informações do referido produto, o PUT significa a edição de um produto específico e DELETE a remoção de um produto específico.

É importante mencionar que o design do sistema desenvolvido (no exemplo, usando BootStrap) não será considerado nesta atividade. Portanto, utilize a interface que preferir (desde que o site resultante seja utilizável). Outros detalhes importantes:

- Para realizar o cadastro, basta o envio dos parâmetros title, price e description. Os demais parâmetros do produto são gerados ou mantidos automaticamente pelo servidor.
- O servidor https://banco-dados-teste.glitch.me/ tem como característica "desligar-se" a cada 5 minutos se uma nova requisição não for realizada. Assim, antes de testar o código, verifique se o servidor apresenta a mensagem de "Está funcionando".
- A atividade deve ser entregue como um arquivo HTML único, contendo o site completo. Nesta tarefa, deve ser utilizado JavaScript nativo e/ou jQuery.

Quanto ao funcionamento do sistema em si, é importante mencionar alguns detalhes:

- Após o cadastro bem sucedido de um produto, o formulário de cadastro deve ser "resetado".
- Ao editar um produto, e esta operação resultar em sucesso, o formulário para edição do produto deve desaparecer.
- Não deve haver nenhum comando para efetuar o redirecionamento ou o reload na página
