
def minDays(bloomDay: list[int], no_boq: int, no_flr: int) -> int:
    if len(bloomDay) < no_boq * no_flr:
        return -1
    
    left = min(bloomDay)
    right = max(bloomDay)
    
    def can_make_boq(days: int) -> bool:
        flr = boq = 0
        
        for bloom in bloomDay:
            if bloom <= days:
                flr += 1
                if flr == no_flr:
                    boq += 1
                    flr = 0
            else:
                flr = 0
            if boq >= no_boq:
                return True
        return boq >= no_boq
    
    while left < right:
        mid = (left + right) // 2
        if can_make_boq(mid):
            right = mid
        else:
            left = mid + 1
    return left if can_make_boq(left) else -1


if __name__=="__main__":
    print(minDays([1,10,3,10,2], 3, 1)) # 3
    print(minDays([1,10,3,10,2], 3, 2)) # -1
    print(minDays([7,7,7,7,12,7,7], 2, 3)) # 12
    