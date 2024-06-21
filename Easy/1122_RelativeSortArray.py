from collections import defaultdict

def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    dp = defaultdict(int)
    
    for i in arr1:
        dp[i] += 1
        
    # print(dp)
    res = []
    
    for i in arr2:
        res += [i] * dp[i]
        dp.pop(i)
    for i in sorted(dp):
        res += [i]* dp[i]
        
    return res

def relativeSortArray_dynamic(arr1: list[int], arr2: list[int]) -> list[int]:
    dp = defaultdict(int)
    end = []
    arr2_set = set(arr2)
    
    for i in arr1:
        if i not in arr2_set:
            end.append(i)
        dp[i] += 1
    end.sort()
        
    
    res = []
    for i in arr2:
        res += [i] * dp[i]
    res += end
    return res


if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(relativeSortArray(arr1, arr2))
    
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    print(relativeSortArray_dynamic(arr1, arr2))