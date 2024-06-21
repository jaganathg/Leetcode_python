

def reverse_string(s: list[str]) -> None:
    n = len(s)
    
    for i in range(n // 2):
        s[i] , s[n - i - 1] = s[n - i - 1], s[i]
        
    return s

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(reverse_string(s))
    
    s = ["H", "a", "n", "n", "a", "h"]
    print(reverse_string(s))