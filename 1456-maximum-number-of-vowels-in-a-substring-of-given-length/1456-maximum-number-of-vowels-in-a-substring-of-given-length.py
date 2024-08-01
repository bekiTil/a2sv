class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set(['a','e','i','o','u'])
        
        
        temp=0
        ans=0
        
        for i in s[:k]:
            if i in vowels:
                temp+=1
        ans = max(temp, ans)
        
        left = 0
        for right in s[k:]:
            if right in vowels:
                temp+=1
            if s[left] in vowels:
                temp-=1
            left+=1
            ans = max(temp, ans)
        return ans
        
        
        
            
        
        