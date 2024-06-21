
def dict_squre() -> dict:
    """ this function creates a dict in sequence with holding squre of the
    respective keys 
    please dont pass any input into this function"""
    my_dict = dict()
    for i in range(1, 21):
        my_dict[i] = i**2
    return my_dict

if __name__ == "__main__":
    print(dict_squre.__doc__)
    print(dict_squre())