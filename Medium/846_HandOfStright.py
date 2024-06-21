from collections import Counter
import heapq

def hand_of_stright_brutal(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    
    res = [[] for _ in range(groupSize)]
    
    hand.sort()
    j = 0
    while hand:
        first_card = hand[0]
        for i in range(groupSize):
            res[j].append(first_card + i)
            if first_card + i in hand:
                
                hand.remove(first_card + i)
            else:
                return False
        j += 1
    #print(res)        
    return True

def hand_of_stright_optimisedsss(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    
    hand = Counter(hand)
    for i in sorted(hand):
        if hand[i] > 0:
            for j in range(groupSize):
                if hand[i+j] < hand[i]:
                    return False
                hand[i+j] -= hand[i]
                

    return True

def hand_of_stright_optimised(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
        return False
    
    count = {}
    for i in hand:
        count[i] = 1 + count.get(i, 0)
        
    minH = list(count.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]
        
        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)
            
    return True
        
if __name__=="__main__":
    hand = [1,1,2,2,3,3]
    groupSize = 3
    print(hand_of_stright_brutal(hand, groupSize)) # True
    hand = [1,1,2,2,3,3]
    groupSize = 3
    print(hand_of_stright_optimised(hand, groupSize)) # True

    hand = [1,2,3,4,5]
    groupSize = 4
    print(hand_of_stright_brutal(hand, groupSize)) # False
    print(hand_of_stright_optimised(hand, groupSize)) # False
    

    