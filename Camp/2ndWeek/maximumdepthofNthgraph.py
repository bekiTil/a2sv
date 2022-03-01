#time complexity
#O(V+E)
#space Complexity
#O(V)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        
        def maximum(root,arr,length):
            if not root.children:
                length+=1
                arr.append(length)
                return
            else:
                for i in root.children:
                    new=length
                    new+=1
                    maximum(i,arr,new)
            return arr
        new=[]
        length=0
        if maximum(root,new,length)==None:
            return 1
        else:
            return max(maximum(root,new,length))
        
    
        
