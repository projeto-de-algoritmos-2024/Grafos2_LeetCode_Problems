import heapq
from typing import List

class Solution:
    def Dijkstra(self, n: int, graph: List[List[int]], start: int) -> List[int]:
        # Usando lista para armazenar a distância do nó inicial para cada nó, começando todos com infinito
        lista_distancia = [float('inf')] * n
        # o nó inicial (start) vai começar em 0
        lista_distancia[start] = 0
        # Criando nosso min heap, que vai armazenar a distância e o nó de origem
        heap = [(0, start)]
        
        # Enquanto o heap não estiver vazio
        while heap:
            # Pegando a distancia do atual, e o nó atual, como sendo o elemento prioritário
            distancia_atual, atual = heapq.heappop(heap)
            # Se a distância atual for maior que a conhecida, ignoramos
            if distancia_atual > lista_distancia[atual]:
                continue

            # Para cada nó atual, que saiu do heap, olharemos seus vizinhos
            for vizinho, peso in graph[atual]:
                # Para cada um calcularemos a nova distância, considerando o peso da aresta
                distancia_nova = distancia_atual + peso
                # Se a distância nova for menor que a distancia atual, atualizaremos noss lista de distância
                if distancia_nova < lista_distancia[vizinho]:
                    lista_distancia[vizinho] = distancia_nova
                    # Colocando esse novo nó na heap
                    heapq.heappush(heap, (distancia_nova, vizinho))
        
        # Retornando lista com as distâncias
        return lista_distancia
    
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # Construção do grafo, que será uma lista de n listas vazias, onde cada índice, representará um nó
        grafo = [[] for i in range(n)]

        # Para cada nó, será adicionada (vizinho, peso) na lista correspondente aquele nó
        for j, (no, vizinho, peso) in enumerate(edges):
            grafo[no].append((vizinho, peso))
            # Porém como é bidirecional, precisamos adicionar também o caminho contrário
            grafo[vizinho].append((no, peso))
        
        # Encontrando as distâncias mínimas a partir do 0 (começo)
        lista_distancia_comeco = self.Dijkstra(n, grafo, 0)
        
        # Encontrando as distâncias mínimas a partir do nó n-1 (final), pois usaremos se uma aresta está ou não no caminho mais curto
        lista_distancia_final = self.Dijkstra(n, grafo, n - 1)
        
        # Distancia do menor caminho começando do 0
        distancia_menor_caminho = lista_distancia_comeco[n - 1]
        
        # Caso não haja nenhum menor caminho, e a distância entre 0 e n - 1, ainda seja infinita
        if distancia_menor_caminho  == float('inf'):
            return [False] * len(edges)

        # Incializando o vetor da resposta
        answer = []

        # Verificando se cada aresta faz parte do menor caminho
        for k, (a, b, peso) in enumerate(edges):
            # A soma da distancia de 0 ao nó a, de b até o nó n - 1, e o peso, dever ser igual a distância do menor caminho, claro que tem que fazer em ambos os sentidos, por ser um grafo bidirecional
            if lista_distancia_comeco[a] + lista_distancia_final[b] + peso == distancia_menor_caminho or \
               lista_distancia_comeco[b] + lista_distancia_final[a] + peso == distancia_menor_caminho:
                # Se sim, adiciona true no vetor de resposta
                answer.append(True)
            else:
                # Se não, adiciona false no vetor de resposta
                answer.append(False)
        
        return answer

# Exemplo da própria questão
solucao = Solution()
n1 = 6 
edges1 = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
print(solucao.findAnswer(n1,edges1))
n2 = 4
edges2 = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
print(solucao.findAnswer(n2,edges2))