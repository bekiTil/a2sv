class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache 
        def dp(i, k, prev, cnt):
          
            if k < 0: 
                return float('inf')
            if i == len(s): 
                return 0 
            ans = dp(i+1, k-1, prev, cnt)
            if prev == s[i]:
                if cnt not in [9,99]:
                    delta=0
                else:
                    delta=1
                if cnt==1:
                    delta+=1
                else:
                    delta+=0
                ans =min(ans,dp(i+1,k,s[i],cnt +1)+ delta)
            else: 
                ans = min(ans, dp(i+1, k, s[i], 1) + 1)
            return ans 
        
        return dp(0, k, "", 0)