

def merge_string_alternatively(word1: str, word2: str) -> str:
    
    result = ""
    for i in range(min(len(word1), len(word2))):
        result += word1[i] + word2[i]
    result += word1[i+1:] + word2[i+1:]
    return result

if __name__ == "__main__":
    print(merge_string_alternatively("abc", "def"))
    print(merge_string_alternatively("ab", "def"))
    print(merge_string_alternatively("abc", "de"))
    print(merge_string_alternatively("abc", "d"))