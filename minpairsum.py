 def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        max=0
        while j>i:
            if nums[i]+ nums[j]>max:
                max=nums[i]+ nums[j]
            i+=1
            j-=1
        return max
        
