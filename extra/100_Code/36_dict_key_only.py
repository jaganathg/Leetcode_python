
def dict_key_only() -> dict:
    key_list = list()
    my_dict = dict()
    for i in range(1, 21):
        my_dict[i] = i**2
    for k in my_dict.keys():
        key_list.append(k)
    return key_list

if __name__ == "__main__":
    print(dict_key_only())