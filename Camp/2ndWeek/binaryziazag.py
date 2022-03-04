# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zigzag=[]
        if root==None:
            queue=deque()
        else:
            queue=deque([root])
        zigvalue=0
        while queue:
            n=len(queue)
            zigzag.append([])
            for i in range(n):
                root=queue.popleft()
                zigzag[-1].append(root.val)
                if not root.left and not root.right:
                    pass
                elif not root.left:
                    queue.append(root.right)
                elif not root.right:
                    queue.append(root.left)
                else:
                    queue.append(root.left)
                    queue.append(root.right)
            if zigvalue:
                zigzag[-1].reverse()
                zigvalue=0
            else:
                zigvalue=1
        return zigzag
