from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    # if nums[0] == target - 1:
    #     return 1
    # elif nums[len(nums) -1] == target - 1:
    #     return len(nums)
    # else:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def best_searchInsert(nums: List[int], target: int) -> int:
    pos = 0
    for num in nums:
        if num < target:
            pos += 1
    return pos
    
    
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums, target)) # 2
    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target)) # 1
    nums = [1,3,5,6]
    target = 7
    print(searchInsert(nums, target)) # 4
    nums = [1,3,5,6]
    target = 0
    print(searchInsert(nums, target)) # 0
    nums = [1]
    target = 0
    print(searchInsert(nums, target)) # 0
    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target)) # 1
    nums = [1,3,5,6]
    target = 7
    print(searchInsert(nums, target)) # 4
    