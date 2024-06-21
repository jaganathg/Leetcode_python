def climbStairs(num: int) -> int:
    if num <= 1:
        return num
    prev, current = 0, 1
    for i in range( num ):
        prev , current = current, prev + current
    return current

if __name__=='__main__':
    print(climbStairs(5))