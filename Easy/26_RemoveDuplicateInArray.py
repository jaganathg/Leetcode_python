from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(removeDuplicates(nums)) # 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums)) # 5
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(removeDuplicates(nums)) # 1
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(removeDuplicates(nums)) # 9
    nums = []
    print(removeDuplicates(nums)) # 0
    