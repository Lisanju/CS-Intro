# Armazenamento de Dados
Correspondente ao Capítulo 1 de Brookshear (2013), o capítulo Armazenamento de Dados apresenta os tópicos a seguir:
- Bits e seu armazenamento;
- Memória principal;
- Armazenamento em massa;
- Representação da informação como padrões de bits.

Neste capítulo, vemos sobre a representação de dados e o armazenamento de dados em um computador, incluindo dados como texto, valores numéricos, imagens, áudio e vídeo.

## Bits e seu armazenamento

Nos computadores atuais, as informações são armazenadas através de padrões de 0 e 1. Esses dígitos são chamados de bits (binary digits). A depender da situação, padrões de bits podem ser usados para representar valores numéricos, caracteres de um alfabeto, imagens e sons.

Os bits são manipulados através de operações booleanas, que atribuem o valor verdadeiro para 1 e falso para 0. Grosso modo, as operações booleanas recebem como entrada e retornam como saída apenas os valores de verdadeiro ou falso.

Três das operações booleanas básicas são AND, OR e XOR:
- P AND Q = 1 sse (P=1) ∧ (Q=1)
- P OR Q = 1 sse (P=1) ∨ (Q=1)
- P XOR Q = 1 sse (P=1) ∧ (Q=0) ∨ (P=0) ∧ (Q=1)

Um dispositivo que produz a saída de uma operação booleana é chamado de porta lógica. As portas lógicas podem ser construídas por uma variedade de tecnologias, como engrenagens, relés e dispositivos ópticos. Nos computadores atuais, as portas lógicas são produzidas a partir de circuitos eletrônicos, nos quais os bits 0 e 1 são representados como níveis de voltagem.

Um exemplo de conjunto de circuitos eletrônicos que representam as operações booleanas são os flip-flops. Um flip-flop produz um valor de saída 0 ou 1, que permanece constante, até que um pulso (mudança temporário para 1 que retorna a 0) de outro circuito faz com que ele mude para outro valor. Isto é, a saída alternará entre os dois valores a partir de estímulos externos. Muitos flip-flops, construídos como circuitos elétricos muito pequenos, podem ser usados dentro de um computador como uma forma de gravar informação codificada como padrões de 0 e 1.

A tecnologia conhecida como VLSI (Very large-scale integration) permite que milhões de componentes elétricos sejam construídos em um wafer (chamado de chip). Esses chips são usados como ferramentas abstratas na construção de sistemas de computação.

