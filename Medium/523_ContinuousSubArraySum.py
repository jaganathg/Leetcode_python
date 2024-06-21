
def CheckSubarraySum(nums: list[int], k: int) -> bool:
    """ using HashMap and having a 0 value in -1 index by default
    the do the check if the sum of values is mod of k and its >= 2"""
    
    dp = {0: -1}
    total = 0
    
    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in dp:
            dp[r] = i
        elif i - dp[r] > 1:
            return True
    return False

if __name__ == "__main__":
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(CheckSubarraySum(nums, k))
    
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(CheckSubarraySum(nums, k))
    
    nums = [23,2,6,4,7]
    k = 13
    print(CheckSubarraySum(nums, k))
    