def upper_lower() -> dict:
    res = dict()
    intake = input()
    for i in intake:
        if i.isupper():
            res['UPPER'] = res.get('UPPER', 0) + 1
        elif i.islower():
            res['LOWER'] = res.get('LOWER', 0) + 1
        else:
            pass
    return res

if __name__ == '__main__':
    print(upper_lower())