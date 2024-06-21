

def find_judge(n: int, trust: list[list[int]]) -> int:
    people = [0] * (n + 1)
    
    for u, v in trust:
        people[u] -= 1
        people[v] += 1
        
    for i in range(1, n+1):
        if people[i] == n -1:
            return i
    return -1

if __name__ == "__main__":
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(find_judge(n, trust)) # 3
    
    n = 3
    trust = [[1, 3], [2, 3]]
    print(find_judge(n, trust)) # 3
    
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(find_judge(n, trust)) # -1