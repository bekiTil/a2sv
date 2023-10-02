"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = deque([])
        if root:
            level.append(root)
        while level:
            
            length  = len(level)
            
            for count in range(length):
                node = level.popleft()
                
                if count == length - 1:
                    node.next = None
                else:
                    node.next = level[0]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return root
        
        