def count_letters_digits() -> dict:
    res = dict()
    intake = input()
    for i in intake:
        if i.isalpha():
            res['LETTERS'] = res.get('LETTERS', 0) + 1
        elif i.isdigit():
            res['DIGITS'] = res.get('DIGITS', 0) + 1
        elif i == ' ':
            res['SPACE'] = res.get('SPACE', 0) + 1
        else:
            pass
    return res

if __name__ == '__main__':
    print(count_letters_digits())
    