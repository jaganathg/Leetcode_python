def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    left, right = 1, x
    while left < right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid + 1
        else:
            right = mid
    return left - 1


if __name__=='__main__':
    print(mySqrt(1)) # 2
    print(mySqrt(8)) # 2
    print(mySqrt(9)) # 3
    print(mySqrt(16)) # 4
    print(mySqrt(25)) # 5
    print(mySqrt(36)) # 6
    print(mySqrt(49)) # 7
    print(mySqrt(64)) # 8
    print(mySqrt(81)) # 9
    print(mySqrt(100)) # 10
   