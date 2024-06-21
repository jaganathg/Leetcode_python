def add_binary(a: str, b: str) -> str:
    return "{0:b}".format(int(a, 2) + int(b, 2))

if __name__=='__main__':
    # Time: O(n)
    # Space: O(1)
    print(add_binary('11', '1')) # 100
    print(add_binary('1010', '1011')) # 10101
    
    
