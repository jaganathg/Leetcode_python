

def reverse_vowels (s: str) -> str:
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s) - 1
    
    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1
    return "".join(s)

if __name__=="__main__":
    s = "hello"
    print(reverse_vowels(s)) # Output: "holle"
    
    s = "leetcode"
    print(reverse_vowels(s)) # Output: "leotcede"
   


