#timeComplexity O(n^2)
#SpaceComplexity O(1)
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        i=0
        j=1
        addition=0
        high=nums[i]
        low=nums[i]
        if len(nums)==1:
            return addition 
        while i<=j and i<len(nums)-1:
            if len(nums)==j:
                    addition+=0
                    i+=1
                    j=i+1
                    high=nums[i]
                    low=nums[i]
            else:
                if nums[j]>high:
                    high=nums[j]
                if nums[j]<low:
                    low=nums[j]
                addition+=(high-low)
                
                j+=1
                
        return addition 
                
            
                
                
