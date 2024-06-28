

def maximumImportance(n: int, roads: list[list[int]]) -> int:
    table = [0] * n
    
    for u, v in roads:
        table[u] += 1
        table[v] += 1
        
    label = 1
    res = 0
   
    for count in sorted(table):
        res += label * count
        label += 1
    return res
    

if __name__=="__main__":
    n = 5
    roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    print(maximumImportance(n, roads))
        
        
        