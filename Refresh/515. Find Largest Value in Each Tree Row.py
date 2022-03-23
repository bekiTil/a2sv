#timeComplexity O(n)
#SpaceComplexity O(n) where n is the number of node 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        new=deque()
        value=deque()
        new.append(root)
        if not root:
            return []
        value.append(root.val)
        large=[]
        
        while new:
            large.append(max(value))
            width=len(new)
            for i in range(width):
                popped=new.popleft()
                value.popleft()
                if popped.left and popped.right:
                    new.append(popped.left)
                    value.append(popped.left.val)
                    new.append(popped.right)
                    value.append(popped.right.val)
                elif not popped.left and popped.right:
                    new.append(popped.right)
                    value.append(popped.right.val)
                elif not popped.right and popped.left:
                    new.append(popped.left)
                    value.append(popped.left.val)
        print(large)
                    
        return large
                    
            
