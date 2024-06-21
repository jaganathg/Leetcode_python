def dict_num(num: int) -> dict:
    d = dict()
    for n in range(1, num + 1):
        d[n] = n * n
    return d

if __name__=='__main__':
    print(dict_num(8))