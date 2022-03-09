class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        current=prices[0]
        maximum=float("-inf")
        for i in range(1,length):
            if prices[i]-current<0:
                current=prices[i]
            else:
                maximum=max(maximum,prices[i]-current)
        return  maximum if maximum>0 else 0
