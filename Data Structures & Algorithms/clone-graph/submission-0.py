"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        q=deque([node])
        cloned={node:Node(node.val)}
        while q:
            curr=q.popleft()
            for i in curr.neighbors:
                if i not in cloned:
                    cloned[i]=Node(i.val)
                    q.append(i)
                cloned[curr].neighbors.append(cloned[i])
        return cloned[node]                