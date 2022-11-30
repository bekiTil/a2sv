class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        temp=0
        for i in range(len(nums)):
            if temp==nums[-1]-nums[i]:
                return i
            temp=nums[i]
        return -1