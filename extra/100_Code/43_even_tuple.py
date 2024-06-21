
def even_tuple() -> list:
    my_tuple = (1, 2, 13, 14, 15, 6, 17, 18, 29, 10)
    my_list = list()
    for i in my_tuple:
        if i % 2 == 0:
            my_list.append(i)
    return my_list

if __name__ == "__main__":
    print(even_tuple())
    print(type(even_tuple()))
    