
from collections import Counter

# def majorityElements(nums: list[int]) -> int:
#     counts = Counter(nums)
#     return max(counts, key=counts.get)

def majorityElements(nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]

if __name__=="__main__":
    print(majorityElements([3,2,3])) # 3
    print(majorityElements([2,2,1,1,1,2,2])) # 2
    print(majorityElements([1])) # 1
    