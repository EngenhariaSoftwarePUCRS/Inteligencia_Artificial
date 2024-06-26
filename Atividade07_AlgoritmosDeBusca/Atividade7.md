# Atividade 7 - Algoritmo de Busca

## Integrantes

### Professora

Silvia Maria W. Moraes

### Alunos

Felipe Freitas e Luiza Heller

## Perguntas

1. Em que tipo de aplicações o algoritmo de busca A* é usado? Qual o seu propósito? Dê exemplos.
2. Em grafo, o A* é considerado um extensão do Dijkistra, execute o programa java A* em anexo (leia o readme) e descubra qual o papel da função heurística. O que a função faz para melhorar o desempenho do Dijkstra?
3. Explique a lógica usada pelo algoritmo A*.
4. Qual a diferença entre A*  e  IDA* (Iterative Deepening A*)?

## Respostas

1. O algoritmo de busca A* é utilizado em aplicações que envolvem a busca de caminhos em grafos, como por exemplo, em jogos de tabuleiro, robótica, planejamento de rotas, entre outros. O seu propósito é encontrar o caminho mais curto entre dois pontos, levando em consideração o custo de cada aresta e uma heurística (função) que estima o custo restante para chegar ao destino. Um exemplo de aplicação é o uso do A* em jogos digitais, como o jogo de damas, onde o algoritmo é utilizado para encontrar a melhor jogada possível para uma dama voltar para ocupar sua casa inicial, por exemplo.

2. O papel da função heurística neste caso é calcular a distância (de Manhattan) entre duas cidades indicadas. O objetivo é melhorar o desempenho sendo um cálculo muito rápido de fazer e se obter resultados. Permite ao algoritmo explorar os caminhos com custo menor que, provavelmente, são os mais promissores de serem navegados na sequência.

3. A lógica do algoritmo A* é utilizar uma função heurística para determinar o custo de um nó até o destino, somando-o ao custo do nó atual. O algoritmo então expande o nó com menor custo total, ou seja, a soma do custo do nó atual com o custo estimado do nó até o destino. O algoritmo continua expandindo os nós até encontrar o nó de destino ou até que não hajam mais nós a serem explorados. Ele pode ser considerado uma fusão de algum algoritmo guloso (greedy) e do algoritmo de Dijkstra, onde o último é utilizado para encontrar o caminho mais curto globalmente e primeiro o que parece mais vantajoso localmente.

4. A diferença entre A* e IDA* é que o A* é um algoritmo de busca informada, que utiliza uma heurística para estimar o custo restante para chegar ao destino, enquanto o IDA* é um algoritmo de busca não informada, que não utiliza heurística. O IDA* é uma versão do A* que utiliza uma busca em profundidade iterativa, onde a profundidade máxima da busca é aumentada a cada iteração, até que o nó de destino seja encontrado. O IDA* é mais eficiente em termos de memória, pois não armazena todos os nós visitados, mas é menos eficiente em termos de tempo, pois pode explorar caminhos desnecessários.
