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
