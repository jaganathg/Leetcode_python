

def array_to_phon_no( num: list) -> str:
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*num)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(array_to_phon_no(numbers))