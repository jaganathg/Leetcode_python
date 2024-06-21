def kidsWithCandies(candies: list[int], extra_candies: int)  -> list[bool]:
    max_candies = max(candies)
    print(max_candies)
    return [candy + extra_candies >= max_candies for candy in candies]

def kidsWithCandies_brutal(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies = 0
    for candy in candies:
        if candy > max_candies:
            max_candies = candy
            
    return [candy + extra_candies >= max_candies for candy in candies]


if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extra_candies = 3
    print(kidsWithCandies_brutal(candies, extra_candies)) # [True, True, True, False, True]
    candies = [4, 2, 1, 1, 2]
    extra_candies = 1
    print(kidsWithCandies_brutal(candies, extra_candies)) # [True, False, False, False, False]
    candies = [12, 1, 12]
    extra_candies = 10
    print(kidsWithCandies_brutal(candies, extra_candies)) # [True, False, True]
    