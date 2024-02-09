## Implemente o jogo da forca. Ao iniciar o jogo, o seguinte menu de opções deverá aparecer para o usuário:

## 1 - Gerenciar arquivo de palavras
## 2 - Jogar
## 3 - Sair

## Ao selecionar a opção “Gerenciar arquivo de palavras”, um novo menu de opções é apresentado.

## 1 - Adicionar palavra: adiciona uma nova palavra digitada pelo usuário ao final do arquivo “palavras.txt”. O arquivo não deve conter palavras duplicadas.
## As palavras são armazenadas uma por linha.
## 2 - Excluir palavra: exclui a palavra digitada pelo usuário do arquivo “palavras.txt”.
## 3 - Voltar: volta ao menu anterior

## Ao selecionar a opção “Jogar”, o jogo tem início:

## 1 - Uma palavra é sorteada aleatoriamente do arquivo.
## 2 - O programa apresenta ao jogador quantas letras a palavra possui
## 3 - O jogador escolhe uma letra que ele acha que a palavra possua.
## 4 - O programa informa se a letra existe ou não. As seguintes informações são apresentadas: as letras já tentadas, a quantidade de erros cometidos e a letras
## já reveladas da palavra oculta.
## 5 - O jogador é declarador vencedor se conseguir revelar a palavra com menos de 5 erros

## Ao selecionar a opção “Sair”, o jogo termina.

## ================== Implementação do Jogo da Forca a seguir: ==================

while (True):
    
    # Menu de opções
    print("========== Menu de Opções ========== \n \n Selecione uma das opções a seguir: \n \n 1 - Gerenciar arquivo de palavras; \n 2 - Jogar; \n 3 - Sair. \n")
    opcaoMenu = int(input())

    # Opção 1 - Gerenciador de arquivo de palavras
    arquivo = "palavras.txt"

    if (opcaoMenu == 1):
        menuGer = True
        
        while (menuGer == True):
            
            print("========== Gerenciar arquivo de palavras ========== \n \n Selecione uma das opções a seguir: \n \n 1 - Adicionar palavra; \n 2 - Excluir palavra; \n 3 - Voltar.")
            opcaoGer = int(input())

            lista = open(arquivo, "r")
            textoLista = lista.read()
            lista.close()
        
            if (opcaoGer == 1):
                novaPalavra = str(input("Insira uma nova palavra: "))

                if (novaPalavra in textoLista):
                    print("\n A palavra inserida já está no arquivo. \n")
                    pass
            
                else:
                    lista = open(arquivo, "a+")
                    lista.write(novaPalavra)
                    lista.write("\n")
                    lista.close()

                    print("\n A palavra inserida foi adicionada ao arquivo. \n")

            elif (opcaoGer == 2):
                print(textoLista)
                exclPalavra = str(input("Insira uma palavra da lista acima para excluir: "))

                if (exclPalavra + "\n" in textoLista):
                    textoLista = textoLista.replace(exclPalavra + "\n", "")

                    with open(arquivo, "w") as lista:
                        lista.write(textoLista)

                    print("\n A palavra inserida foi excluída do arquivo. \n")

                else:
                    print("\n A palavra inserida não está na lista apresentada acima. \n")

            elif (opcaoGer == 3):
                menuGer = False
                continue

            else:
                print("\n A opção selecionada é inválida. \n")
        
    # Opção 2 - Jogar


    # Opção 3 - Sair
