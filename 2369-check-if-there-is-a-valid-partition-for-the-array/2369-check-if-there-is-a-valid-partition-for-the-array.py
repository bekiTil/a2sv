class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp=[[False,0] for _ in range(len(nums)+1)]
        dp[0][0]=True
        
        
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                if dp[i-1][0] or (i-2>=0 and dp[i-2][0] and nums[i-2]==nums[i]):
                    dp[i+1][0]=True
            elif nums[i]==nums[i-1]+1:
                if dp[i][1]==1:
                    dp[i+1][0]=True
                    if i-2>=0 and dp[i-1][0]:
                        dp[i+1][1]+=1
                    
                elif dp[i][1]==0 and dp[i-1][0]:
                    dp[i+1][1]+=1
        return dp[-1][0]