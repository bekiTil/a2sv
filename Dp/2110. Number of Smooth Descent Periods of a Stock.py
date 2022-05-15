class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp=[1]*len(prices)
        j=0
        for i in range(1,len(prices)):
            if prices[j]==prices[i]+1:
                dp[i]+=dp[j]
            j=i
        return sum(dp)
