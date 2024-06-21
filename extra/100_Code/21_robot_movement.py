import math

def robot_movement() -> int:
    # Robot movement
    # The robot can only move in the right and down direction
    # The robot can move only to the right and down
    pos = [0, 0]
    while True:
        intake = input()
        if not intake:
            break
        direction, steps = intake.split(' ')
        steps = int(steps)
        if direction == "UP":
            pos[0] += steps
        elif direction == "DOWN":
            pos[0] -= steps
        elif direction == "LEFT":
            pos[1] += steps
        elif direction == "RIGHT":
            pos[1] -= steps
        else:
            pass
    return round(math.sqrt(pos[0]**2 + pos[1]**2))

if __name__ == "__main__":
    print(robot_movement())