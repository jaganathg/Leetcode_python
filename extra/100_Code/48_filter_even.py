
def filter_range() -> list:
    return list(filter(lambda x: x % 2 == 0, range(1, 21)))


if __name__ == '__main__':
    print(filter_range())