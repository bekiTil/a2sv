# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        
        def addition(root,arr,total,targetSum):
            if not root.left and not root.right:
                total+=root.val
                if total==targetSum:
                    arr.append(True)
                else:
                    arr.append(False)
            else:
                i,j=root.left,root.right
                if not i:
                    new=total
                    new+=root.val
                    addition(j,arr,new,targetSum)
                elif not j:
                    new=total
                    new+=root.val
                    addition(i,arr,new,targetSum)
                else:
                    new=total
                    new+=root.val
                    addition(i,arr,new,targetSum)
                    addition(j,arr,new,targetSum)
            return arr
        new=[]
        total=0
        k=addition(root,new,total,targetSum)
        if True in k:
            return True
        else:
            return False
        
                    
