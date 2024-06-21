

def split_username() -> str:
    # Split username from email
    email = input("Enter email: ")
    username = email.split('@')[0]
    return username

import re

def split_name_re() -> str:
    email = input("Enter email: ")
    pat2 = "(\w+)@((\w+\.)+(com))"
    r2 = re.match(pat2, email)
    return r2.group(1)

if __name__ == "__main__":
    #print(split_username())
    print(split_name_re())