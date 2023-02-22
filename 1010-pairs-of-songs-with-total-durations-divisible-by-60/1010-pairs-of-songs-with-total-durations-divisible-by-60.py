class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = defaultdict(int)
        
        
            
        ans = 0 
        
        for val in time:
            
            value = (60 - val%60)
           
            
            if value == 60:
                value =0
            ans += count[value]
           
            count[val%60]+=1
        return ans 
        