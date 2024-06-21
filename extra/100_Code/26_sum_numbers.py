
def sum_numbers() -> int:
   
    intake = input("Enter two numbers: ")
    
    one, two = intake.split(" ")
    #print(one)
    #print(two)
    one = int(one)
    two = int(two)
    
    return one + two

if __name__ == "__main__":
    print(sum_numbers())
    