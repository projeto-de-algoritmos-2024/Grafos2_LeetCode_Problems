import heapq # Importando biblioteca heap
from typing import List # Vai ser usado para dizer que a matriz é uma lista de listas de inteiros

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Para caso a matriz esteja vazia, retorna 0
        if not matrix:
            return 0
        
        # Número de linhas
        linhas = len(matrix) 
        # Número de colunas
        colunas = len(matrix[0])

        # Movimentos que podem ser feitos
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #cima, baixo, esquerda, direita

        # Criando matriz auxiliar, toda com 1, que armazenará o valor do caminho mais longo
        aux_matrix = [[1] * colunas for l in range(linhas)]
        
        # Criando nosso heap, que armazenará nossos nós
        heap = []

        # Adicionando todas as células no heap, no seguinte formato: (valor, linha, coluna)
        for l in range(linhas):
            for c in range(colunas):
                heapq.heappush(heap, (matrix[l][c], l, c))
        
        # Enquanto o heap não estiver vazio
        while heap:
            # Pegando o menor elemento do heap, que é o elemtno prioritário, como o "atual"
            atual, l, c = heapq.heappop(heap)

            # x vai representar um avanço na linha, e y um avanço na coluna
            for x, y in moves:
                # calculando as coordenadas do vizinho do atual
                viz_l, viz_c = l + x, c + y

                # Primeiro verificando se o vizinho está dentro da matriz e depois, verifica se o vizinho é maior que o atual
                if 0 <= viz_l < linhas and 0 <= viz_c < colunas and matrix[viz_l][viz_c] > atual:
                    # Verificando se podemos aumentar o comprimento que leva até o vizinho
                    if aux_matrix[viz_l][viz_c] < aux_matrix[l][c] + 1:
                        # Se sim, colocamos esse novo caminho mais longo
                        aux_matrix[viz_l][viz_c] = aux_matrix[l][c] + 1

                        # Coloca esse vizinho no heap, para ele ser o novo atual, e olhar os seus vizinhos
                        heapq.heappush(heap, (matrix[viz_l][viz_c], viz_l, viz_c))
        
        # Após o processamento de todo o heap, nossa matriz auxiliar estará com o exato custo para chegar em cada célula; e como o processamento faz com que só altere o valor caso siga a regra do exercício de caminho crescente, o maior valor de toda a matriz, será justamente o maior caminho crescente
        return max(max(i) for i in aux_matrix)
            

# Exemplo da própria questão
solucao = Solution()
matrix1 = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
    ]
matrix2 = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
    ]
matrix3 = [
    [1]
    ]
print(f"{matrix1}\n{solucao.longestIncreasingPath(matrix1)}\n")
print(f"{matrix2}\n{solucao.longestIncreasingPath(matrix2)}\n")
print(f"{matrix3}\n{solucao.longestIncreasingPath(matrix3)}\n")

