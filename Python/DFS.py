# Grafo de exemplo (lista de adjacência)
grafo_dfs = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

# Conjunto para guardar os nós já visitados
visitados_dfs = set() 

def dfs(visitados, grafo, no):
    """
    Função para executar a travessia DFS em um grafo.
    """
    if no not in visitados:
        print(no, end=" ")
        visitados.add(no)
        # Para cada vizinho do nó atual, chama a função recursivamente
        for vizinho in grafo[no]:
            dfs(visitados, grafo, vizinho)

# Chamada inicial da função
print("Ordem da travessia DFS:")
dfs(visitados_dfs, grafo_dfs, 'A')
# Saída esperada: A B D E F C