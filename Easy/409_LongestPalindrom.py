
from collections import Counter

def longestPalindrome(s: str) -> int:
    count = 0
    for v in Counter(s).values():
        count += v // 2 * 2
        if count % 2 == 0 and v % 2 == 1:
            count += 1
    return count

def testlongestPalindrome(s: str) -> int:
    count = set()
    res = 0
    
    for c in s:
        if c in count:
            count.remove(c)
            res += 2
        else:
            count.add(c)
            
    return res + 1 if len(count) > 0 else res
    

if __name__=="__main__":
    s = "abccccdd"
    print(longestPalindrome(s)) # 7
    s = "a"
    print(longestPalindrome(s)) # 1
    s = "bb"
    print(longestPalindrome(s)) # 2
    s = "ab"
    print(longestPalindrome(s)) # 1
    s = "abc"
    print(longestPalindrome(s)) # 1
    s = "ccc"
    print(longestPalindrome(s)) # 3