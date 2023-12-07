# Introdução

Correspondente ao Capítulo 0 de Brookshear (2013), a Introdução apresenta os tópicos a seguir:
- O papel dos algoritmos;
- A história da computação;
- A ciência dos algoritmos;
- Abstração;
- Um esboço de nosso estudo;
- Repercussões sociais.

A ideia é que, nesse capítulo, seja delimitado o escopo da ciência da computação, desenvolvendo uma perspectiva histórica e estabelecendo uma base para estudo.

## O papel dos algoritmos

Informalmente, um algoritmo é um conjunto de passos que define como uma tarefa é realizada. A representação de um algoritmo, num formato que seja compatível com a tecnologia da máquina, é chamada de programa. O processo de desenvolver um programa, codificando-o em um formato compatível para uma máquina, é chamado de programação. O conjunto de programas, bem como os algoritmos que eles representam, são chamados de software, enquanto o maquinário propriamente dito é chamado de hardware. O conceito de algoritmo é o mais fundamental da ciência da computação, pois todo computador precisa de instruções para realizar uma tarefa.

## A história da computação

Um dos primeiros dispositivos de computação é o ábaco. Ele funciona através de elementos de contagem (contas), que são mantidas em hastes. Na medida em que as contas são movidas pelas hastes, um dado valor é armazenado. Então, o ábaco, por si só, é um sistema de armazenamento de dados a partir da posição das contas pelas hastes. Ele precisa ser manualmente manipulado por um humano para compor uma máquina computacional completa.

Blaise Pascal (1623-1662) na França, Gottfried Wilhelm Leibniz (1646-1716) na Alemanha e Charles Babbage (1792-1871) na Inglaterra desenvolveram máquinas de computação com a tecnologia de engrenagens. Os dados nessas máquinas eram representados pelo posicionamento das engrenagens a partir das posições iniciais delas. Os dados de saída das máquinas de Pascal e Leibniz eram obtidos pela observação da posição final das engrenagens. Já, para a máquina de Babbage, era especulado que fosse possível imprimir os resultados da computação em folhas de papel, evitando erros de transcrição.

Sobre as habilidades de seguir um algoritmo, é possível ver uma progressão na flexibilidade dessas máquinas. A máquina de Pascal era projetada apenas para realizar adições, com a sequência de passos estando embutida na própria estrutura da máquina. A máquina de Leibniz também tinha os algoritmos embutidos na sua arquitetura, mas apresentava uma variedade de operações aritméticas que podiam ser selecionados por quem operasse a máquina. Babbage projetou a Máquina Diferencial, que poderia ser modificada para realizar diferentes cálculos, e a Máquina Analítica, que poderia ler instruções na forma de perfurações em cartões de papel. É possível dizer, então, que a Máquina Analítica de Babbage era programável. Quem publicou diversos artigos que mostravam que a Máquina Analítica de Babbage seria programável foi Augusta Ada Byron (Ada Lovelace), considerada a primeira programadora do mundo.

A ideia de comunicar para a máquina um algoritmo através de perfurações em papel não foi de Babbage, mas sim de Joseph Jacquard (1752-1834). Ele desenvolveu uma máquina de tear que recebia diferentes padrões de perfurações em cartões finos feitos de madeira, fazendo com que a máquina produzisse diferentes desenhos de tecelagem a partir dos padrões dos cartões. Herman Hollerith (1860-1929) aplicou o conceito de Jacquard de representar informações em cartões de papel para acelerar o processo de apuração do censo demográfico americano, sendo esse um dos trabalhos que levou à criação da IBM.

Com o avanço da tecnologia eletrônica, as máquinas de computação tornaram-se mais refinadas. A máquina de George Stibitz e a máquina Mark I, produzida por Howard Aiken e engenheiros da IBM, são exemplos de máquinas eletromecânicas, que faziam uso de relés mecânicos controlados eletronicamente. Pouco tempo depois, foram substituídas por máquinas totalmente eletrônicas, como a máquina Atanasoff-Berry, construída por John Atanasoff e Clifford Berry. Outra máquina eletrônica é a Colossus, construída por Tommy Flowers durante a Segunda Guerra Mundial para a decodificação de mensagens alemãs.

A popularização dos computadores se deu com a invenção dos desktops. A origem dessas máquinas pode ser remetida aos hobistas que construíam computadores em casa a partir da combinação de chips. Foi dentro dessa atividade nichada que Steve Jobs e Stephen Wozniak construíram um computador caseiro comercialmente viável, estabelecendo a Apple Computer Incorporation. Outras empresas que comercializavam produtos similares foram a Commodore, a Heathkit e a Radio Shack. Apesar desses produtos serem populares entre os hobistas de computadores, eles não foram amplamente aceitos pela comunidade empresarial, que continuava a recorrer à IBM. Em 1981 a IBM apresenteu seu primeiro desktop, chamado de computador pessoal (PC), cujo software adjacente tinha sido desenvolvido pela recém-formada Microsoft. Atualmente o termo PC é usado para se referir a todas as máquinas cujo projeto evoluiu do primeiro desktop da IBM.

Com o final do século XX, a habilidade de conectar indivíduos em um sistema de amplitude mundial chamado de Internet estava revolucionando a comunicação. Assim, Tim Berners-Lee propôs um sistema pelo qual documentos armazenados em computadores ao longo da Internet podiam ser unidos, produzindo um emaranhado de informações conectadas chamado de World Wide Web (abreviado para Web). Para tornar a informação na Web acessível, sistema de software chamados de motores de busca foram desenvolvidos, permitindo que as informações na Web sejam categorizadas e pesquisados por tópicos em particulares. Empresas como Google, Yahoo! e Microsoft são exemplos nessa área.

Atualmente, há um movimento de miniaturização dos computadores, estando presentes em diferentes dispositivos, como automóveis, que portam Sistemas de Posicionamento Global (GPS), monitorando o funcionamento do motor e fornecendo serviços de comando de voz para controlar o áudio e os sistema de comunicação telefônica do carro. Os smartphones também são exemplos de computadores em miniatura que se popularizaram atualmente. Esses computadores são equipados com um amplo conjunto de sensores e interfaces, incluindo câmeras, microfones, bússolas, telas sensíveis ao toque, acelerômetros e diversas tecnologias sem fio para se comunicarem com outros smartphones e computadores. 

## A ciência dos algoritmos

Como consequência do teorema da incompletude de Gödel, os matemáticos já investigavam questões relacionadas à processos algorítmicos, que foram evidenciados com os avanços tecnológicos da computação. A ciência da computação estabeleceu-se como a ciência dos algoritmos, incluindo uma variedade de tópicos. De todo modo, as questões gerais que perpassam a ciência da computação são:
- Que problemas podem ser solucionados por processos algorítmicos?
- Como tornar mais fácil a descoberta de algoritmos?
- Como as técnicas de representação e de comunicação de algoritmos podem ser melhoradas?
- Como as características de diferentes algoritmos podem ser analisadas e comparadas?
- Como algoritmos podem ser usados para manipular informações?
- Como algoritmos podem ser aplicados para produzir comportamento inteligente?
- Como a aplicação de algoritmos afeta a sociedade?

## Abstração

Abstração é uma técnica de simplificação importante que se refere à distinção entre as propriedades externas de uma entidade e os detalhes da sua composição interna. É a abstração que permite que usemos um computador como uma unidade única compreensível, ignorando seus detalhes internos complexos. Para cada nível de abstração, vemos o sistema em termos de componentes chamados de ferramentas abstratas.

## Um esboço de nosso estudo

O capítulo apresenta uma abordagem ascendente para o estudo da ciência da computação, iniciando com tópicos, como hardware de computadores, e indo em direção à tópicos mais abstratos, como complexidade de algoritmos e computabilidade. A ideia é que o estudo siga um padrão de construção de ferramentas de abstração cada vez maiores.

## Repercussões sociais

Na legislação, a ciência da computação gera questões relacionadas ao grau pelo qual a propriedade intelectual pode ser garantida e aos direitos e às responsabilidades que acompanham essa propriedade. Na ética, ela gera numerosas opções que desafiam os princípios tradicionais nos quais o comportamento social é baseado. No governo, gera debates relacionados a quanto a tecnologia computacional e suas aplicações devem ser reguladas. Na filosofia, gera controvérisas entre a presença de um comportamento inteligente e a presença de inteligência propriamente dita. Na sociedade, ela gera disputas que dizem respeito sobre as novas aplicações trazerem novas liberdades ou novos controles. Para tratar dessas questões, no final de cada capítulo há questões sobre repercussões sociais geradas pelos avanços tecnológicos da ciência da computação.
