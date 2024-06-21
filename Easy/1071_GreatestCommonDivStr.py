
def string_div(str1: str, str2: str) -> str:
    if not str1 or not str2:
        return ""
    if str1[0] != str2[0]:
        return ""
    
    if len(str1) < len(str2):
        str1, str2 = str2, str1
        
    if len(str1) % len(str2) == 0:
        if str2 == str1[:len(str2)]:
            return str2
    elif len(str1) % 2 == 0 and len(str2) % 2 == 0:
        if str2[:2] == str1[:2]:
            return str2[:2]
        
def string_div_dyn(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)
    
    def isDiv(i) -> bool:
        if len1 % i or len2 % i:
            return False
        f1, f2 = len1 // i, len2 // i
        return str1[:i] * f1 == str1 and str1[:i] * f2 == str2
    
    for i in range(min(len1, len2), 0, -1):
        if isDiv(i):
            return str1[:i]
    return ""

def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1: return ""

    return str1[:math.gcd(len(str1), len(str2))]
        
        
if __name__ == "__main__":
    print(string_div("abab", "ab"))
    print(string_div_dyn("abcdef", "abc"))
    print(string_div("abcabc", "abc"))
    print(string_div("leet", "code"))