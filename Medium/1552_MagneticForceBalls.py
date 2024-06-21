
def max_distance(position: list[int], balls: int) -> int:
    position.sort()
    left, right = 1, position[-1] - position[0]
    
    def can_ball_placed(mid_pos: int):
        count = 1
        last_postion = position[0]
        for i in range(1, len(position)):
            if position[i] - last_postion >= mid_pos:
                count += 1
                last_postion = position[i]
        return count
    
    while left <= right:
        mid = (left + right) // 2
        if can_ball_placed(mid) >= balls:
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__=='__main__':
    print(max_distance([1, 2, 3, 4, 7], 3))  # 3
    print(max_distance([5, 4, 3, 2, 1, 1000000000], 2))  # 999999999
    print(max_distance([79, 74, 57, 22], 4))  # 5
    print(max_distance([79, 74, 57, 22], 3))  # 22
    print(max_distance([79, 74, 57, 22], 2))  # 35
    print(max_distance([79, 74, 57, 22], 1))  # 57
   