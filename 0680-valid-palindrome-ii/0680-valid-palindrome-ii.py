class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s):
            i=0
            j=len(s)-1
            while i<=j:
                if s[i]!=s[j]:
                    return (i,j)
                i+=1
                j-=1
            return (-1,-1)
        def validity(s):
            i=0
            j=len(s)-1
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        if valid(s)!=(-1,-1):
            (x,y)=valid(s)
            if validity(s[:x]+s[x+1:]) or validity(s[:y]+s[y+1:]):
                return True
            else:
                return False
        else:
            return True