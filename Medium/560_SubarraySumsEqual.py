
def subarraySumDivbyK( nums: list[int] , k: int) -> int:
    dp = {0: 1}
    total = 0
    count = 0
    
    for num in nums:
        total += num
        diff = total - k
        
        count += dp.get(diff, 0)
        dp[total] = dp.get(total, 0) + 1
       
    return count

if __name__=="__main__":
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(subarraySumDivbyK(nums, k)) # 7
    
    nums = [1, 1, 1, 1, 1]
    k = 3
    print(subarraySumDivbyK(nums, k)) # 1
    
    
            
            