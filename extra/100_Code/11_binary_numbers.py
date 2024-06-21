def check_binary() -> list:
    binary = input()
    lists = []
    listss = [list for list in binary.split(',')]
    for i in listss:
        if not int(i, 2) % 5:
            lists.append(i)
    return lists


if __name__ == '__main__':
    print(check_binary())