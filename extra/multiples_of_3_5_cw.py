
def multiples_of_3_5(number: int) -> int:
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)
      


if __name__ == "__main__":
    print(multiples_of_3_5(10)) # [0, 3, 5, 6, 9]
    print(multiples_of_3_5(16)) # [0, 3, 5, 6, 9, 10, 12, 15]    