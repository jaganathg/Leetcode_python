

def rotate_array(nums: list[int], steps: int) -> None:
    """
    Rotate an array to the right by k steps in-place.
    """
    
    # steps = steps % len(nums)
    # print(steps)
    #! working but not accepted
    # nums[:] = nums[-steps:] + nums[:-steps]
    # return nums
    
    n = len(nums)
    print(n)
    k = steps % n
    print(k)
    
    def reverse_arry(nums: list[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    reverse_arry(nums, 0, n - 1)
    reverse_arry(nums, k, n - 1)
    reverse_arry(nums, 0, k - 1)
    
    return nums


    
    


if __name__=="__main__":
    nums = [1,2,3,4,5,6,7]
    steps = 3
    print(rotate_array(nums, steps))  # Output: [5,6,7,1,2,3,4]
    
    nums = [-1,-100,3,99]
    steps = 2
    print(rotate_array(nums, steps))  # Output: [3,99,-1,-100]
    
    nums = [1,2,3,4,5,6,7]
    steps = 3
    print(rotate_array(nums, steps))  # Output: [5,6,7,1,2,3,4]
    
   