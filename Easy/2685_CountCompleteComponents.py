from collections import defaultdict
from typing import List

def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            nodes = []
            dfs(i, visited, graph, nodes)
            if is_complete_component(nodes, graph):
                count += 1
    return count
            
      

def is_complete_component(nodes, graph) -> bool:
    size = len(nodes)
    for node in nodes:
        if len(graph[node]) != size - 1:
            return False
        for nod in graph[node]:
            if nod not in nodes:
                return False
    return True
    
      
def dfs(i, visited, graph, nodes):
    visited[i] = True
    nodes.append(i)
    for neighbor in graph[i]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, nodes)
            
            
if __name__=="__main__":
    print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]])) # 1
    