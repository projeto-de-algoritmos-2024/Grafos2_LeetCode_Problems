# LeetCode Problems

## Sumário
1. [#329. Longest Increasing Path in a Matrix](#329-longest-increasing-path-in-a-matrix-🔴)

## #329. Longest Increasing Path in a Matrix 🔴

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

![ex1](img/ex1.png)

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]

Output: 4

Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

![ex1](img/ex2.png)

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]

Output: 4

Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]

Output: 1

## Como resolvemos?
Mesmo não sendo a melhor forma possível, decidimos fazer uma adaptação do Dijkstra, por ser um dos algoritmos vistos nesse módulo.

Enquanto o Dijkstra, mostra o menor caminho entre um ponto e outro, e a cada retirada do heap, atualizávamos com o menor caminho, aqui decidimos que a cada retirada do heap iríamos armazenar em uma matriz auxiliar o maior caminho até aquele nó, claro respeitando a regra de ser sempre um caminho crescente.

Então meio que a ideia veio do Dijkstra, porém não tratamos nosso problema com um grafo com pesos nas arestas, que iam se somando. Aqui o custo pra ir, sempre seria 1, porém era verificado se o vizinho era um número maior que o atual.
