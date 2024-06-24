from collections import deque

def minKBitFlips(nums: list[int], k: int) -> int:
    q = deque()
    res = 0
    
    for i in range(len(nums)):
        
        while q and i > q[0] + k - 1:
            q.popleft()
        
        if (nums[i] + len(q)) % 2 == 0:
            if i + k > len(nums):
                return -1
            res += 1
            q.append(i)
    return res


if __name__=="__main__":
    print(minKBitFlips([0,1,0], 1)) # 2
    print(minKBitFlips([1,1,0], 2)) # -1
    print(minKBitFlips([0,0,0,1,0,1,1,0], 3)) # 3
   