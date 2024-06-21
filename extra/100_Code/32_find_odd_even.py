def odd_or_even() -> str:
    n = int(input())
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
if __name__ == "__main__":
    print(odd_or_even())