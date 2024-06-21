
def subarray_sum_divide(nums: list[int], k: int) -> int:
    dp = {0: 1}
    total = 0
    count = 0
    
    for num in nums:
        total += num
        rem = total % k
        
        count += dp.get(rem, 0)
        dp[rem] = dp.get(rem, 0) + 1
        
    return count

if __name__=="__main__":
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(subarray_sum_divide(nums, k)) # 7
    
    nums = [5]
    k = 9
    print(subarray_sum_divide(nums, k)) # 1
   