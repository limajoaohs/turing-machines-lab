import collections
grafo = {
    "A" : ["B","C"],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visitados_bfs = set()
fila = collections.deque()

def bfs(visitados,grafo,no_inicial):
    visitados.add(no_inicial)
    fila.append(no_inicial)
    while fila:
        vertice = fila.popleft()
        print(vertice,end = " ")
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

bfs(visitados_bfs, grafo, 'A')