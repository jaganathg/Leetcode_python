

def minDifference(nums: list[int]) -> int:
    if len(nums) <= 4:
        return 0

    nums.sort()
    
    return min(
        nums[-1]-nums[3],
        nums[-2]-nums[2],
        nums[-3]-nums[1],
        nums[-4]-nums[0]
    )
    
    
if __name__ == "__main__":
    nums = [5,3,2,4]
    print(minDifference(nums))
    nums = [1,5,0,10,14]
    print(minDifference(nums))
    nums = [6,6,0,1,1,4,6]
    print(minDifference(nums))
    nums = [1,5,6,14,15]
    print(minDifference(nums))
    nums = [82,81,95,75,20]
    print(minDifference(nums))
    