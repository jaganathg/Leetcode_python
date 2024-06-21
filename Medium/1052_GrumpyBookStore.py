

def max_satisfied(customer: list[int], grumpy: list[int], minutes: int) -> int:
    my_table = list()
    
    for (cus, grp) in zip(customer, grumpy):
         my_table.append((cus, grp))
    
    # print(my_table)
    # print(len(my_table))

    max_satisfied = my_table[0][0] + my_table[1][0]
    print(max_satisfied)
    
    for i in range(2, len(my_table)):
        if my_table[i][1] == 0:
            max_satisfied += my_table[i][0]
    
    print(max_satisfied)
         
         
if __name__=="__main__":
    print(max_satisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))  # 16
   