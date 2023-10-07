"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        order = []
        stack = []
        if head:
            stack.append(head)
        
        while stack:
            node = stack.pop()
            order.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        print(len(order))
        for i in range(len(order)-1):
            order[i+1].prev = order[i]
            order[i].next= order[i+1]
            order[i].child = None
        return head
                
                
          