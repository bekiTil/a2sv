# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            temp=0
            if not root:
                return [0,None]
            else:
                value=prune(root.left)
                if value[0]==0:
                    root.left=None
                temp+=value[0]
                
                value=prune(root.right)
                if value[0]==0:
                    root.right=None
                temp+=value[0]
                
                
            return [temp+root.val,root]
        ans = prune(root)
        if ans[0]==0:
            return None
        else:
            return ans[1]
       