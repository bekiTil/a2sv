# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total=[0]
        def dfs(total,root,father,grandfather):
            if root:
                if grandfather:
                    if grandfather%2==0:
                        total[0]+=root.val
                dfs(total,root.left,root.val,father)
                dfs(total,root.right,root.val,father)
        dfs(total,root,None,None)
        print(total)
        return total[0]
