# Objetos, funções, argumentos e scripts

## Objetos

Um objeto nada mais é que um nome que você usa para chamar por um dado armazenado na memória do computador.

Para criar um objeto em R, escolha um nome e use o `<-` para indicar o valor a ser armazenado nele.

```
die <- 1:6
# um objeto chamado 'die' que armazena valores de 1 a 6.
```

Quando um objeto é criado, ele irá aparecer no painel de ambientação do RStudio, localizado no canto direito superior. Esse painel mostra todos os objetos criados desde que o RStudio foi aberto.

Você pode nomear um objeto em R de praticamente qualquer coisa, mas há algumas restrições. Primeiro, um objeto não pode começar com um número. Segundo, um objeto não pode conter em seu nome os símbolos especiais `!`, `$`, `@`, `-`, `/` ou `*`.

Note que o R é uma linguagem de caso sensitivo, o que significa que letras maiúsculas e minúsculas são entendidas como caracteres diferentes.

Com a função `ls`, você pode conferir os nomes de objetos que já estão sendo utilizados:

```
ls()
## "a"         "die"       "my_number" "name"     "Name"
```

Outra alternativa para ver os nomes de objetos já utilizados é olhar no painel de ambientação do RStudio.

