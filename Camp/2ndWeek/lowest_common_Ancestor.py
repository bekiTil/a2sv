#Time Complexity 
#O(n)
#Space Complexity
#O(n)
#link https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.bench=[0]
        answer=[None]
        def deepNode(root,depth):
            if not root:
                if self.bench[0]<=depth:
                    self.bench[0]=depth
            else:
                depth+=1
                deepNode(root.left,depth)
                deepNode(root.right,depth)
        deepNode(root,0)
        def Ancestor(root,depth):
            if not root:
                return depth
            else:
                depth+=1
                left=Ancestor(root.left,depth)
                right=Ancestor(root.right,depth)
                if left==right:
                    if left==self.bench[0]:
                        answer[0]=root
                        return self.bench[0]
                    else:
                        return left 
                else:
                    if left==self.bench[0]:
                        if answer[0]==None:
                            answer[0]=root.left
                        return self.bench[0]
                    elif right==self.bench[0]:
                        if answer[0]==None:
                            answer[0]=root.right
                        return self.bench[0] 
                    else:
                        return left if left>right else right
        Ancestor(root,0)
        return answer[0]
