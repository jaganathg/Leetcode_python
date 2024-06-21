
from heapq import heappop, heappush

def findMaxCapital(no_proj: int, cap: int, profits: list[int], capital: list[int]) -> int:
    projects = list(zip(capital, profits))
    
    projects.sort()
    
    max_heap = []
    index = 0
    
    for _ in range(no_proj):
        while index < len(projects) and projects[index][0] <= cap:
            heappush(max_heap, -projects[index][1])
            index += 1
            
        if not max_heap:
            break
        
        cap += -heappop(max_heap)
        
    return cap


if __name__=="__main__":
    no_proj = 2
    cap = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    
    print(findMaxCapital(no_proj, cap, profits, capital))
    
    no_proj = 3
    cap = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    
    print(findMaxCapital(no_proj, cap, profits, capital))