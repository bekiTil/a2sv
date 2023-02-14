class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        dp = [0 for _ in range(len(s)+1)]
        for index,char in enumerate(s):
            if char == 'b':
                count+=1
                dp[index+1]+=dp[index]
            else:
                dp[index+1]=min(count, dp[index] +1)
            
        return dp[-1]
        