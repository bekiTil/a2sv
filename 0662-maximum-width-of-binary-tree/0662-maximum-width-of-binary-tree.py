# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        level = deque([(root,1)])
        
        while level:
           
            left = level[0][1]
            right = level[-1][1]
            self.max = max(self.max,right - left )
            
            length = len(level)
            for _ in range(length):
                node,value = level.popleft()
                if node.left :
                    level.append((node.left,(value*2)-1) )
                if node.right :
                    level.append((node.right,(value*2)))
        return self.max + 1
                
                
        