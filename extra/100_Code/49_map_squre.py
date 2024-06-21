
def map_squre() -> list:
    return list(map(lambda x: x**2, range(1, 21)))


if __name__ == '__main__':
    print(map_squre())