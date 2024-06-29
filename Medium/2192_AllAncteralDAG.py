
def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[v].append(u)
        
    # print(graph)
        
    res = []
    
    def dfs( node, visited, ancestors):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                ancestors.add(neighbor)
                dfs(neighbor, visited, ancestors)
    
    for i in range(n):
        visited = set()
        ancestors = set()
        dfs(i, visited, ancestors)
        res.append(sorted(ancestors))
    return res


if __name__=="__main__":
    n = 8
    edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    print(getAncestors(n, edges))