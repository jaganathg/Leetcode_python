def long_str() -> str:
    intake = input("Enter two string with spaces: ")
    one, two = intake.split(" ")
    if len(one) > len(two):
        return one
    elif len(one) < len(two):
        return two
    else:
        return one, two
        
    
if __name__ == "__main__":
    print(long_str())