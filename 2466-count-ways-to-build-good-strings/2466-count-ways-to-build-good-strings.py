class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans=[0]*(high+1)
        
        ans[0]=1
        for i in range(1,high+1):
            if i - one>=0:
                ans[i] += ans[i - one ]
            
            if i - zero >= 0:
                ans[i] += ans[i - zero] 
        
        total=0
        for i in range(low,high+1):
            print(i)
            total += ans[i]
        
        return total % (10**9 +7)