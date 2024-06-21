from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return  [int(i) for i in str((int(''.join(str(i) for i in digits)) + 1))]

def bestplusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits)))
        num = num + 1
        return [int(i) for i in str(num)]

if __name__ == '__main__':
    digits = [1,2,3]
    print(plusOne(digits)) # [1,2,4]
    digits = [4,3,2,1]
    print(plusOne(digits)) # [4,3,2,2]
    digits = [9]
    print(plusOne(digits)) # [1,0]
    