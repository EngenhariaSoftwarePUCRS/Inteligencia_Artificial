Essa atividade pode ser feita em duplas. Para responder as questões a seguir, considere o material que está na semana 4:

## Questão 1

Como base no pdf de aula e materiais complementares, entenda o propósito e a lógica do algoritmo de agrupamento particional k-Means.
Tente entender também o método do cotovelo que visa estimar o valor de k.
A seguir , faça um passo a passo, a exemplo do material de aula, para a questão abaixo que foi extraída de uma prova. Documente esse passo a passo e poste no link abaixo. Exiba os cálculos tal como no feito nos slides de aula.
Crie um 3o programa, a partir dos disponíveis no moodle, aplicando o k-Means aos  dados da tabela abaixo (da questão de prova). Analise o melhor valor para k com o método do cotovelo. Poste o seu programa também no link abaixo.

## Questão 2

Apresente os cálculos e os centróides encontrados após uma iteração do algoritmo k-Means para os dados da tabela a seguir. Considere k=2 e que os centróides foram inicializados com os dados das linhas 3 e 4 da tabela. Use a distância de Manhatan em seus cálculos. Use no máximo 2 casas decimais, se necessário.

$d(x_i, x_j) = \sum\limits_{l=1}^{d} |x_i^l - x_j^l|$

| | atributo1 | atributo2 | atributo3 | atributo4 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 5 | 4 | 3 | 1 |
| 2 | 1 | 0 | 1 | 2 |
| 3 | 2 | 1 | 0 | 1 |
| 4 | 6 | 3 | 6 | 1 |
| 5 | 3 | 4 | 2 | 3 |
| 6 | 3 | 3 | 1 | 3 |

### Resposta

Centróides Iniciais = {
    C1: (2, 1, 0, 1)
    C2: (6, 3, 6, 1)
}


Distâncias = {
$d(C1, 1) = 2-5 + 1-4 + 0-3 + 1-1 = 3 + 3 + 3 + 0 = 9$

$d(C2, 1) = 6-5 + 3-4 + 6-3 + 1-1 = 1 + 1 + 3 + 0 = 5$

Logo $1 \in C2$


$d(C1, 2) = 2-1 + 1-0 + 0-1 + 1-2 = 1 + 1 + 1 + 1 = 4$

$d(C2, 2) = 6-1 + 3-0 + 6-1 + 1-2 = 5 + 3 + 5 + 1 = 14$

Logo $2 \in C1$


$d(C1, 3) = 2-2 + 1-1 + 0-0 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C2, 3) = 6-2 + 3-1 + 6-0 + 1-1 = 4 + 2 + 6 + 0 = 12$

Logo $3 \in C1$


$d(C1, 4) = 2-6 + 1-3 + 0-6 + 1-1 = 4 + 2 + 6 + 0 = 12$

$d(C2, 4) = 6-6 + 3-3 + 6-6 + 1-1 = 0 + 0 + 0 + 0 = 0$

Logo $4 \in C2$


$d(C1, 5) = 2-3 + 1-4 + 0-2 + 1-3 = 1 + 3 + 2 + 2 = 8$

$d(C2, 5) = 6-3 + 3-4 + 6-2 + 1-3 = 3 + 1 + 4 + 2 = 10$

Logo $5 \in C1$


$d(C1, 6) = 2-3 + 1-3 + 0-1 + 1-3 = 1 + 2 + 1 + 2 = 6$

$d(C2, 6) = 6-3 + 3-3 + 6-1 + 1-3 = 3 + 0 + 5 + 2 = 10$

Logo $6 \in C1$
}

Agrupamentos = {
    C1: {
        2: (1, 0, 1, 2)
        3: (2, 1, 0, 1)
        5: (3, 4, 2, 3)
        6: (3, 3, 1, 3)
    }
    C2: {
        1: (5, 4, 3, 1)
        4: (6, 3, 6, 1)
    }
}

Centróides Finais = {
    C1: (
        $(1 + 2 + 3 + 3) \over 4$,
        $(0 + 1 + 4 + 3) \over 4$,
        $(1 + 0 + 2 + 1) \over 4$,
        $(2 + 1 + 3 + 3) \over 4$,
    )
    C1: (2.25, 2, 1, 2.25)
    C2: (
        $(5 + 6) \over 2$,
        $(4 + 3) \over 2$,
        $(3 + 6) \over 2$,
        $(1 + 1) \over 2$,
    )
    C2: (5.5, 3.5, 4.5, 1)
}    
