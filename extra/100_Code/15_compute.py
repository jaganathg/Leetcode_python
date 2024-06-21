def compute() -> int:
    a = input()
    n1 = int('%s' % a)
    print(n1)
    n2 = int('%s%s' % (a, a))
    print(n2)
    n3 = int('%s%s%s' % (a, a, a))
    print(n3)
    n4 = int('%s%s%s%s' % (a, a, a, a))
    print(n4)
    return n1 + n2 + n3 + n4

if __name__ == '__main__':
    print(compute())