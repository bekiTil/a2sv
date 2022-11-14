class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        ans=[0]*(len(s)+1)
        
        for m in shifts:
            
            if m[2]==1:
                ans[m[0]]+=1
                ans[m[1]+1]-=1
            else:
                ans[m[0]]-=1
                ans[m[1]+1]+=1
        
        for i in range(1,len(s)):
            ans[i]+=ans[i-1]
        
        
        s=list(s)
        a=ord("a")
        for i in range(len(s)):
            char=ord(s[i])-97
            temp=(char+ans[i])%26
            s[i]=chr(temp+97)
        return "".join(s)
            