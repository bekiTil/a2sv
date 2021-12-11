class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new=[]
        
        for i in range (len(nums)):
            
            idx=i
            for j in range(i+1,len(nums)):
                if nums[idx]>nums[j]:
                    idx=j
            nums[idx],nums[i]=nums[i],nums[idx]
            if target==nums[i]:
                new.append(i)
        
        return new
            
      
            
