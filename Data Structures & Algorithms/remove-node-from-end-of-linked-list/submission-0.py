# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=actual=head
        while n:
            first=first.next
            n-=1
        if first is None:
            return head.next    
        while first.next:
            first=first.next
            actual=actual.next
        actual.next=actual.next.next

        return head
