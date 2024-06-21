def get_odd() -> list:
    num = input()
    res = list()
    res = [i for i in num.split(',') if int(i)%2 != 0]
    return ", ".join(res)

if __name__ == '__main__':
    print(get_odd())