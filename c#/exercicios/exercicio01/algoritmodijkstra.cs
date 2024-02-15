using System;

namespace AlgoritmoDijkstra
{

    class Grafo
    {

        //Declarei uma variável para armazenar o número total de vértices.
        static int numeroVertices = 9;

        //Declarei uma função para calcular o peso mínimo entre os vértices,
        //ela possui como parâmetro duas matrizes: (1) tipo inteiro, que
        //contém os pesos entre os vértices; (2) tipo bool, que contém
        //o conjunto de caminhos mais curtos de pesos.
        int pesoMinimo(int[] pesos, bool[] conjuntoCaminhosCurtos)
        {
            //A primeira atividade da função é declarar o valor mínimo de peso.
            //A ideia é que até então os pesos associados aos vértices são
            //nulo (para vértice de origem) e infinito (para os outros vértices).
            //Por isso, o peso mínimo é int.MaxValue (representando infinito).
            int minimo = int.MaxValue, indice_minimo = -1;

            //A variável vertice é criada recebendo 0 como atribuição se o valor de vertice
            //for menor que o valor de numeroVertices (isto permite aque a gente limite o 
            //funcionamento do código para apenas o número de vértices que queremos representar
            //em nosso grafo). Após o código ser executado, é atribuído mais 1 ao valor de vertice.
            for (int vertice = 0; vertice < numeroVertices; vertice++)
                if (conjuntoCaminhosCurtos[vertice] == false && pesos[vertice] <= minimo){
                    minimo = pesos[vertice];
                    indice_minimo = vertice;
                }
            //Primeiro queremos pegar o vértice com menor peso. Para isso, criamos a condição
            //de que, caso o vértice não esteja listado no conjunto de caminhos mais curtos ainda
            //(conjuntoCaminhosCurtos[vertice]==false) e o peso do vértice seja menor ou igual infinito
            //(pesos[vertice]<=minimo), o peso mínimo passa a ser o valor do vértice (minimo = pesos[vertice]).
            //Além disso, o vértice é marcado como mínimo no índice (indice_minimo = vertice).
        
            return indice_minimo;
        }

        //Para facilitar na visualização, temos uma função que escreve na tela a matriz de pesos construída.
        void printSolucao(int[] pesos)
        {
            Console.Write("Vértice \t\t Peso "
                            + "a partir da Origem\n");
            for (int i = 0; i < numeroVertices; i++)
                Console.Write(i + " \t\t " + pesos[i] + "\n");
        }

        void dijkstra(int[,] grafo, int origem)
        {
            int[] pesos = new int[numeroVertices];
            bool[] conjuntoCaminhosCurtos = new bool[numeroVertices];
            //A primeira matriz é o que dá o valor de infinito para todos os pesos, usamos pesos[i] para
            //realizar a atribuição de infinito para cada peso da matriz.
            //A segunda matriz é o que delimita que nenhum dos pesos faz parte do conjunto de caminhos curtos,
            //usamos conjuntosCaminhosCurtos[i] para excluir as atribuições i do conjunto.

            for (int i = 0; i < numeroVertices; i++){
                pesos[i] = int.MaxValue;
                conjuntoCaminhosCurtos[i] = false;
            }

            //O peso da origem para a origem é 0.
            pesos[origem] = 0;

            //Para encontrar o caminho mais curto para todos os vértices
            for (int contagem = 0; contagem < numeroVertices - 1; contagem++){
                int u = pesoMinimo(pesos, conjuntoCaminhosCurtos);
            //Pegue o vértice de peso mínimo do conjunto de vértices ainda não processados.
            //Na primeira iteração, u é sempre igual a origem.

            //Incluia o vértice como processado, isto é, como parte do conjunto.
                conjuntoCaminhosCurtos[u] = true;

            //Vamos atualizar o valor de peso dos vértices adjacentes ao vértice escolhido.
                for (int vertice = 0; vertice < numeroVertices; vertice++)
        
                if (!conjuntoCaminhosCurtos[vertice] && grafo[u, vertice] != 0
                    && pesos[u] != int.MaxValue && pesos[u] + grafo[u, vertice] < pesos[vertice])
                    pesos[vertice] = pesos[u] + grafo[u, vertice];
            //Só alteramos o valor de peso pesos[vertice] se:
            //1 - O vertice adjacente não estiver no conjunto de caminhos mais curtos / não foi processado;
            //2 - Existe um caminho entre o vértice escolhido e o vértice adjacente;
            //3 - O vértice adjacente não ter peso infinito;
            //4 - A soma do peso do vértice adjacente com o caminho da origem até o vértice escolhido seja
            //menor que o peso atual de pesos[vertice]
            }

            printSolucao(pesos);
        }

        public static void Main()
        {

            int[,] grafo = new int[,] {
                { 0, 4, 0, 0, 0, 0, 0, 8, 0 },   //Vértice 0: peso dos vértices adjacentes, partindo do vértice 0.
                { 4, 0, 8, 0, 0, 0, 0, 11, 0 },  //Vértice 1: peso dos vértices adjacentes, partindo do vértice 1.
                { 0, 8, 0, 7, 0, 4, 0, 0, 2 },   //...
                { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                { 0, 0, 2, 0, 0, 0, 6, 7, 0 } 
                };

                Grafo exemplo = new Grafo();

                exemplo.dijkstra(grafo, 0);
        }
    }

}
