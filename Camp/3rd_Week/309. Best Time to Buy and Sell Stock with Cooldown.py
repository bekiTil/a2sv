class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(days,stock,sold):
            if days<0:
                if stock:
                    return float("-inf")
                else:
                    return 0
            price=prices[days]
            if stock:
                buy=helper(days-2,False,False)-price
                hold=helper(days-1,True,False)
                return max(buy,hold)
            else:
                
                sell=helper(days-1,True,False)+price
                avoid=helper(days-1,False,False)
                return max(sell,avoid)
        return helper(len(prices)-1,False,False)
