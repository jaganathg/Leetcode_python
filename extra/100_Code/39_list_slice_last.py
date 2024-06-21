def list_slice() -> list:
    my_list = list()
    for i in range(1, 21):
        my_list.append(i**2)
    return my_list[-5:]

if __name__ == '__main__':
    print(list_slice())