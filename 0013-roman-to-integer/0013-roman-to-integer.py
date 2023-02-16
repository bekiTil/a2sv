class Solution:
    def romanToInt(self, s: str) -> int:
        memo=defaultdict(int)
        memo["I"]=1
        memo["V"]=5
        memo["X"]=10
        memo["L"]=50
        memo["C"]=100
        memo["D"]=500
        memo["M"]=1000
        memo["IV"]=4
        memo["IX"]=9
        memo["XL"]=40
        memo["XC"]=90
        memo["CD"]=400
        memo["CM"]=900
        i=0
        ans=0
        while i+1<len(s):
            if memo[s[i:i+2]]!=0:
                ans+=memo[s[i:i+2]]
                i+=2
            else:
                ans+=memo[s[i]]
                i+=1
        while i<len(s):
            ans+=memo[s[i]]
            i+=1
        return ans
        