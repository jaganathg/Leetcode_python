def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
    
    
if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle)) # 2
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle)) # -1
    haystack = ""
    needle = ""
    print(strStr(haystack, needle)) # 0
    haystack = "a"
    needle = ""
    print(strStr(haystack, needle)) # 0
    haystack = "a"
    needle = "a"
    print(strStr(haystack, needle)) # 0