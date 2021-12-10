class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        idx=0
        new=[]
        for i in range(len(nums)):
            min=nums[i]
            for j in range(i+1,len(nums)):
                if min>nums[j]:
                    min=nums[j]
                    idx=j
    
                
            nums[idx],nums[i]=nums[i],min
            if min==target:
                new.append(i)
        return new
            
