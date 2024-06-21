from operator import itemgetter


def sort_tuple() -> tuple:
    res = list()
    while True:
        intake = input()
        if not intake:
            break
        res.append(tuple(intake.split(',')))
    print(res)
    print(sorted(res, key=itemgetter(0)))
    

if __name__ == '__main__':
    print(sort_tuple())