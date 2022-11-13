class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count=defaultdict(int)
        result=0
        
        for i in range(0,len(nums)):
            
            new=defaultdict(int)
       
            if nums[i] % k ==0:
                
                count[nums[i]]+=1
                
                for val in count:
                    new[gcd(nums[i],val)]+=count[val]
            
            result+=new[k]
            
           
            count=new
        
        
        return result
        
                
            