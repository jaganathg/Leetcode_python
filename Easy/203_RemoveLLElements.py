from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head is not None and head.val == val:
            head = head.next
        prev = None
        curr = head
        
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
    
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(6)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(6)
    
    s = Solution()
    res = s.removeElements(l1, 6)
    while res is not None:
        print(res.val, end=" ")
        res = res.next
    print()
    
    

    
    