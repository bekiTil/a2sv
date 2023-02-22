class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s=list(s)
        def check(s):
            for i in range(1,len(s)):
                if s[i]=="1" and s[i-1]=="0":
                    return True
            return False
        ans=0
        while check(s):
            i=0
            j=1
            while j<len(s):
                if s[i]=="0" and s[j]=="1":
                    s[i]="1"
                    s[j]="0"
                    i+=2
                    j+=2
                else:
                    i+=1
                    j+=1
                
            ans+=1  
            # print(s)
        return ans