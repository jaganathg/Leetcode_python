

def sort_colors(nums: list[int]) -> None:
    
    left, right = 0, len(nums) - 1
    i = 0
    
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else: 
            i += 1
            
            
if __name__=="__main__":
    nums = [0,1,2,1,0,2]
    sort_colors(nums)
    print(nums)  # Output: [0,0,1,1,2,2]
    
    nums = [2,0,1]
    sort_colors(nums)
    print(nums)  # Output: [0,1,2]
    
    nums = [0]
    sort_colors(nums)
    print(nums)  # Output: [0]
    
    nums = [1]
    sort_colors(nums)
    print(nums)  # Output: [1]
    
    nums = [2]
    sort_colors(nums)
    print(nums)  # Output: [2]
    
    nums = [1,2,0]
    sort_colors(nums)
    print(nums)  # Output: [0,1,2]
    
   