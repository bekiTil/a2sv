class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
       
        dic={}
        def robber(node):
            if node>=length:
                return 0
            elif node in dic:
                return dic[node]
            else:
                new=nums[node]
                robs = robber(node+1)
                leave=new+robber(node+2)
                memo=max(robs,leave)
                dic[node]=memo
                return memo
        return robber(0)
        
                
            
                
