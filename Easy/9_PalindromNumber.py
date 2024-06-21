def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]
    
if __name__ == "__main__":
    x = 121
    print(isPalindrome(x))
    x = -121
    print(isPalindrome(x))
    x = 10
    print(isPalindrome(x))
    x = -101
    print(isPalindrome(x))
    x = 0
    print(isPalindrome(x))