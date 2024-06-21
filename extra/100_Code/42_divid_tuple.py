
def divide_tuple() -> tuple:
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return my_tuple[:5], my_tuple[5:]

if __name__ == '__main__':
    print(divide_tuple())
    print(type(divide_tuple()))