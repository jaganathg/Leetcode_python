
def list_slice() -> tuple:
    my_list = list()
    for i in range(1, 21):
        my_list.append(i**2)
    return tuple(my_list)

if __name__ == '__main__':
    print(type(list_slice()))
    print(list_slice())