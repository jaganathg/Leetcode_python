import re

def toCamelCase(text):
    words = re.split('-|_', text)
    return words[0] + ''.join([word.capitalize() for word in words[1:]])

def toCamelCase_re(text):
    return re.sub('[_-](.)', lambda match: match.group(1).upper(), text)


if __name__ == '__main__':
    print(toCamelCase("the-stealth-warrior"))
    print(toCamelCase("The_Stealth_Warrior"))
    print(toCamelCase_re("The_Stealth-Warrior"))