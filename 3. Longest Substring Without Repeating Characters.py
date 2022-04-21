class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        step=0
        i=0
        memo={}
        maximum=float("-inf")
        while i<len(s):
            if s[i] not in stack:
                memo[s[i]]=i
                stack.append(s[i])
                i+=1
            else:
                maximum=max(maximum,i-step)
                index=stack.index(s[i])
                stack=stack[index+1:]
                step=memo[s[i]]+1 
                memo[s[i]]=i
                stack.append(s[i])
                i+=1
            
        maximum=max(maximum,i-step)
        return maximum
        
