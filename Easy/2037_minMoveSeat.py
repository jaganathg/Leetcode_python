

def min_move(seat: list[int], stud: list[int]) -> int:
    seat.sort()
    stud.sort()
    res = 0
    
    for i in range(0, len(seat)):
            res += abs(seat[i] - stud[i])
    return res

def min_move_dyn(seat: list[int], stud: list[int]) -> int:
    seat.sort()
    stud.sort()
    
    return sum(abs(a - b) for a, b in zip(seat, stud))

if __name__=="__main__":
    seat = [3, 1, 5]
    stud = [2, 7, 4]
    print(min_move_dyn(seat, stud))
    
    seats = [4,1,5,9]
    students = [1,3,2,6]
    print(min_move(seats, students))
    