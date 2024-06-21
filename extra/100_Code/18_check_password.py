import re 

def check_password_re() -> list:
    passwords = input()
    password_list = [password for password in passwords.split(',') ]
    valid_password = list()
    for password in password_list:
        if len(password) < 6 or len(password) > 12:
            continue
        elif not re.search('[a-z]', password):
            continue
        elif not re.search('[0-9]', password):
            continue
        elif not re.search('[A-Z]', password):
            continue
        elif not re.search('[$#@]', password):
            continue
        elif not re.search('\s', password):
            continue
        else:
            pass
        valid_password.append(password)
    return valid_password

def check_password() -> list:
    passwords = input()
    special_characters = ['$', '#', '@']
    password_list = [password for password in passwords.split(',') ]
    valid_password = list()
    for password in password_list:
        if len(password) < 6 or len(password) > 12:
            continue
        if not any(char.isdigit() for char in password):
            continue
        if not any(char not in special_characters for char in password):
            continue
        if not any(char.isupper() for char in password):
            continue
        if not any(char.islower() for char in password):
            continue
        valid_password.append(password)
    return valid_password

if __name__ == '__main__':
    print(check_password())
    print(check_password_re())