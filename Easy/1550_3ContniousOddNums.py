
def threeConsecutiveOdds(arr: list[int]) -> bool:
    count = 0
    
    for i in arr:
        if i % 2 == 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


if __name__=="__main__":
    arr = [2,6,4,1]
    print(threeConsecutiveOdds(arr))
    arr = [1,2,34,3,4,5,7,23,12]
    print(threeConsecutiveOdds(arr))
    arr = [1,2,1,1]
    print(threeConsecutiveOdds(arr))
    arr = [1,2,1,1,1]
    print(threeConsecutiveOdds(arr))