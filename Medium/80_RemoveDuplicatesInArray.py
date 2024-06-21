from collections import defaultdict

def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    count = 0
    
    dp = defaultdict(int)
    
    for num in nums:
        dp[num] += 1
        count += 1
        if dp[num] > 2:
            dp[num] -= 1
            count -= 1
            
    nums.clear()
    
    for key, val in dp.items():
        for _ in range(0,val):
            nums.append(key)
    
    print(nums)
    
    return count

def removeDuplicates_dyn(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    
    write_index = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[write_index - 2]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

if __name__=="__main__":
    nums = [1,1,2]
    print(removeDuplicates_dyn(nums))  # Output: 2
    
    nums = [0,0,1,1,1,1,1,2,2,3,3,4]
    print(removeDuplicates_dyn(nums))  # Output: 5
    
    nums = [1,1,1]
    print(removeDuplicates_dyn(nums))  # Output: 1
    

    
    
    