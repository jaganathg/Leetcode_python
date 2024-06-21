
from collections import defaultdict

def height_checker(heights: list[int]) -> int:
    if not heights:
        return 0
    count = 0
    df = defaultdict(int)
    for i, h in enumerate(heights):
        df[i] = h
        
    heights=sorted(heights)
    for i , h in enumerate(heights):
        if df[i] != h:
            count += 1
    return count

def leetcode_solution(self, heights: list[int]) -> int:
        c=heights[:]
        d=0
        c.sort()
        for i in range(len(c)):
            if heights[i]!=c[i]:
                d+=1
        return d

if __name__ == "__main__":
    h = [1,1,4,2,1,3]
    print(height_checker(h))
    
    h = [5,1,2,3,4]
    print(height_checker(h))
    
    h = [1,2,3,4,5]
    print(height_checker(h))