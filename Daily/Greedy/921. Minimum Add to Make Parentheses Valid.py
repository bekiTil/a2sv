class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=0
        new=0
        for i in s:
            if i=="(":
                stack+=1
            elif i==")" and stack:
                stack-=1
            else:
                new+=1
        return stack+new
