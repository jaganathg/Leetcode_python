
def filter_list() -> list:
    my_list = list()
    for i in range(1, 21):
        my_list.append(i**2)
    return list(filter(lambda x: x % 2 == 0, my_list))


if __name__ == '__main__':
    print(filter_list())