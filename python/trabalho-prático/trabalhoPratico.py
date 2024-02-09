import random

rodarJogo = True
while rodarJogo == True:

    # Menu de opções

    print(
        "\n ========== Menu de Opções ========== \n \n Selecione uma das opções a seguir: \n \n 1 - Gerenciar arquivo de palavras; \n 2 - Jogar; \n 3 - Sair. \n"
    )
    opcaoMenu = int(input())

    # Opção 1 - Gerenciador de arquivo de palavras

    arquivo = "palavras.txt"

    if opcaoMenu == 1:

        menuGer = True

        while menuGer == True:

            print(
                "\n ========== Gerenciar arquivo de palavras ========== \n \n Selecione uma das opções a seguir: \n \n 1 - Adicionar palavra; \n 2 - Excluir palavra; \n 3 - Voltar."
            )
            opcaoGer = int(input())

            lista = open(arquivo, "r")
            textoLista = lista.read()
            lista.close()

            if opcaoGer == 1:

                novaPalavra = str(input("\n Insira uma nova palavra: ")).lower()

                if novaPalavra in textoLista:

                    print("\n A palavra inserida já está no arquivo. \n")
                    pass

                else:

                    lista = open(arquivo, "a+")
                    lista.write(novaPalavra)
                    lista.write("\n")
                    lista.close()

                    print("\n A palavra inserida foi adicionada ao arquivo. \n")

            elif opcaoGer == 2:

                print(textoLista)
                exclPalavra = str(
                    input("\n Insira uma palavra da lista acima para excluir: ")
                )

                if exclPalavra + "\n" in textoLista:

                    textoLista = textoLista.replace(exclPalavra + "\n", "")

                    with open(arquivo, "w") as lista:
                        lista.write(textoLista)

                    print("\n A palavra inserida foi excluída do arquivo. \n")

                else:

                    print(
                        "\n A palavra inserida não está na lista apresentada acima. \n"
                    )

            elif opcaoGer == 3:

                menuGer = False
                continue

            else:

                print("\n A opção selecionada é inválida. \n")

    # Opção 2 - Jogar

    elif opcaoMenu == 2:

        palpiteErrado = []
        palpiteTotal = []
        errosPermitidos = 5

        lista = open(arquivo, "r")
        textoLista = lista.read()
        lista.close()

        listaForca = textoLista.split("\n")
        listaForca = list(filter(None, listaForca))

        if listaForca == []:

            print("\n Não há palavras no arquivo, insira novas palavras para jogar. \n")

        else:

            palavraEscolhida = random.choice(listaForca)
            numeroLetras = len(palavraEscolhida)
            chancesRestantes = errosPermitidos

            while chancesRestantes > 0:

                palavraAtualizada = "".join(
                    letra if letra in palpiteTotal else "_"
                    for letra in palavraEscolhida
                )

                print("\n ===============================")

                print("\n Palavra escolhida: ", palavraAtualizada)

                print("\n Quantidade de letras: ", len(palavraEscolhida))

                if "_" not in palavraAtualizada:
                    print("\n Você ganhou o jogo da forca!")
                    break

                print("\n Chances restantes: ", chancesRestantes)

                print("\n Palpites errados: ", palpiteErrado)

                print("\n ===============================")

                palpite = input("\n Dê seu palpite: ").lower()

                if palpite in palpiteTotal or palpite in palpiteErrado:
                    print("\n Você já fez esse palpite, faça outro.")

                elif palpite in palavraEscolhida:
                    print("\n Palpite correto.")
                    palpiteTotal.append(palpite)

                else:
                    print("\n Palpite errado.")
                    palpiteErrado.append(palpite)
                    chancesRestantes = chancesRestantes - 1

            if "_" in palavraAtualizada:
                print(
                    "\n Você perdeu o jogo da forca. A palavra era: ", palavraEscolhida
                )

    # Opção 3 - Sair

    elif opcaoMenu == 3:

        print("\n Encerrando o jogo da forca. \n")
        rodarJogo = False
        break

    else:

        print("\n A opção selecionada é inválida. \n")
