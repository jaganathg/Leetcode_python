from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # have a empty dictionary
    d = {}

    # enumerate list to get index and value
    for i, num in enumerate(nums):
        # try to get the missing value by subtracting num from target 
        #  and check if it exists in dictionary
        if target - num in d:
            # return the index from the for loop 'i' and index from above subtraction
            return [d[target - num], i]
        d[num] = i
        
        
if __name__ == "__main__":
    nums = [22, 11, 2, 5]
    target = 7
    print(twoSum(nums, target))