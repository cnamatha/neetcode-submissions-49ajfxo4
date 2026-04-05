# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)     
        groupPrev=dummy
        while True:
            kth=self.kth(groupPrev,k)
            if not kth:
                break
            kthnext=kth.next
            prev=kthnext
            curr=groupPrev.next
            while curr!=kthnext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummy.next            

    def kth(self,curr,k):

        while curr and k:
            curr=curr.next
            k-=1
        return curr    

           


