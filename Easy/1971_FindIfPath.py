
def validPath(n: int, edges: list[list[int]], src: int, des: int) -> bool:
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    def dfs(node):
        if node == des:
            return True
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False
    return dfs(src)


if __name__=="__main__":
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 3)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 4)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 3)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 0)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 1)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 2)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 4)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 3)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 0)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 1)) # True
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 2)) # True