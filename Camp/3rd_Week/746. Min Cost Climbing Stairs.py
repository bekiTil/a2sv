#top_down approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def costs(n):
            if n in memo:
                return memo[n]
            if n==1 or n==0:
                return 0
            else:
                new=min(cost[n-1]+costs(n-1),cost[n-2]+costs(n-2))
                memo[n]=new
                return new
        return costs(len(cost))
  #bottom_up approach
def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+2)
       
        dp[0]=0
        dp[1]=0
        dp[2]=dp[0]
        for i in range(3,len(dp)):
            dp[i]=min(dp[i-1]+cost[i-2],dp[i-2]+cost[i-3])
        return dp[-1]
