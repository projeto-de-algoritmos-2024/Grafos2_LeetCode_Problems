import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # criando lista de adjacencia
        N = len(points)
    
        adj = {i:[] for i in range(N)} #dicionário com as listas vazias para cada nó

        #Calcula distancia entre os pares de pontos / coordenadas 'i' e 'j'
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distancia = abs(x1 - x2) + abs(y1 - y2) # Distancia de Manhattan entre os pontos
                #Adicionando distancia entre os nós nas listas de adjacencia
                adj[i].append([distancia, j])
                adj[j].append([distancia, i])

        # Implementando o algoritmo de Prim
        resultado = 0
        visitado = set()
        minHeap = [[0,0]] # Cada par ordenado é [custo, point] / point = nó

        #Continua até todos os nós serem percorridos
        while len(visitado) < N:
            custo, i = heapq.heappop(minHeap) # A cada iteração vamos 'popar' do minHeap / tirar o menor custo do heap
            if i in visitado:
                continue
            resultado += custo
            visitado.add(i)
            for custoVizinho, vizinho in adj[i]:
                if vizinho not in visitado:
                    heapq.heappush(minHeap, [custoVizinho, vizinho])

        return resultado


# Exemplo da própria questão
solucao = Solution()

points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(solucao.minCostConnectPoints(points1))

points2 = [[3,12],[-2,5],[-4,1]]
print(solucao.minCostConnectPoints(points2))