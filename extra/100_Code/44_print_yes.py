
def yes() -> str:
    intake = input()
    if intake == "yes" or intake == "YES" or intake == "Yes":
        return "Yes"
    else:
        return "No"
    
    
if __name__ == "__main__":
    print(yes())