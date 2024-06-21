
def appendChars(s: str, t: str) -> int:
    
    i = 0
    j = 0
    count = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
        
    count = len(t) - j
    return count
    

if __name__ == "__main__":
   

    s = "coaching"
    t = "coding"
    print(appendChars(s, t))  # Output: 4
    
    s = "abcde"
    t = "a"
    print(appendChars(s, t))  # Output: 0
    
    s = "z"
    t = "abcde"
    print(appendChars(s, t))  # Output: 5
    
    

   