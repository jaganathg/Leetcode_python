def find_it_odd(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        
if __name__ == "__main__":
    # Example 1
    seq = [20, 1, -1, 2, -2, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
    print(find_it_odd(seq))  # Output: 5
    
    # Example 2
    seq = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
    print(find_it_odd(seq))  # Output: -1
    
    # Example 3
    seq = [10]
    print(find_it_odd(seq))  # Output: 10