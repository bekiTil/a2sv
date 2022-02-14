class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first=0
        last=1
      
        while first<len(nums) and last<len(nums):
            if nums[first]!=nums[last] and first+1==last:
                first+=1
                last+=1
                continue
            elif nums[first]!=nums[last] and first+1!=last:
                nums[first+1]=nums[last]
                nums[last]=0
                first+=1
                last+=1
                continue
            else:
                
                nums[last]=0
                last+=1
                continue
        return first+1
        
