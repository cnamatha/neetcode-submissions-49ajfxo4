# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))
        new=ListNode()
        dummy=new
        while heap:
            val,i,l=heapq.heappop(heap)
            dummy.next=l
            dummy=dummy.next
            if l.next:
                heapq.heappush(heap,(l.next.val,i,l.next))
        return new.next        

            
