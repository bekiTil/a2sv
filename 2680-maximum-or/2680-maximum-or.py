class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        
        prefix = [0]
        suffix = [0]
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] | nums[i])
        for i in range(len(nums)-1,-1,-1):
            suffix.append(suffix[-1] | nums[i])
        prefix.append(0)
       
        suffix.append(0)
        suffix.reverse()
       
        
        
        
        maximum = float("-inf")
        for i in range(len(nums)):
            maximum =max( nums[i] * (2 ** k) | prefix[i] | suffix[i+2], maximum)
        return maximum
            
                