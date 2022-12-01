# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0
        def dfs(node,target):
            if not node:
                return 
            if node.val==target:
                self.ans+=1
            dfs(node.left,target-node.val)
            dfs(node.right,target-node.val)
        def total(node,target):
            if not node:
                return 
            dfs(node,target)
            total(node.left,target)
            total(node.right,target)
        total(root,targetSum)
        return self.ans