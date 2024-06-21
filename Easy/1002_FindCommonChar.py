from collections import Counter

def comm_chars(words: list[str] ) -> list[str]:
    # get hash of first word in words
    cnt = Counter(words[0])
    
    l = set(words[0])
    print(l)
    
    for word in words:
        cur_cnt = Counter(word)
        # compater base hash with the current hash and update the base hash
        for c in cnt:
            cnt[c] = min(cnt[c], cur_cnt[c])
            
    res = []
    for c in cnt:
        # loop number of times as per the key in hash.
        for i in range(cnt[c]):
            res.append(c)
    return res


def commonChars(self, words: list[str]) -> list[str]:
            arr = []
            l = set(words[0])
            for i in l:
                t = min(w.count(i) for w in words)
                arr+= [i]*t
            return arr

if __name__=="__main__":
    words = ["bella", "label", "roller"]
    print(comm_chars(words)) # ['e', 'l', 'l']
    
    words = ["cool", "lock", "cook"]
    print(comm_chars(words)) # ['c', 'o']
    
    