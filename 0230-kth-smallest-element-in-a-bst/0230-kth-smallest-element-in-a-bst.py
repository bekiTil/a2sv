# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=None
        self.count=0
        def sorting(root,k):
            if not root:
                return 
            else:
                sorting(root.left,k)
                self.count+=1
                
                if self.count==k:
                    self.ans=root.val
                    return 
                sorting(root.right,k)
        sorting(root,k)
       
        return self.ans
            