from collections import deque

def longest_subarray(nums: list[int], limit: int) -> int:
    min_q = deque()
    max_q = deque()
    
    l, res = 0, 0
    
    for r in range(len(nums)):
        while min_q and nums[r] < min_q[-1]:
            min_q.pop()
        while max_q and nums[r] > max_q[-1]:
            max_q.pop()
            
        min_q.append(nums[r])
        max_q.append(nums[r])
        
        while max_q[0] - min_q[0] > limit:
            if nums[l] == max_q[0]:
                max_q.popleft()
            if nums[l] == min_q[0]:
                min_q.popleft()
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    print(longest_subarray([8, 2, 4, 7], 4))
    print(longest_subarray([10, 1, 2, 4, 7, 2], 5))
   
    