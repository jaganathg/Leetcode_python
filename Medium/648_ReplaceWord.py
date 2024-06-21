
def replaceWord(dictionary: list[str], sentence: str) -> str:
    words = sentence.split()
    
    for i in range(len(words)):
        for word in dictionary:
            if words[i].startswith(word):
                words[i] = word 
                break
    return ' '.join(words)

    
def LeetCode(dictionary: list[str], sentence: str) -> str:
        s = set(dictionary)
        sentence = sentence.split()
        for j, w in enumerate(sentence):
            for i in range(1, len(w)):
                db = w[:i]
                if w[:i] in s: 
                    sentence[j] = w[:i]
                    break
        return " ".join(sentence)


if __name__=="__main__":
    dictionary = ["cat", "bat", "rat"]
    sentence = "the pcattle was rattled by the battery"
    print(LeetCode(dictionary, sentence)) # Output: "the cat was rat by the bat"

    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(replaceWord(dictionary, sentence)) # Output: "a a b c"

    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    print(replaceWord(dictionary, sentence)) # Output: "a a a a a a a a bbb baba a"