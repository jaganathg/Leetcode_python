
def map_list() -> list:
    return list(map(lambda x: x**2, range(1, 11)))

if __name__ == '__main__':
    print(map_list())