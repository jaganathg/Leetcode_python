def sort_words() -> list:
    words = input()
    
    word_list = [word for word in words.split(',')]
        
    word_list.sort()
    print(', '.join(word_list))

if __name__ == '__main__':
    print(sort_words())
    
    
    