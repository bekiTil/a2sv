# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)
        traverse(root)
        value=float('inf')
        for i in range(1,len(ans)):
            value = min (ans[i]-ans[i-1],value)
        return value
            