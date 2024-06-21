from collections import defaultdict

def minimum_fuel_cost(roads: list[list[int]], seats: int) -> int:
    n_cities = len(roads) + 1
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    fuel = [0]  # Use a list to mutate the fuel variable inside dfs
    dfs(0, -1, graph, seats, fuel)
    return fuel[0]
        

def dfs(node: int, parent: int, graph: dict, seats: int, fuel: list) -> int:
    representative = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            representative += dfs(neighbor, node, graph, seats, fuel)
           
    if node != 0:
        fuel[0] += (representative + seats - 1) // seats
        
    return representative

            

if __name__== "__main__":
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    print(minimum_fuel_cost(roads, seats))  