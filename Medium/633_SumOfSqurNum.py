
def sum_of_squre(target: int) -> bool:
    left = 0
    right = int(target ** 0.5)
    # print(right)
    temp = target ** 0.5
    print(temp)
    
    while left <= right:
        total = left ** 2 + right ** 2
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False

if __name__=="__main__":
    target = 22
    print(sum_of_squre(target))  # Output: True
    
    target = 33
    print(sum_of_squre(target))  # Output: False
    
    target = 44
    print(sum_of_squre(target))  # Output: True
    
    target = 55
    print(sum_of_squre(target))  # Output: True