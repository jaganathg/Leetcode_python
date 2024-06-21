from typing import Optional, List
def mergeTwoListsOld(list1: Optional[List], list2: Optional[List]) -> Optional[List]:
    return sorted((list1 + list2))

    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        emptyList = ListNode()
        currentList = emptyList
        
        while list1 and list2:
            if list1.val < list2.val:
                currentList.next = list1
                list1 = list1.next
            else:
                currentList.next = list2
                list2 = list2.next
            currentList = currentList.next
            
        if list1:
            currentList.next = list2
        elif list2:
            currentList.next = list1
            
        return currentList.next


if __name__ == "__main__":
    
    list1 = ListNode()
    list2 = ListNode()
    list1 = [1, 2, 4, 6]
    list2 = [1, 3, 4]
    ss = Solution()
    
    print(ss.mergeTwoLists(list1, list2)) # [1, 2, 4, 1, 3, 4]