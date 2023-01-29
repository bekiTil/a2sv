class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=[0 for _ in range(len(s))]
        num=0
        for i,char in enumerate(s):
            if char == '1':
                dp[i]=dp[i-1]
                num+=1
            else:
                dp[i]=min(num,dp[i-1]+1)
        return dp[-1]