def fact(num: int):
    if num == 0:
        return 1
    return num * fact(num - 1)

x = fact(8)
print(x)