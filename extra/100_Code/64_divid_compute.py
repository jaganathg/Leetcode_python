
def compute_div(num: int) -> float:
    res = 0.0
    for i in range(1, num+1):
        res += i / (i + 1)
    return res

if __name__ == '__main__':
    print(compute_div(5))