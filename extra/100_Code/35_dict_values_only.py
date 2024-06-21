
def dict_values_only() -> list:
    value_list = list()
    my_dict = dict()
    for i in range(1, 21):
        my_dict[i] = i**2
    for (k,v) in my_dict.items():
        value_list.append(v)
    return value_list

if __name__ == "__main__":
    print(dict_values_only())