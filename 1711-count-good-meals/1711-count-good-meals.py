class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        if len(deliciousness) == 1:
            return 0
        
        deliciousness.sort()
    
    
        count=defaultdict(int)
        
        for i in deliciousness:
            count[i]+=1
        
        max_sum=deliciousness[-1]+deliciousness[-2]
        max_two=1
        
        
        while max_sum//2 > 0:
            max_two*=2
            max_sum=max_sum//2
        ans=0 
        for i in deliciousness:
            check=1
            while check<=max_two:
                if check-i>=i:
                    if check-i==i and count[i]>0:
                        count[i]-=1
                        ans=(ans+count[i])% 1000000007
                    else:
                        ans=(ans+count[check-i])% 1000000007
                check*=2
        return ans
    
    """
       Time Complexity 
       O(20n)
       Space Complexity
       O(n)

        """
                        
                    
                
                