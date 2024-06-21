from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current:
        while current.next and current.value == current.next.value:
            current.next = current.next.next
        current = current.next
    return current


if __name__ == '__main__':
    pass
    