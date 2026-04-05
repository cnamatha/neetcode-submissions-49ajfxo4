"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr=head
        new_l={}
        while curr:
            new_l[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            new_l[curr].next=new_l.get(curr.next)
            new_l[curr].random=new_l.get(curr.random)
            curr=curr.next
        return new_l[head]    
