class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=[]
        while columnNumber>0:
            value=columnNumber%26
            if value==0:
                ans.append(chr(64+26))
                columnNumber//=26
                columnNumber-=1
            
            else:
                ans.append(chr(64+value))
                columnNumber//=26
            
        
        ans.reverse()
        return "".join(ans)