
def word_count() -> dict:
    word_dict = dict()
    while True:
        words = input("Enter sentence: ")
        if not words:
            break
        wordList = [word for word in words.split(' ')]
        for word in wordList:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict

def wordcount() -> dict:
    word_dict = dict()
    intake = input()
    for word in intake.split():
        word_dict[word] = word_dict.get(word, 0) + 1
        
    words = word_dict.keys()
    
    for w in words:
        print(f"{w}: {word_dict[w]}")

if __name__ == "__main__":
    print(wordcount())