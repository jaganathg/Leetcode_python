

def max_satisfied(customer: list[int], grumpy: list[int], minutes: int) -> int:
    satisfied = 0
    windows = 0
    left = 0
    max_val = 0

    for right in range(len(customer)):
        if grumpy[right]:
            windows += customer[right]
        else:
            satisfied += customer[right]
            
        if right - left + 1 > minutes:
            if grumpy[left]:
                windows -= customer[left]
            left += 1
        max_val = max(max_val, windows)
    return satisfied + max_val
        
         
         
if __name__=="__main__":
    print(max_satisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))  # 16
   