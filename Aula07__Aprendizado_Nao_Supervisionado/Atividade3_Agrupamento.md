Essa atividade pode ser feita em duplas. Para responder as questões a seguir, considere o material que está na semana 4:

## Integrantes

- Felipe Freitas
- Luiza Heller

## Atividade

Como base no pdf de aula e materiais complementares, entenda o propósito e a lógica do algoritmo de agrupamento particional k-Means.
Tente entender também o método do cotovelo que visa estimar o valor de k.
A seguir, faça um passo a passo, a exemplo do material de aula, para a questão abaixo que foi extraída de uma prova. Documente esse passo a passo e poste no link abaixo. Exiba os cálculos tal como no feito nos slides de aula.
Crie um 3o programa, a partir dos disponíveis no moodle, aplicando o k-Means aos  dados da tabela abaixo (da questão de prova). Analise o melhor valor para k com o método do cotovelo. Poste o seu programa também no link abaixo.

Apresente os cálculos e os centróides encontrados após uma iteração do algoritmo k-Means para os dados da tabela a seguir. Considere k=2 e que os centróides foram inicializados com os dados das linhas 3 e 4 da tabela. Use a distância de Manhatan em seus cálculos. Use no máximo 2 casas decimais, se necessário.

$distance(x_i, x_j) = \sum\limits_{l=1}^{d} |x_i^l - x_j^l|$

$Inertia = \sum(distance(point, centroid)^2)$

Distortion = $Inertia\over{n}$

| | atributo1 | atributo2 | atributo3 | atributo4 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 5 | 4 | 3 | 1 |
| 2 | 1 | 0 | 1 | 2 |
| 3 | 2 | 1 | 0 | 1 |
| 4 | 6 | 3 | 6 | 1 |
| 5 | 3 | 4 | 2 | 3 |
| 6 | 3 | 3 | 1 | 3 |

### Resposta

#### K = 2

Centróides Iniciais = {<br>
    C1: (2, 1, 0, 1)<br>
    C2: (6, 3, 6, 1)<br>
}

Distâncias = {<br>
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
<br>}

Agrupamentos = {<br>
    G1: {<br>
        2: (1, 0, 1, 2)<br>
        3: (2, 1, 0, 1)<br>
        5: (3, 4, 2, 3)<br>
        6: (3, 3, 1, 3)<br>
    }<br>
    G2: {<br>
        1: (5, 4, 3, 1)<br>
        4: (6, 3, 6, 1)<br>
    }<br>
}

Centróides K2 = {<br>
    C1: (
        $(1 + 2 + 3 + 3) \over 4$,
        $(0 + 1 + 4 + 3) \over 4$,
        $(1 + 0 + 2 + 1) \over 4$,
        $(2 + 1 + 3 + 3) \over 4$
    )<br>
    C1: (2.25, 2, 1, 2.25)<br>
    C2: (
        $(5 + 6) \over 2$,
        $(4 + 3) \over 2$,
        $(3 + 6) \over 2$,
        $(1 + 1) \over 2$
    )<br>
    C2: (5.5, 3.5, 4.5, 1)<br>
}

Distâncias = {<br>
$d(C1, 1) = (2.25 - 5) + (2 - 4) + (1 - 3) + (2.25 - 1) = 2.75 + 2 + 2 + 1.25 = 8$

$d(C2, 1) = (5.5 - 5) + (3.5 - 4) + (4.5 - 3) + (1 - 1) = 0.5 + 0.5 + 1.5 + 0 = 2.5$

Logo $1 \in C2$


$d(C1, 2) = (2.25 - 1) + (2 - 0) + (1 - 1) + (2.25 - 2) = 1.25 + 2 + 1 + 0.25 = 4.5$

$d(C2, 2) = (5.5 - 1) + (3.5 - 0) + (4.5 - 1) + (1 - 2) = 4.5 + 3.5 + 3.5 + 1 = 12.5$

Logo $2 \in C1$


$d(C1, 3) = (2.25 - 2) + (2 - 1) + (1 - 0) + (2.25 - 1) = 0.25 + 1 + 1 + 1.25 = 3.5$

$d(C2, 3) = (5.5 - 2) + (3.5 - 1) + (4.5 - 0) + (1 - 1) = 3.5 + 2.5 + 4.5 + 0 = 10.5$

Logo $3 \in C1$


$d(C1, 4) = (2.25 - 6) + (2 - 3) + (1 - 6) + (2.25 - 1) = 3.75 + 1 + 5 + 1.25 = 11$

$d(C2, 4) = (5.5 - 6) + (3.5 - 3) + (4.5 - 6) + (1 - 1) = 0.5 + 0.5 + 1.5 + 0 = 2.5$

Logo $4 \in C2$


$d(C1, 5) = (2.25 - 3) + (2 - 4) + (1 - 2) + (2.25 - 3) = 0.75 + 2 + 1 + 0.75 = 4.5$

$d(C2, 5) = (5.5 - 3) + (3.5 - 4) + (4.5 - 2) + (1 - 3) = 2.5 + 0.5 + 2.5 + 2 = 7.5$

Logo $5 \in C1$


$d(C1, 6) = (2.25 - 3) + (2 - 3) + (1 - 1) + (2.25 - 3) = 0.75 + 1 + 0 + 0.75 = 2.5$

$d(C2, 6) = (5.5 - 3) + (3.5 - 3) + (4.5 - 1) + (1 - 3) = 2.5 + 0.5 + 3.5 + 2 = 8.5$

Logo $6 \in C1$
<br>}

Inertia K2 = {<br>
    C1: $d(C1, 2)^2 + d(C1, 3)^2 + d(C1, 5)^2 + d(C1, 6)^2 = 4.5^2 + 3.5^2 + 4.5^2 + 2.5^2 = 20.25 + 12.25 + 20.25 + 6.25 = 59$<br>
    C2: $d(C2, 1)^2 + d(C2, 4)^2 = 2.5^2 + 2.5^2 = 6.25 + 6.25 = 12.5$<br>
}

$WCSS = Inertia C1 + Inertia C2 = 59 + 12.5 = 71.5$


#### K = 3

Centróides Iniciais = {<br>
    C1: (5, 4, 3, 1)<br>
    C2: (2, 1, 0, 1)<br>
    C3: (3, 4, 2, 3)<br>
}

Distâncias = {<br>
$d(C1, 1) = 5-5 + 4-4 + 3-3 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C2, 1) = 2-5 + 1-4 + 0-3 + 1-1 = 3 + 3 + 3 + 0 = 9$

$d(C3, 1) = 3-5 + 4-4 + 2-3 + 3-1 = 2 + 0 + 1 + 2 = 5$

Logo $1 \in C1$


$d(C1, 2) = 5-1 + 4-0 + 3-1 + 1-2 = 4 + 4 + 2 + 1 = 11$

$d(C2, 2) = 2-1 + 1-0 + 0-1 + 1-2 = 1 + 1 + 1 + 1 = 4$

$d(C3, 2) = 3-1 + 4-0 + 2-1 + 3-2 = 2 + 4 + 1 + 1 = 8$

Logo $2 \in C2$


$d(C1, 3) = 5-2 + 4-1 + 3-0 + 1-1 = 3 + 3 + 3 + 0 = 9$

$d(C2, 3) = 2-2 + 1-1 + 0-0 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C3, 3) = 3-2 + 4-1 + 2-0 + 3-1 = 1 + 3 + 2 + 2 = 8$

Logo $3 \in C2$


$d(C1, 4) = 5-6 + 4-3 + 3-6 + 1-1 = 1 + 1 + 3 + 0 = 5$

$d(C2, 4) = 2-6 + 1-3 + 0-6 + 1-1 = 4 + 2 + 6 + 0 = 12$

$d(C3, 4) = 3-6 + 4-3 + 2-6 + 3-1 = 3 + 1 + 4 + 2 = 10$

Logo $4 \in C1$


$d(C1, 5) = 5-3 + 4-4 + 3-2 + 1-3 = 2 + 0 + 1 + 2 = 5$

$d(C2, 5) = 2-3 + 1-4 + 0-2 + 1-3 = 1 + 3 + 2 + 2 = 8$

$d(C3, 5) = 3-3 + 4-4 + 2-2 + 3-3 = 0 + 0 + 0 + 0 = 0$

Logo $5 \in C3$


$d(C1, 6) = 5-3 + 4-3 + 3-1 + 1-3 = 2 + 1 + 2 + 2 = 7$

$d(C2, 6) = 2-3 + 1-3 + 0-1 + 1-3 = 1 + 2 + 1 + 2 = 6$

$d(C3, 6) = 3-3 + 4-3 + 2-1 + 3-3 = 0 + 1 + 1 + 0 = 2$

Logo $6 \in C3$
}

Agrupamentos = {<br>
    G1: {<br>
        1: (5, 4, 3, 1)<br>
        4: (6, 3, 6, 1)<br>
    }<br>
    G2: {<br>
        2: (1, 0, 1, 2)<br>
        3: (2, 1, 0, 1)<br>
    }<br>
    G3: {<br>
        5: (3, 4, 2, 3)<br>
        6: (3, 3, 1, 3)<br>
    }<br>
}

Inertia K3 = {<br>
    C1: $d(C1, 1)^2 + d(C1, 4)^2 = 0^2 + 5^2 = 25$<br>
    C2: $d(C2, 2)^2 + d(C2, 3)^2 = 4^2 + 0^2 = 16$<br>
    C3: $d(C3, 5)^2 + d(C3, 6)^2 = 0^2 + 2^2 = 4$<br>
}

$WCSS = Inertia C1 + Inertia C2 + Inertia C3 = 25 + 16 + 4 = 45$


#### K = 4

Centróides Iniciais = {<br>
    C1: (5, 4, 3, 1)<br>
    C2: (2, 1, 0, 1)<br>
    C3: (6, 3, 6, 1)<br>
    C4: (3, 3, 1, 3)<br>
}

Distâncias = {<br>
$d(C1, 1) = 5-5 + 4-4 + 3-3 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C2, 1) = 2-5 + 1-4 + 0-3 + 1-1 = 3 + 3 + 3 + 0 = 9$

$d(C3, 1) = 6-5 + 3-4 + 6-3 + 1-1 = 1 + 1 + 3 + 0 = 5$

$d(C4, 1) = 3-5 + 3-4 + 1-3 + 3-1 = 2 + 1 + 2 + 2 = 7$

Logo $1 \in C1$


$d(C1, 2) = 5-1 + 4-0 + 3-1 + 1-2 = 4 + 4 + 2 + 1 = 11$

$d(C2, 2) = 2-1 + 1-0 + 0-1 + 1-2 = 1 + 1 + 1 + 1 = 4$

$d(C3, 2) = 6-1 + 3-0 + 6-1 + 1-2 = 5 + 3 + 5 + 1 = 14$

$d(C4, 2) = 3-1 + 3-0 + 1-1 + 3-2 = 2 + 3 + 1 + 1 = 7$

Logo $2 \in C2$


$d(C1, 3) = 5-2 + 4-1 + 3-0 + 1-1 = 3 + 3 + 3 + 0 = 9$

$d(C2, 3) = 2-2 + 1-1 + 0-0 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C3, 3) = 6-2 + 3-1 + 6-0 + 1-1 = 4 + 2 + 6 + 0 = 12$

$d(C4, 3) = 3-2 + 3-1 + 1-0 + 3-1 = 1 + 2 + 1 + 2 = 6$

Logo $3 \in C2$


$d(C1, 4) = 5-6 + 4-3 + 3-6 + 1-1 = 1 + 1 + 3 + 0 = 5$

$d(C2, 4) = 2-6 + 1-3 + 0-6 + 1-1 = 4 + 2 + 6 + 0 = 12$

$d(C3, 4) = 6-6 + 3-3 + 6-6 + 1-1 = 0 + 0 + 0 + 0 = 0$

$d(C4, 4) = 3-6 + 3-3 + 1-6 + 3-1 = 3 + 0 + 5 + 2 = 10$

Logo $4 \in C3$


$d(C1, 5) = 5-3 + 4-4 + 3-2 + 1-3 = 2 + 0 + 1 + 2 = 5$

$d(C2, 5) = 2-3 + 1-4 + 0-2 + 1-3 = 1 + 3 + 2 + 2 = 8$

$d(C3, 5) = 6-3 + 3-4 + 6-2 + 1-3 = 3 + 1 + 4 + 2 = 10$

$d(C4, 5) = 3-3 + 3-4 + 1-2 + 3-3 = 0 + 1 + 1 + 0 = 2$

Logo $5 \in C4$


$d(C1, 6) = 5-3 + 4-3 + 3-1 + 1-3 = 2 + 1 + 2 + 2 = 7$

$d(C2, 6) = 2-3 + 1-3 + 0-1 + 1-3 = 1 + 2 + 1 + 2 = 6$

$d(C3, 6) = 6-3 + 3-3 + 6-1 + 1-3 = 3 + 0 + 5 + 2 = 10$

$d(C4, 6) = 3-3 + 3-3 + 1-1 + 3-3 = 0 + 0 + 0 + 0 = 0$

Logo $6 \in C4$
<br>}

Agrupamentos = {<br>
    G1: {<br>
        1: (5, 4, 3, 1)<br>
    }<br>
    G2: {<br>
        2: (1, 0, 1, 2)<br>
        3: (2, 1, 0, 1)<br>
    }<br>
    G3: {<br>
        4: (6, 3, 6, 1)<br>
    }<br>
    G4: {<br>
        5: (3, 4, 2, 3)<br>
        6: (3, 3, 1, 3)<br>
    }<br>
}

Inertia K4 = {<br>
    C1: $d(C1, 1)^2 = 0^2 = 0$<br>
    C2: $d(C2, 2)^2 + d(C2, 3)^2 = 4^2 + 0^2 = 16$<br>
    C3: $d(C3, 4)^2 = 0^2 = 0$<br>
    C4: $d(C4, 5)^2 + d(C4, 6)^2 = 2^2 + 0^2 = 4$<br>
}

$WCSS = Inertia C1 + Inertia C2 + Inertia C3 + Inertia C4 = 0 + 16 + 0 + 4 = 20$


#### K = 5

| 1 | 5 | 4 | 3 | 1 |
| 2 | 1 | 0 | 1 | 2 |
| 3 | 2 | 1 | 0 | 1 |
| 4 | 6 | 3 | 6 | 1 |
| 5 | 3 | 4 | 2 | 3 |
| 6 | 3 | 3 | 1 | 3 |
Centróides Iniciais = {<br>
    C1: (5, 4, 3, 1)<br>
    C2: (1, 0, 1, 2)<br>
    C3: (2, 1, 0, 1)<br>
    C4: (6, 3, 6, 1)<br>
    C5: (3, 4, 2, 3)<br>
}

Distâncias = {<br>
$C1 = 1 \therefore $1 \in C1$

$C2 = 2 \therefore $2 \in C2$

$C3 = 3 \therefore $3 \in C3$

$C4 = 4 \therefore $4 \in C4$

$C5 = 5 \therefore $5 \in C5$

$d(C1, 6) = 5-3 + 4-3 + 3-1 + 1-3 = 2 + 1 + 2 + 2 = 7$

$d(C2, 6) = 1-3 + 0-3 + 1-1 + 2-3 = 2 + 3 + 0 + 1 = 6$

$d(C3, 6) = 2-3 + 1-3 + 0-1 + 1-3 = 1 + 2 + 1 + 2 = 6$

$d(C4, 6) = 6-3 + 3-3 + 6-1 + 1-3 = 3 + 0 + 5 + 2 = 10$

$d(C5, 6) = 3-3 + 4-3 + 2-1 + 3-3 = 0 + 1 + 1 + 0 = 2$

Logo $6 \in C5$
<br>}

Agrupamentos = {<br>
    G1: { 1: (5, 4, 3, 1) }
    G2: { 2: (1, 0, 1, 2) }
    G3: { 3: (2, 1, 0, 1) }
    G4: { 4: (6, 3, 6, 1) }
    G5: {<br>
        5: (3, 4, 2, 3)<br>
        6: (3, 3, 1, 3)<br>
    }<br>
}

Inertia K5 = {<br>
    C1: $d(C1, 1)^2 = 0^2 = 0$<br>
    C2: $d(C2, 2)^2 = 0^2 = 0$<br>
    C3: $d(C3, 3)^2 = 0^2 = 0$<br>
    C4: $d(C4, 4)^2 = 0^2 = 0$<br>
    C5: $d(C5, 5)^2 + d(C5, 6)^2 = 2^2 + 0^2 = 4$<br>
}

$WCSS = Inertia C1 + Inertia C2 + Inertia C3 + Inertia C4 + Inertia C5 = 0 + 0 + 0 + 0 + 4 = 4$


#### K = 6

Centróides = Dados

Distâncias = 0 = Inertia = WCSS
