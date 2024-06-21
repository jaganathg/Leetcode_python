def upper_line() -> list:
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line.upper())
        else: 
            break
        
    for line in lines:
        print(line)
        
if __name__ == "__main__":
    upper_line()