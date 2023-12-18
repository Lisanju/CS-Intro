# Noções de Debug com JavaScript

Entender o conceito de Debug é importante pois permite a fácil detecção de erros e equívocos no código-fonte digitado.

## História e considerações

Historicamente, o primeiro bug da história foi reportado por Grace Hopper no dia 9 de setembro de 1947.

Na ocasião, estava sendo executado um código-fonte que estava causando erros em programas subsequentes.

Sabendo que o referido código deveria funcionar, ao abrir o grande computador, foi encontrada uma mosca, já morta, em um circuito lógico essencial. Graças a sua presença, surgiam pequenas alterações cumulativos no resultado das operações sendo realizadas. 

A partir de então, a ocorrência de erros foi chamada de "bug" (tradução para 'inseto') e o ato de resolver ou procurar tais erros como "debugging" ou simplesmente "debug".

Obviamente, já passou o tempo onde um programa deixa de funcionar devido a presença de um organismo estranho no circuito do computador. Embora ainda possa ocorrer casos esporádicos, o principal causador de bugs no sistema é o próprio programador.

Há inúmeros fatores que contribuem para o surgimento de bugs, tais como:

- Desconhecimento das particularidades dos recursos da linguagem ou software usados;
- Especificação do software deficiente;
- Falha no entendimento ou especifição do software por parte do programador;
- Reuso inadequado de trechos de código sem critério;
- Falhas de comunicação entre equipe de desenvolvimento e teste;
- etc.

Nesta aula, será ensinado conceitos e recursos fundamentais para a linguagem JavaScript usando o navegador Google Chrome.

## Como achar as ferramentas?

O Google Chrome possui diversos recursos que auxiliam o desenvolvimento web, chamado popularmente como DevKit ("kit de desenvolvimento"). Para acessar as Ferramentas de Desenvolvedor pode-se usar os seguintes meios (considerando uma máquina desktop rodando o Windows):

- Ctrl + Shift + J;
- F12;
- Opções... Mais ferramentas... Ferramentas do desenvolvedor.

Ao abrir as Ferramentas do Desenvolvedor, surgirão os recursos divididos em várias abas, como Elements, Console, Source e outros:

Após abrir as Ferramentas do Desenvolvedor, utilizaremos as ferramentas de debugging presente na aba Source.

## Breakpoints
