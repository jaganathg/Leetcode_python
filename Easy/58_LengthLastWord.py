def lengthLastWord(s: str) -> int:
    if not s:
        return 0
    return len(s.split()[-1])

def try_length(s: str) -> int:
    if not s:
        return 0
    return len(s[-1])

if __name__ == "__main__":
    s = "Hello World"
    print(try_length(s)) # 5
    s = "Hello"
    print(try_length(s)) # 5
    s = "Hello "
    print(try_length(s)) # 5
    s = "Hello World "
    print(try_length(s)) # 5
    