import unicodedata
def ascii_to_unicode():
    s = input()
    u = s.encode("utf-8")
    print(u)
    print(type(u))


if __name__ == "__main__":
    ascii_to_unicode()