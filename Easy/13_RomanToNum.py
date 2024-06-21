def romanToNumer(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    prev = 0
    for c in s:
        curr = roman_dict[c]
        if curr > prev:
            result += curr - 2 * prev
        else:
            result += curr
        prev = curr
    return result
            
if __name__ == "__main__":
    s = "III"
    print(romanToNumer(s))
    s = "IV"
    print(romanToNumer(s))
    s = "V"
    print(romanToNumer(s))
    s = "IX"
    print(romanToNumer(s))
    s = "XIV"
    print(romanToNumer(s))