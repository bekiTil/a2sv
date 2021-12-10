class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(len(nums)):
            a=0
            for j in range(len(nums)):
                if  nums[i]>nums[j] and i!=j:
                    a+=1
            new.append(a)
        return new
