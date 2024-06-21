

def jump_game(nums: list[int]) -> bool:
    goal = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


if __name__=="__main__":
    print(jump_game([2, 3, 1, 1, 4]))  # True
    print(jump_game([3, 2, 1, 0, 4]))  # False
  