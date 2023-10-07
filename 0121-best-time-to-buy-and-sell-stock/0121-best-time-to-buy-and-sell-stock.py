class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = prices[-1]
        ans = 0
        
        for i in range(len(prices)-2,-1,-1):
            
            if prices[i] < maximum:
                ans = max(ans, maximum - prices[i])
            maximum = max(maximum, prices[i])
        return ans