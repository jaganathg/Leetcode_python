
def rob(nums: list[int]) -> int:
    
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    prev = nums[0]
    curr = max(nums[1], nums[0])
    
    for i in range(2, len(nums)):
        prev, curr = curr, max(nums[i] + prev, curr)
        
    return curr

if __name__=="__main__":
    print(rob([2, 3, 2]))  # Output: 3
    print(rob([1, 2, 3, 1]))  # Output: 4
    print(rob([0]))  # Output: 0
    print(rob([1]))  # Output: 1
   