

def merge_array(num1: list[int], m: int, num2: list[int], n: int) -> list[int]:
    # Merge two sorted arrays
    num1[m:] = num2
    num1.sort()
    return num1

def merge_array_dyn(num1: list[int], m: int, num2: list[int], n: int) -> list[int]:
    
    last = m + n - 1
    
    while m > 0 and n > 0 :
        if num1[m - 1] > num2[n - 1]:
            num1[last] = num2[m - 1]
            m -= 1
        else:
            num1[last] = num2[n - 1]
            n -= 1
        last -= 1
        
    while n > 0:
        num1[last] = num2[n - 1]
        n, last = n -1, last - 1

if __name__ == "__main__":
    print(merge_array([1,2,3,0,0,0], 3, [2,5,6], 3))
    