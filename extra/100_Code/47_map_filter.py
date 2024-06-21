
def map_filter() -> list:
    return list(filter(lambda x: x%2 == 0, map(lambda x: x**2, range(1, 11))))

if __name__ == '__main__':
    print(map_filter())