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

A forma mais eficaz de encontrar um bug é executar, linha-a-linha todo o programa uma vez. Se todas as linhas são percorridas, avaliadas e "corrigidas", é provável que o bug será encontrado eventualmente.

Porém, um código-fonte pode conter, geralmente, centenas ou milhares de comandos, divididos em dezenas ou centenas de funções, objetos ou módulos espalhados pelo programa. Um erro em uma única instrução pode causar uma pane grave em outro trecho de código, tornando difícil descobrir em que instrução há o erro.

Para evitar de ter que verificar todas as linhas (que ainda é o jeito recomendável para programas pequenos), existem os pontos de quebra (do inglês: breakpoints). Em geral, quando um programa de debug está executando, todas as instruções são executadas sem interrupção até o final do código-fonte. Como queremos verificar se uma instrução está correta, podemos interromper a execução em determinada parte/instrução do código. Esses são os breakpoints.

Na sua forma habitual, um breakpoint pode ser inserido no DevKit ao clicar diretamente na linha do código desejado.

Um mesmo trecho de código pode conter diversos breakpoints espalhados pelo código fonte, conforme a necessidade do programador.

## Debug passo a passo

Com os breakpoints, podemos "pausar" a execução em determinada instrução. Caso a instrução esteja correta, em tese, o bug não se encontra na referida instrução e podemos continuar a execução. Mas surgem então duas questões:

- Como "continuar" a execução? 
- Se a instrução é complexa (uma chamada de função, por exemplo), como saber se o problema não é exatamente a função?

Para responder tais questões, vamos executar um trecho simples de código capaz de exercitar nossos conhecimentos de debug.

Para isso, considere esse trecho simples de código-fonte em JavaScript.

```
function delta(a, b, c) {
    return b*2 - 4 * a * c;
}

function baskhara(a, b, c) {
    var valor_delta = delta(a,b,c);
    var x1 = (-b + Math.sqrt(valor_delta)) / (2 * a);
    var x2 = (-b - Math.sqrt(valor_delta)) / (2 * a);

    console.log("X1: " + x1);
    console.log("X2: " + x1);
}

var a = prompt("Digite a");
var b = prompt("Digite b");
var c = prompt("Digite c");

baskhara(a,b,c);
```

O trecho de código acima tem por objetivo receber três valores digitados pelo usuário e imprimir no console as duas raízes da função de segundo grau (ax² + bx + c).

Primeiro, temos que testar se o algoritmo executa corretamente (ou apresenta o resultado esperado). 

O resultado que devemos esperar (Results) são as raízes -1 e 6.

Mas, na hora de executar o código, encontramos algum bug.

### Resume

Como não sabemos onde está(ão) o(s) bug(s), precisamos verificar o nosso código fonte. Normalmente, em códigos simples como esse, começamos verificando se a chamada da função baskhara está sendo feita com os parâmetros corretos. Para isso, criamos um breakpoint exatamente na linha 25 do código fonte e recarregamos a página (para reexecutar o código do zero).

Depois de digitado os parâmetros 1, -5 e -6 nas caixas de prompt, o resultado é o seguinte: o console está vazio e a mensagem na barra superior direita dizendo "Paused on breakpoint". São sinais de que o código ainda está em execução, mas pausado no breakpoint. 

Nesse momento, podemos colocar o mouse sobre as variáveis do código fonte e podemos verificar o valor delas...

Podemos notar que os valores estão corretos, mas estão marcados como strings. Como isso pode influenciar algo, é recomendável transformar os valores de string para número. Para isso, temos as funções...

`parseFloat` e `parseInt`

Como os números digitados PODEM ser com vírgula (float), usaremos parseFloat.

Colocando o mouse sobre as variáveis na chamada da função, podemos verificar que está tudo ok. São reconhecidos como números como esperado...

Mas funciona? Para verificarmos, podemos clicar para continuar a execução do código-fonte com o controle de Resume script execution. 

É possível notar mudanças significativas na interface. Primeiro, os valores resultantes das operações são mostradas diretamente no código fonte (painel superior central), além dos valores das variáveis no escopo local (canto superior direito).

Graças a tal recursos, é possível detectar mais um bug. Veja que o resultado original imprimiu dois valores iguais (4.370828....). Porém, podemos ver que os valores x1 e x2 tem valores diferentes! Isso se deve ao engano na linha de código 18, onde desejamos imprimir o valor da variável x2, mas imprimimos o valor de x1! Corrigindo...
