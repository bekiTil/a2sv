# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob(root):
            if not root:
                return (0,0)
            else:
                left_unUsed,left_used=rob(root.left)
                right_unUsed, right_used=rob(root.right)
                
                unUsed=max(left_unUsed+right_unUsed,left_used+right_used,left_unUsed+right_used,left_used+right_unUsed)
                used=(left_unUsed+right_unUsed)+root.val
                return (unUsed,used)
        return max(rob(root))