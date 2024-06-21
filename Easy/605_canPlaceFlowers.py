
def canPlaceFlower(flowerbed: list[int], flower: int) -> bool:
    if flower == 0:
        return True
    flowerbed = [0] + flowerbed + [0]
    count = 0
    for i in range(1, len(flowerbed)) :
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= flower


def canPlaceFlower_dyn(flowerbed: list[int], flower: int) -> bool:
    empty = 0 if flowerbed[0] else 1
    
    for flowr in flowerbed:
        if flowr:
            flower -= int((empty - 1) / 2)
            empty = 0
        else:
            empty += 1
    flower -= (empty) // 2
    
    return flower <= 0
    
    

if __name__=="__main__":
    print(canPlaceFlower([1,0,0,0,1], 1)) # True
    print(canPlaceFlower([1,0,0,0,1], 2)) # False
    print(canPlaceFlower([1,0,0,0,0,1], 2)) # False
    print(canPlaceFlower_dyn([0,0,1,0,0,0,1,1,0,0], 3)) # True
    print(canPlaceFlower_dyn([1,0,0,0,0,0,1,0], 3)) # True
    