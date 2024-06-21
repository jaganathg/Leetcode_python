
def length_runtime_error():
    intake = input("Enter a length:")
    length = int(intake)
    if length == 3:
        raise RuntimeError("Length must be greater than 3")
    else:
        print(f"Length is {length}")
    return length

if __name__ == "__main__":
    print(length_runtime_error())