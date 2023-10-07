class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        
        count = defaultdict(int)
        
        maximum = 0
        for right in range(len(s)):
            
            if count[s[right]]:
                
                maximum = max(right-left,maximum)
                while s[left]!=s[right]:
                    count[s[left]]-=1
                    left+=1
                left+=1
                
            else:
                count[s[right]]+=1
        if len(s): 
            maximum = max(right-left + 1,maximum)
        
        return maximum
                    