def duplicate_words() -> str:
    s = input()
    words = [word for word in s.split(' ')] 
    
    return ' '.join(sorted(list(set(words))))


if __name__ == '__main__':
    print(duplicate_words())