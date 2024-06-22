from collections import defaultdict


def num_of_subarray(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    perfix_sum = 0
    result = 0
    
    for num in nums:
        if num % 2:
            perfix_sum += 1
            
        if perfix_sum - k in count:
            result += count[perfix_sum - k]
            
        count[perfix_sum] += 1
        
    return result


def ptr3_num_of_subarray(nums: list[int], k: int) -> int:
    l, m = 0, 0
    res, odd = 0, 0
    
    for r in range(len(nums)):
        if nums[r] % 2:
            odd += 1
            
        while odd > k:
            if nums[l] % 2:
                odd -= 1
            l += 1
            m = l
        
        if odd == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l) + 1
    return res
    


if __name__=="__main__":
    print(num_of_subarray([1,1,2,1,1], 3)) # 2
    print(num_of_subarray([2,4,6], 1)) # 0
    print(num_of_subarray([2,2,2,1,2,2,1,2,2,2], 2)) # 16
    print(ptr3_num_of_subarray([2,2,2,1,2,2,1,2,1,2], 2)) # 16
   