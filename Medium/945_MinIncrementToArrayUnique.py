
from collections import defaultdict

def minIncrementForUnique(nums: list[int]) -> int:

    #! not completed
    if not nums: 
        return 0
    
    counter = 0
    max_val = 0
    lookup_table = defaultdict(int)
    
    for num in nums:
        lookup_table[num] += 1
        if max_val < num:
            max_val = num
            
    for i in range(len(lookup_table)):
        if lookup_table[i] <= 1:
            continue
        duplicate = lookup_table[i] - 1
        lookup_table[i + 1] += duplicate
        lookup_table[i] = 1
        counter += duplicate
            
    # for num in nums:
    #     if num in lookup_table and lookup_table[num] >= 2:
    #         for idx in range(1, max_val + 2):
    #             if idx not in lookup_table:
    #                 counter += abs(idx - num)
    #                 lookup_table[idx] += 1
    #                 lookup_table[num] -= 1
        
    return counter

def minIncrement(nums: list[int]) -> int:
    if not nums: return 0
    
    nums.sort()
    counter = 0
    prev = nums[0]
    
    for idx in range(1, len(nums)):
        if nums[idx] <= prev:
            counter += prev - nums[idx] + 1
            nums[idx] = prev + 1
        prev = nums[idx]

    return counter

if __name__=="__main__":
    nums = [1,2,2]
    print(minIncrementForUnique(nums))  # Output: 1
    
    nums = [3,2,1,2,1,7]
    print(minIncrement(nums))  # Output: 6
    
   