# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo=defaultdict(list)
        self.min=float("inf")
        self.max=float("-inf")
       
        level=deque()
       
        level.append((root,0))
        while level:
            length=len(level)
            temp=defaultdict(list)
            for val,col in level:
                temp[col].append(val.val)
                self.min,self.max=min(self.min,col),max(self.max,col)
            
            for val in temp:
                temp[val].sort()
                memo[val].extend(temp[val])
         
            
            for _ in range(length):
                val,col= level.popleft()
                if val.left:
                    level.append((val.left,col-1))
                if val.right:
                    level.append((val.right,col+1))
       
        ans=[]
        for i in range(self.min,self.max+1):
            ans.append(memo[i])
        return ans
        
            