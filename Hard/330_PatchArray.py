
def patch_array(nums: list[int], n: int) -> int:
    patches_count = 0
    miss = 1
    idx = 0
    
    while miss <= n:
        if idx < len(nums) and nums[idx] <= miss:
            miss += nums[idx]
            idx += 1
        else:
            miss += miss
            patches_count += 1
    return patches_count 
    
    
if __name__=="__main__":
    nums = [1, 3]
    n = 6
    print(patch_array(nums, n))
    
    nums = [1, 5, 10]
    n = 20
    print(patch_array(nums, n))
    
    nums = [1, 2, 2]
    n = 5
    print(patch_array(nums, n))
    
    nums = [1, 2, 31, 33]
    n = 40
    print(patch_array(nums, n))
    
    