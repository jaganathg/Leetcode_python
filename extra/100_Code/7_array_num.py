data_str = input()
dimension = [int(x) for x in data_str.split(',')]
row_num = dimension[0]
col_num = dimension[1]
multilist = [[0 for col in range(col_num)] for col in range(row_num)]
print("--------------------------------")
print(multilist)
print("$$$$$$$--------------------------------$$$$$$")
for row in range(row_num):
    for col in range(col_num):
        multilist[row][col] = row * col
print(multilist)
