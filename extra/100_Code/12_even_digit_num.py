def even_digit():
    res = list()
    for i in range(1000, 3001):
        flag = 1
        for j in str(i):
            if ord(j) % 2 != 0:
                flag = 0
        if flag == 1:
            res.append(i)
    return res

if __name__ == '__main__':
    print(even_digit())