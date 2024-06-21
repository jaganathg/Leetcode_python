
def list_squre() -> list:
    squre_list = list()
    for i in range(1, 21):
        squre_list.append(i**2)
    return squre_list


if  __name__ == '__main__':
    print(list_squre())