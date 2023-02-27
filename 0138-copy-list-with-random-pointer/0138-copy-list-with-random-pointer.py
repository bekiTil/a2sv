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
        mp = {None: None}
        p = head
        while p:
            mp[p] = Node(p.val, None, None)
            p = p.next
        p = head
        while p:
            mp[p].next = mp[p.next]
            mp[p].random = mp[p.random]
            p = p.next
        return mp[head]
        